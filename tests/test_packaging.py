"""Verifica a distribuição Claude ZIP usando unittest padrão."""
import subprocess
import sys
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent.parent

class PackageTests(unittest.TestCase):
    def test_zip_layout_and_entries(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "package_skill.py")], check=True)
        target = ROOT / "dist" / "academic-research-architect.zip"
        with ZipFile(target) as archive:
            names = archive.namelist()
            self.assertIn("academic-research-architect/SKILL.md", names)
            self.assertTrue(all(p.startswith("academic-research-architect/") for p in names))
            self.assertFalse(any(p.endswith("/README.md") for p in names))
            self.assertTrue(all(".." not in Path(p).parts for p in names))
            self.assertGreaterEqual(len(names), 8)

if __name__ == "__main__":
    unittest.main()

