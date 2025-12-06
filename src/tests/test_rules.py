import unittest
# Import the function from your journal.py file
from journal import apply_journal_rule 

class TestJournalRules(unittest.TestCase):

    # You can reuse the tests from the previous example, just modify 
    # the function call to match 'apply_journal_rule'

    def test_happy_now_rule(self):
        """Test Rule 1: Happy mood and ready to journal immediately."""
        response = apply_journal_rule("Happy", True)
        self.assertIn("Mark Twain", response)
        self.assertIn("What made you feel this way", response)

    def test_sad_reschedule_rule(self):
        """Test Rule 4: Sad mood but wants to reschedule (comforting exit)."""
        response = apply_journal_rule("sad", False)
        self.assertIn("Your feelings are logged", response)
        self.assertNotIn("What's weighing on you?", response) # Ensure no prompt

    def test_neutral_default_rule(self):
        """Test Rule 6/Default: Neutral mood and wants to reschedule."""
        # This test covers the default branch of the logic
        response = apply_journal_rule("Just okay", False)
        self.assertIn("We'll be here later", response)
        self.assertNotIn("What is your journaling goal", response)


if __name__ == '__main__':
    # This ensures the tests run when the script is executed directly
    unittest.main()
