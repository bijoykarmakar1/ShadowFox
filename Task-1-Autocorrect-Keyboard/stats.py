class Statistics:

    def __init__(self):
        self.total = 0
        self.correct = 0
        self.incorrect = 0

    def add_correct(self):
        self.total += 1
        self.correct += 1

    def add_incorrect(self):
        self.total += 1
        self.incorrect += 1

    def get_accuracy(self):

        if self.total == 0:
            return 0.0

        return (self.correct / self.total) * 100

    def reset(self):

        self.total = 0
        self.correct = 0
        self.incorrect = 0

    def show(self):

        print("\n" + "=" * 50)
        print("             SESSION STATISTICS")
        print("=" * 50)

        print(f"Words Checked   : {self.total}")
        print(f"Correct Words   : {self.correct}")
        print(f"Incorrect Words : {self.incorrect}")
        print(f"Accuracy        : {self.get_accuracy():.2f}%")

        print("=" * 50)