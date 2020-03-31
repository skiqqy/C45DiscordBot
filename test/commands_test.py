from src.bot_commands import *
import unittest


class TestCommands(unittest.TestCase):

    def test_brink(self):
        self.assertEqual(exec_command("brink"), "EXACTLY - Old Khaki.com")


if __name__ == '__main__':
    unittest.main()
