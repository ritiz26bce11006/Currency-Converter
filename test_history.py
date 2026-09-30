import os
import unittest
import history_manager


class TestHistory(unittest.TestCase):

    def setUp(self):
        # use a separate file so the real history is not touched
        history_manager.HISTORY_FILE = "test_history.json"
        history_manager.save_history([])

    def tearDown(self):
        if os.path.exists("test_history.json"):
            os.remove("test_history.json")

    def test_add_record(self):
        history_manager.add_record("USD", "INR", 10, 830.0)
        history = history_manager.load_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["from"], "USD")
        self.assertEqual(history[0]["result"], 830.0)

    def test_clear_history(self):
        history_manager.add_record("USD", "INR", 10, 830.0)
        history_manager.clear_history()
        self.assertEqual(history_manager.load_history(), [])

    def test_missing_file_returns_empty(self):
        os.remove("test_history.json")
        self.assertEqual(history_manager.load_history(), [])

    def test_max_history_limit(self):
        for i in range(history_manager.MAX_HISTORY + 5):
            history_manager.add_record("USD", "EUR", i, i * 0.9)
        history = history_manager.load_history()
        self.assertEqual(len(history), history_manager.MAX_HISTORY)


if __name__ == "__main__":
    unittest.main()
