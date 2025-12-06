import string
import re
from collections import Counter
import os

JOURNAL_FILE = 'journal_entries.txt'
REPORT_FILE = 'journal_report.html'

def save_entry_to_file(entry_text: str):
    """Appends a new journal entry to a text file."""
    # Use 'a' mode to append to the file. Creates file if it doesn't exist.
    with open(JOURNAL_FILE, 'a') as f:
        f.write(entry_text + "\n---\n") # Add a separator between entries
    print(f"Entry successfully saved to {JOURNAL_FILE}")

def analyze_and_generate_html():
    """Reads all entries, counts word frequency, and generates an HTML report."""
    if not os.path.exists(JOURNAL_FILE):
        print("No journal entries found to analyze.")
        return

    with open(JOURNAL_FILE, 'r') as f:
        all_text = f.read()

    # Clean and normalize text for analysis
    # Remove punctuation, convert to lowercase, split into words
    # Use regex to find all word characters
    words = re.findall(r'\b\w+\b', all_text.lower())
    
    # Filter out common stop words and single-letter words if desired
    stop_words = set(['the', 'is', 'and', 'a', 'to', 'of', 'in', 'it', 'was', 'i', 'had', 'my'])
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1]
    
    # Count word frequencies
    counts = Counter(filtered_words)
    top_words = counts.most_common(20) # Get the top 20 most common words

    generate_html_report(top_words)

def generate_html_report(top_words_data):
    """Generates a simple HTML file with the most used words."""
    html_content = f"""
    <html>
    <head>
        <title>Journal Buddy Word Report</title>
        <style>
            body {{ font-family: sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            .word-list {{ list-style-type: none; padding: 0; }}
            .word-list li {{ margin-bottom: 5px; background-color: #f4f4f4; padding: 5px; border-radius: 4px; }}
        </style>
    </head>
    <body>
        <h1>Your Top 20 Most Used Journal Words</h1>
        <ul class="word-list">
            {''.join(f'<li><strong>{word}</strong>: {count} occurrences</li>' for word, count in top_words_data)}
        </ul>
        <p>This report is based on all entries in `{JOURNAL_FILE}`.</p>
    </body>
    </html>
    """
    with open(REPORT_FILE, 'w') as f:
        f.write(html_content)
    
    print(f"HTML report generated: {REPORT_FILE}")

# Include the previous process_journal_entry function here if you are using it in app.py
def process_journal_entry(entry_text: str) -> str:
    """ (From previous step, ensure this is in src/journal.py) """
    if not isinstance(entry_text, str) or not entry_text.strip():
        return "Error: Entry cannot be empty."
    entry_text = entry_text.strip().lower()
    entry_text = entry_text.translate(str.maketrans('', '', string.punctuation))
    if len(entry_text.split()) < 3:
        return "Error: Entry must contain at least 3 words after cleanup."
    return f"Entry processed: '{entry_text[:50]}...'"



# def apply_journal_rule(user_mood_input: str, journal_now: bool) -> str:
#     # ... (paste the logic from the previous answer here) ...
#     normalized_mood = user_mood_input.strip().lower()

#     if normalized_mood == 'sad':
#         if not journal_now:
#             return "Okay, I understand. Your feelings are logged. Come back anytime you're ready to write."
#         else:
#             quote = "“The only way out of the labyrinth of suffering is to forgive.” – John Green"
#             prompt = "I hear you. Sometimes writing things down helps. What's weighing on you today?"
#             return f"{quote}\n\n{prompt}"
    
#     # ... (continue with happy and default cases) ...
#     if normalized_mood == 'happy':
#         if not journal_now:
#             return "No problem, your good vibes are logged! Feel free to come back when you have time."
#         else:
#             quote = "“The best way to cheer yourself is to try to cheer someone else up.” – Mark Twain"
#             prompt = "That's wonderful! What made you feel this way today?"
#             return f"{quote}\n\n{prompt}" 

#     if not journal_now:
#         return "Acknowledged. We'll be here later if you change your mind. Take care!"
#     else:
#         quote = "“Journaling is like whispering to your future self.” – Unknown"
#         prompt = "Thanks for checking in. What is your journaling goal for today?"
#         return f"{quote}\n\n{prompt}"