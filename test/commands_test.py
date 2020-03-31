from src.bot_commands import *
import unittest


class TestCommands(unittest.TestCase):

    def test_brink(self):
        self.assertEqual(exec_command("brink"), "EXACTLY - Old Khaki.com")

    def test_p3(self):
        self.assertEqual(exec_command("python3 2**3"), 8)


if __name__ == '__main__':
    unittest.main()
