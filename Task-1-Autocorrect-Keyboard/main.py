from autocorrect import AutoCorrect
from predictor import NextWordPredictor
from history import save_history, show_history, clear_history
from stats import Statistics
from utils import banner, menu


def main():

    checker = AutoCorrect()
    predictor = NextWordPredictor()
    stats = Statistics()

    while True:

        banner()
        menu()

        choice = input("\nEnter your choice: ").strip()

        # Spell Checker
        if choice == "1":

            word = input("\nEnter word: ").lower().strip()

            status, suggestions = checker.check_word(word)

            if status == "invalid":

                print("\n❌ Invalid input. Please enter alphabets only.")

            elif status == "correct":

                print("\n✅ Correct spelling.")
                stats.add_correct()

            else:

                print("\n❌ Incorrect spelling.")
                stats.add_incorrect()

                if suggestions:

                    print("\nSuggestions:\n")

                    for i, suggestion in enumerate(suggestions, start=1):
                        print(f"{i}. {suggestion}")

                else:

                    print("\nNo suggestions found.")

                save_history(word, suggestions)

        # Next Word Prediction
        elif choice == "2":

            sentence = input(
                "\nEnter previous word(s): "
            ).lower().strip()

            predictions = predictor.predict(sentence)

            print()

            if predictions:

                print("Predicted next words:\n")

                for i, prediction in enumerate(predictions, start=1):
                    print(f"{i}. {prediction}")

            else:

                print("No predictions available.")

        # View History
        elif choice == "3":

            show_history()

        # Session Statistics
        elif choice == "4":

            stats.show()

        # Clear History
        elif choice == "5":

            clear_history()

        # Exit
        elif choice == "6":

            print("\nThank you for using ShadowFox Autocorrect System!")
            break

        else:

            print("\n❌ Invalid choice. Please select between 1 and 6.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()