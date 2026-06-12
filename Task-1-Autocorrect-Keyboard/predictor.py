import nltk
from nltk.corpus import gutenberg
from collections import defaultdict, Counter

nltk.download("gutenberg", quiet=True)


class NextWordPredictor:

    def __init__(self):

        self.bigram = defaultdict(Counter)
        self.trigram = defaultdict(Counter)

        self.default_predictions = [
            "the",
            "is",
            "and",
            "to",
            "you"
        ]

        training = []

        custom_sentences = [

            "hello how are you",
            "hello my friend",
            "hello everyone",
            "hello there",
            "hello beautiful people",
            "hello beautiful world",
            "good morning everyone",
            "good afternoon everyone",
            "good evening everyone",
            "good night everyone",

            "how are you",
            "how are you doing",
            "how are you today",
            "how is your day",
            "how is everything",
            "how can i help you",
            "how may i help you",

            "i am fine",
            "i am good",
            "i am happy",
            "i am learning python",
            "i am working",
            "i am studying",
            "i am excited",

            "i love machine learning",
            "i love artificial intelligence",
            "i love programming",
            "i love coding",
            "i love python",

            "thank you",
            "thank you very much",
            "thank you for helping",
            "thank you for your support",

            "can you help me",
            "could you help me",
            "please help me",

            "what are you doing",
            "where are you going",
            "who are you",
            "why are you here",

            "nice to meet you",
            "nice to see you",

            "have a nice day",
            "have a safe journey",

            "see you soon",
            "see you tomorrow",

            "welcome to shadowfox",
            "welcome to our project",

            "machine learning is powerful",
            "machine learning is interesting",

            "artificial intelligence is amazing",
            "artificial intelligence is the future",

            "deep learning is interesting",

            "python is easy",
            "python is easy to learn",

            "data science is fun",

            "good luck",
            "best wishes",
            "take care",
            "take care of yourself",

            "wish you all the best",
            "all the best",

            "beautiful day",
            "beautiful morning",
            "beautiful evening",
            "beautiful place",
            "beautiful world",

            "happy birthday",
            "happy anniversary",

            "good job",
            "great work",
            "excellent work",
            "well done"
        ]

        # Weight custom data heavily

        for _ in range(100):
            for sentence in custom_sentences:
                training.extend(sentence.lower().split())

        # Gutenberg corpus

        for fileid in gutenberg.fileids():

            for word in gutenberg.words(fileid):

                if word.isalpha():
                    training.append(word.lower())

        # Bigram

        for i in range(len(training)-1):

            self.bigram[
                training[i]
            ][
                training[i+1]
            ] += 1

        # Trigram

        for i in range(len(training)-2):

            key = (
                training[i],
                training[i+1]
            )

            self.trigram[
                key
            ][
                training[i+2]
            ] += 1

    def predict(self, sentence):

        sentence = sentence.lower().strip()

        if not sentence:
            return self.default_predictions

        words = sentence.split()

        # Trigram

        if len(words) >= 2:

            key = (
                words[-2],
                words[-1]
            )

            if key in self.trigram:

                result = [
                    w for w, c
                    in self.trigram[key].most_common(5)
                ]

                if result:
                    return result

        # Bigram

        last = words[-1]

        if last in self.bigram:

            result = [
                w for w, c
                in self.bigram[last].most_common(5)
            ]

            if result:
                return result

        # Partial matching

        partial = []

        for key in self.bigram:

            if key.startswith(last):

                partial.extend(
                    [
                        w for w, c
                        in self.bigram[key].most_common(2)
                    ]
                )

        if partial:

            unique = []

            for word in partial:

                if word not in unique:
                    unique.append(word)

            return unique[:5]

        # Final fallback

        return self.default_predictions