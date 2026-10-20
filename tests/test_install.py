import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parent.parent

class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='nord-sway-test-')
        self.addCleanup(self.temp.cleanup)
        self.target = Path(self.temp.name)

    def run_theme(self, *args):
        return subprocess.run([sys.executable, str(REPO / 'install.py'), *args,
                               '--target-home', str(self.target)], text=True, capture_output=True, check=True)

    def test_install_restore_and_edited_profiles(self):
        sway = self.target / '.config/sway/config'
        sway.parent.mkdir(parents=True)
        sway.write_text('# previous desktop\n')
        self.run_theme()
        self.assertIn('Nord', sway.read_text())
        css = self.target / '.config/waybar/style.css'
        self.assertIn(str(self.target), css.read_text())
        self.assertNotIn('@DATA@', css.read_text())
        css.write_text(css.read_text() + '\n/* custom edit */\n')
        self.run_theme('restore')
        self.assertEqual(sway.read_text(), '# previous desktop\n')
        self.assertFalse(css.exists())
        sway.write_text('# edited previous desktop\n')
        self.run_theme('apply')
        self.assertIn('custom edit', css.read_text())
        self.run_theme('restore')
        self.assertEqual(sway.read_text(), '# edited previous desktop\n')

    def test_symlink_is_restored_without_modifying_target(self):
        external = self.target / 'external-kdeglobals'
        external.write_text('[General]\nColorScheme=Original\n')
        link = self.target / '.config/kdeglobals'
        link.parent.mkdir(parents=True)
        link.symlink_to(external)
        self.run_theme()
        self.assertFalse(link.is_symlink())
        self.assertEqual(external.read_text(), '[General]\nColorScheme=Original\n')
        self.run_theme('restore')
        self.assertTrue(link.is_symlink())
        self.assertEqual(link.resolve(), external)

    def test_dry_run_does_not_create_configuration(self):
        self.run_theme('--dry-run')
        self.assertEqual(list(self.target.iterdir()), [])

if __name__ == '__main__': unittest.main()
