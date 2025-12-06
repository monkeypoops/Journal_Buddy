def apply_journal_rule(mood):
    """
    Applies a journal rule based on the user's mood.

    Args:
        mood (str): The user's current mood (e.g., 'great', 'bad', 'neutral').

    Returns:
        str: A message with the suggested journal rule.
    """

    bad_moods = ["bad", "sad", "mad", "pissed", "bla", "meh"]
    good_moods = ["great", "good", "okay", "not bad", "happy", "glad"]

    # Decision rules with a safe default
    if mood.lower() in good_moods:
        return "Write about your successes and what made you feel great today!"
    elif mood.lower() in bad_moods:
        return "Write down three things you are grateful for, even if it's tough."
    else:
        # Safe default rule for any other mood or no specified mood
        return "Jot down your thoughts, reflect on your day, and plan for tomorrow."