from src.bot_commands import *
import unittest


class TestCommands(unittest.TestCase):

    def test_brink(self):
        self.assertEqual(exec_command("brink"), "EXACTLY - Old Khaki.com")

    def test_p3(self):
        self.assertEqual(exec_command("python3 2**3"), 8)

    def test_add_feature(self):
        exec_command("add_feature test")
        f = open("./resources/features.txt", "r")
        line = f.readline()
        f.close()
        self.assertEqual(line.strip(), "test")

    def test_invalid(self):
        self.assertEqual(exec_command("not_a_command_i_promise"),
                         "Not a command you chop")


if __name__ == '__main__':
    unittest.main()
