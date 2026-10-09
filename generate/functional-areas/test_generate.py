"""Focused checks for relationship validation and generated documentation."""

import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

import generate

OUTPUT_DIR = generate.ROOT.parents[1] / "docs/functional-areas-preview"


class GenerationTests(unittest.TestCase):
    def test_missing_class_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown classification"):
            generate.class_refs({"all_of": ["MISSING"]}, {})

    def test_misplaced_dependency_is_rejected(self):
        expression = {
            "all_of": ["CLASS_A"],
            "exclude_functional_areas": ["AREA"],
        }
        with self.assertRaisesRegex(ValueError, "one all_of/any_of"):
            generate.class_refs(expression, {"CLASS_A": {}})

    def test_nested_expression(self):
        expression = {
            "all_of": [
                "CLASS_A",
                {"any_of": ["CLASS_B", "CLASS_C"]},
            ]
        }
        classes = {identifier: {} for identifier in ("CLASS_A", "CLASS_B", "CLASS_C")}
        self.assertEqual(
            generate.class_refs(expression, classes),
            ["CLASS_A", "CLASS_B", "CLASS_C"],
        )

    def test_dependency_cycle_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "cycle"):
            generate.check_cycles(
                {"A": ["B"], "B": ["A"]},
                "Dependency",
            )

    def test_unknown_assumption_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(
                generate.ROOT / "references",
                root / "references",
            )

            path = root / "references/functional_area_specifications.yaml"
            spec = generate.read_yaml(path)
            spec["functional_areas"][0]["calculations"][0]["assumption_ids"].append(
                "MISSING"
            )
            path.write_text(
                yaml.safe_dump(spec),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "unknown assumption MISSING"):
                generate.load_references(root)

    def test_generated_pages(self):
        refs = generate.load_references()
        pages = [
            (path.stem, generate.read_yaml(path))
            for path in sorted((generate.ROOT / "content").glob("*.yaml"))
        ]
        self.assertTrue(pages, "No narrative content files found")

        titles = {
            content["functional_area_id"]: (content["title"], slug)
            for slug, content in pages
        }

        for slug, content in pages:
            with self.subTest(page=slug):
                page = generate.render(content, refs, titles)
                output_path = OUTPUT_DIR / f"{slug}.md"

                self.assertTrue(
                    output_path.exists(),
                    f"Missing {output_path}; run the generator first",
                )
                self.assertEqual(
                    page,
                    output_path.read_text(encoding="utf-8"),
                    "Generated page is stale; regenerate it",
                )

                technical_heading = '??? info "Technical details"'
                self.assertIn(technical_heading, page)
                self.assertIn('!!! info "Definition"', page)
                self.assertNotIn("Future enhancements", page)

                if content.get("notes", "").strip():
                    self.assertIn("## Notes", page)
                    self.assertLess(
                        page.index("## Notes"),
                        page.index(technical_heading),
                    )
                else:
                    self.assertNotIn("## Notes", page)


if __name__ == "__main__":
    unittest.main()
