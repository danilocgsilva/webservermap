import sys
sys.path.insert(1, "..")
from webservermap.Debian import Debian
import unittest

class test_Debian(unittest.TestCase):

    def setUp(self):
        self.debian = Debian()

    def test_get_update_os_script_lines(self):

        lines = self.debian.get_update_os_script_lines()

        expected_line0 = "apt-get -y update --fix-missing"
        expected_line1 = "apt-get upgrade -y"
        expected_line2 = "apt-get --no-install-recommends install -y apt-utils"
        expected_line3 = "rm -rf /var/lib/apt/lists/*"

        self.assertEqual(expected_line0, lines[0])
        self.assertEqual(expected_line1, lines[1])
        self.assertEqual(expected_line2, lines[2])
        self.assertEqual(expected_line3, lines[3])

    def test_get_update_os_script(self):

        expected_script = '''apt-get -y update --fix-missing
apt-get upgrade -y
apt-get --no-install-recommends install -y apt-utils
rm -rf /var/lib/apt/lists/*'''

        returned_string = self.debian.get_update_os_script()

        self.assertEqual(expected_script, returned_string)

