# undo.py
# Author: Austin Hilderbrand
#
# This is one possible solution to the problem.

class Text():
    """This represents a text document with the following options:
            1. display_text()
            2. add_text(input_text)
            3. undo()"""

    def __init__(self, starting_text = ""):
        """Initialize a new text document. The document can be initialized
        with or without starting text."""

        self.text = [] 
        if starting_text != "":
            self.text.append(str(starting_text))


    def display_text(self):
        """Display the text in the document in a user-friendly format."""
        
        if len(self.text) >= 1:
            for text_element in self.text:
                print(text_element, end = " ")
            print("\n") # We want a newline here.
        else:
            print("The text document is empty.\n")


    def add_text(self, text_input):
        """Add text to the document. Anything passed to this method will be
        converted to a string and appended directly to the document as-is, 
        with no extra punctuation or spacing."""

        self.text.append(str(text_input))


    def undo(self):
        """Undo the most recent text addition to the document. If the document
        is empty, tell the user. Let the user review the text about to be undone
        and opt out."""

        if len(self.text) >= 1:
            if "y" in input(f"Are you sure you want to undo: add '{self.text[len(self.text) - 1]}' (y/n)? ").lower():
                self.text.pop()
            else: 
                print("'undo' operation cancelled.\n")
        else:
            print("'undo' operation failed: the text document is empty.\n")


def test_runner():
    txt_doc = Text()
    txt_doc.display_text() # Empty
    txt_doc.undo() # "'undo' operation failed"
    txt_doc.add_text("Stacks are awesome!")
    txt_doc.display_text() # "Stacks are awesome! "
    txt_doc.add_text("They are really useful.")
    txt_doc.add_text("They are easy to learn.")
    txt_doc.display_text() # "Stacks are awesome! They are really useful. They are easy to learn."
    txt_doc.undo()
    txt_doc.display_text() # "Stacks are awesome! They are really useful. "
    txt_doc.undo()
    txt_doc.display_text() # "Stacks are awesome!  "

if __name__ == "__main__":
    test_runner()