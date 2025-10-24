class WordReverser:
    """
    A class to store a string and provide a method to reverse it word by word.

    It demonstrates encapsulation by storing the original text in a protected
    attribute and uses special methods for initialization and representation.
    """

    def __init__(self, text: str):
        """
        Initializes the WordReverser with the input text.

        :param text: The string to be reversed word by word.
        """
        # Encapsulation: Storing the original text in a protected attribute
        # (indicated by a single leading underscore).
        self._original_text = text

    def reverse_words(self) -> str:
        """
        Reverses the order of words in the stored string.

        Example: "Hello world Python" -> "Python world Hello"

        :return: The string with the words reversed.
        """
        # 1. Split the string into a list of words using whitespace as a delimiter.
        words = self._original_text.split()

        # 2. Reverse the order of the words in the list.
        # Python's slicing provides a concise way to reverse a list: [::-1]
        reversed_words = words[::-1]

        # 3. Join the words back into a single string, separated by a space.
        reversed_string = " ".join(reversed_words)

        return reversed_string

    def get_original_text(self) -> str:
        """
        Public method to safely access the original text (getter).
        """
        return self._original_text

    # --- Special/Magic Methods ---

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the object.
        """
        return f"WordReverser(Original='{self._original_text}')"

    def __repr__(self) -> str:
        """
        Returns an official string representation, typically for debugging.
        """
        return f"WordReverser(text='{self._original_text}')"

# --- Example Usage ---
if __name__ == "__main__":
    # Test Case 1
    sentence1 = "The quick brown fox jumps over the lazy dog"
    reverser1 = WordReverser(sentence1)

    print(f"Original String 1 (using __str__): {reverser1}")
    reversed1 = reverser1.reverse_words()
    print(f"Reversed String 1: {reversed1}")
    print("-" * 30)

    # Test Case 2 (handling leading/trailing/multiple spaces - split() handles this well)
    sentence2 = "  Python is fun and powerful  "
    reverser2 = WordReverser(sentence2)

    print(f"Original String 2 (using getter): {reverser2.get_original_text()}")
    reversed2 = reverser2.reverse_words()
    print(f"Reversed String 2: {reversed2}")
    print("-" * 30)

    # Test Case 3 (empty string)
    sentence3 = ""
    reverser3 = WordReverser(sentence3)

    print(f"Original String 3: {reverser3.get_original_text()}")
    reversed3 = reverser3.reverse_words()
    print(f"Reversed String 3: '{reversed3}'")
    print("-" * 30)

    # Test Case 4 (one word)
    sentence4 = "Programming"
    reverser4 = WordReverser(sentence4)
    print(f"Original String 4: {reverser4.get_original_text()}")
    reversed4 = reverser4.reverse_words()
    print(f"Reversed String 4: {reversed4}")
