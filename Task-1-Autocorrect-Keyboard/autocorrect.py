import nltk
from nltk.corpus import words
from spellchecker import SpellChecker
from difflib import get_close_matches

try:
    words.words()
except:
    nltk.download("words", quiet=True)

spell = SpellChecker()

COMMON_WORDS = {

    "hello","hi","hey","good","morning","afternoon",
    "evening","night","thanks","thank","please",
    "welcome","sorry","beautiful","happy","birthday",
    "python","java","cpp","javascript",
    "machine","learning","deep","artificial",
    "intelligence","shadowfox","internship",
    "project","computer","coding","programming",
    "friend","world","today","tomorrow"

}

NLTK_DICT = set(w.lower() for w in words.words())

FULL_DICT = COMMON_WORDS | NLTK_DICT


class AutoCorrect:

    def __init__(self):

        self.common = COMMON_WORDS
        self.dictionary = FULL_DICT

    def check_word(self, word):

        word = word.lower().strip()

        if not word.isalpha():
            return "invalid", []

        if word in self.dictionary:
            return "correct", []

        suggestions = []

        # SpellChecker best guess

        best = spell.correction(word)

        if best:
            suggestions.append(best)

        # SpellChecker candidates

        try:
            for w in spell.candidates(word):
                suggestions.append(w)
        except:
            pass

        # Common words

        suggestions.extend(
            get_close_matches(
                word,
                list(self.common),
                n=5,
                cutoff=0.5
            )
        )

        # NLTK backup

        suggestions.extend(
            get_close_matches(
                word,
                list(self.dictionary),
                n=5,
                cutoff=0.8
            )
        )

        # Prefix

        for w in self.common:
            if len(word) >= 2:
                if w.startswith(word[:2]):
                    suggestions.append(w)

        # Remove duplicates

        unique = []

        for s in suggestions:

            if s not in unique:
                unique.append(s)

        # Priority words

        priority = [

            "hello",
            "good",
            "thanks",
            "thank",
            "beautiful",
            "happy",
            "python",
            "machine",
            "learning",
            "shadowfox",
            "internship"

        ]

        final = []

        for p in priority:
            if p in unique:
                final.append(p)

        for s in unique:
            if s not in final:
                final.append(s)

        return "incorrect", final[:5]