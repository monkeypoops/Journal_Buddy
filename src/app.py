import argparse
# Use a relative import if rules.py is in the same directory/package level
from rules import apply_journal_rule 

def main():
    """ 
    Main function for the Journal Buddy. 
    Handles command-line arguments using argparse.
    """ 
    user_name = input("What is your name? ")

    print(f"Hello, {user_name}! Welcome to your Personal Journal Buddy.")

    mood = input("How are you feeling today? ")
    
    parser = argparse.ArgumentParser(
        description="A Journal Buddy chatbot CLI that provides quotes and prompts based on your mood.",
        epilog="Example: python app.py --mood happy --now"
    )
    parser.add_argument(
        '-m', '--mood', 
        type=str, 
        default='neutral', 
        help="Specify your current mood (e.g., 'happy', 'sad', 'neutral'). Defaults to 'neutral'."
    )
    parser.add_argument(
        '--now', 
        action='store_true', # This makes it a boolean flag. If present, it's True.
        help="Add this flag if you want to journal right now (True/False behavior)."
    )

    # 3. Parse the arguments from the command line
    args = parser.parse_args()

    # Pass both the mood string and the boolean flag to your function
    rule_message = apply_journal_rule(mood)
    
    print("\n--- Bot Response ---")
    print(rule_message)
    print("--------------------")

if __name__ == "__main__":
    main()
