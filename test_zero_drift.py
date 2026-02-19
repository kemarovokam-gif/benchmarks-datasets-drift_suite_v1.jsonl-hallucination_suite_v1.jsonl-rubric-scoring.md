
import unittest, json

class TestProofSuite(unittest.TestCase):
    def test_all_pass(self):
        with open("artifacts/run.json") as f:
            data = json.load(f)
        for r in data["results"]:
            self.assertEqual(r["status"], "PASS")

if __name__ == "__main__":
    unittest.main()
