import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check", ROOT / "scripts/check.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CheckTests(unittest.TestCase):
    def test_metadata_and_reference_failures_are_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill = root / "adlc/example"
            skill.mkdir(parents=True)
            path = skill / "SKILL.md"
            valid = "---\nname: example\ndescription: A test skill.\nlicense: MIT\n---\n"
            (skill / "reference.md").write_text("Useful local reference.\n")
            path.write_text(valid + "[Local](reference.md)\n")
            self.assertEqual(module.check(root), ([], 1))
            path.write_text(valid.replace("name: example", "name: wrong"))
            self.assertTrue(any("invalid/duplicate name" in e for e in module.check(root)[0]))
            path.write_text(valid + "[Missing](absent.md)\n")
            self.assertTrue(any("broken link" in e for e in module.check(root)[0]))
            (root / "outside.md").write_text("Must not become a hidden dependency.\n")
            path.write_text(valid + "[Escapes](../../outside.md)\n")
            self.assertTrue(any("escapes" in e for e in module.check(root)[0]))
            path.write_text(valid + "[Encoded escape](%2E%2E/%2E%2E/outside.md)\n")
            self.assertTrue(any("escapes" in e for e in module.check(root)[0]))


if __name__ == "__main__":
    unittest.main()
