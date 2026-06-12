from datetime import datetime

HISTORY_FILE = "history.txt"


def save_history(original, suggestions):

    with open(
        HISTORY_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write("\n")
        file.write("=" * 50 + "\n")

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        file.write(f"Time : {timestamp}\n")
        file.write(f"Word : {original}\n")

        if suggestions:

            file.write("Suggestions:\n")

            for suggestion in suggestions:
                file.write(
                    f"-> {suggestion}\n"
                )

        else:

            file.write(
                "No suggestions available.\n"
            )

        file.write("=" * 50 + "\n")


def show_history():

    try:

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = file.read()

            if data.strip():

                print(data)

            else:

                print(
                    "History is empty."
                )

    except FileNotFoundError:

        print(
            "History file not found."
        )

    except OSError:

        print(
            "Unable to read history."
        )


def clear_history():

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ):
        pass

    print(
        "History cleared successfully."
    )