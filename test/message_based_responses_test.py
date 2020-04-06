import unittest
from __init__ import ignore_resource_warnings
from message_based_responses import _match_word, regex_based_response


class TestRegexBasedMatches(unittest.TestCase):

    def test_matcher(self):
        self.assertIsNotNone(_match_word("papi", "here is papi !"))
        self.assertIsNotNone(_match_word("papi", "where is papi?"))
        self.assertIsNotNone(_match_word("papi", "papi"))
        self.assertIsNone(_match_word("papi", "papisdasd"))

    def test_test(self):
        response = regex_based_response("test")
        self.assertEqual(response, ["Marks out", "?"])

    def test_papi(self):
        response = regex_based_response("papi").pop()
        flag1 = "UWU DID SOMEBODY SAY P A P I" == response
        flag2 = "Yas daddi 🤪" == response
        flag3 = "Big P A P I Dave 😍" == response
        self.assertTrue(flag1 | flag2 | flag3)

    @ignore_resource_warnings
    def test_triggered(self):
        response = regex_based_response("triggered").pop()
        with open("./resources/triggered.lol", "r") as fl:
            msgs = fl.readlines()
            flags = [msg == response for msg in msgs]
            if True not in flags:
                self.fail()

    @ignore_resource_warnings
    def test_vim(self):
        response = regex_based_response("vim").pop()
        with open("./resources/vim.txt", "r") as fl:
            msg = fl.readline()
            self.assertEqual(msg, response)

    def test_eclipse(self):
        response = regex_based_response("eclipse").pop()
        self.assertEqual(response, "eclipse kaka, IDE's kaka")


if __name__ == '__main__':
    unittest.main()
