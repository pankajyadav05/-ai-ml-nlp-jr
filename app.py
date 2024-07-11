import nltk
from nltk.corpus import words

nltk.download('words')


def load_words():
    return set(word.lower() for word in words.words() if len(word) > 2)


def play_word_chain_game():
    valid_words = load_words()
    used_words = set()

    print("Welcome to the Word Chain Game!")
    print("Enter a word, and I'll respond with a word that starts with the last letter of your word.")
    print("Type 'quit' to end the game.")


if __name__ == "__main__":
    play_word_chain_game()
