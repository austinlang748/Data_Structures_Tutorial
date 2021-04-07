# wildlife_survey_with_tree.py
# Author: Austin Hilderbrand
#
# This is one possible solution to the problem. Note that 
# much of the error handling has been left incomplete. 
# See if you can make this program more robust while also 
# reinforcing your understanding of trees in Python. 
#
# As an added challenge, see if you can inplement the remove() feature. 
# This will enable the user to select OPTION (2) Remove entry.
# All the code needed in the main program code is there. The appropriate
# function definitions in the BST class are missing, though. 

################################################
# Define the BST class.
#
# This will be our data structure template.
################################################

class BST:
    """Represents the binary search tree"""

    class Node:
        """Represents a node in the BST."""

        def __init__(self, data):
            """Initialize the node with the data passed to it and None type pointers."""
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """Initialize the BST by assigning its root to None type."""

        self.root = None

    def insert(self, data):
        """
        Inserts a node containing the value into the BST. If the BST has no root 
        (is empty), then the new node is assigned to be the root."""

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        Called for the first time by insert(). This is a recursive function
        which looks for a place to insert a value into the BST, and inserts
        it when an available location is found."""

        ###########################
        # Left side
        ###########################
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None: # <-------------------- BASE CASE
                # We found an empty spot
                node.left = BST.Node(data)
            else:                 # <-------------------- RECURSIVE PART
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        
        ###########################
        # Right side
        ###########################       
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __contains__(self, data):
        """Supports use of the 'in' keyword.
        Checks if a value is in the BST."""

        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        Called for the first time by __contains__(), when the 'in' keyword is used.
        This is a recursive function which returns True if the data in the current 
        node matches the search value."""

        if node is not None:

            # Base case
            if data == node.data:
                return True

            # Recursive part:
            return self._contains(data, node.left) # Check left subtree
            return self._contains(data, node.right) # Check right subtree

    def __iter__(self):
        """
        Supports the use of the BST class with loops. Allows the user to
        iterate through every node and view its data."""
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Called for the first time by __iter__(). This is a recursive function 
        which yields the data from each child node."""
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


################################################
# Main program code.
#
# This is almost identical to the code in 
# wildlife_survey.py, but it uses the tree 
# structure instead of the set. 
################################################

#
# List declarations
#
mammals_seen = BST()
birds_seen = BST()
fish_seen = BST()
reptiles_seen = BST()
amphibians_seen = BST()

all_seen = BST()

#
# Function definitions
#

def get_option():
    """Prompt the user for the option.
    THIS MUST BE AN INTEGER FROM 1-4."""

    return int(input("Select one of the following:\n"
    "\t(1) Make entry\n"
    "\t(2) Remove entry (don't select - in progress)\n"
    "\t(3) View entries by class\n"
    "\t(4) View all entries\n"
    "> "))


def get_class():
    """Prompt the user for the wildlife class name.
    THIS MUST BE A VALID STRING."""

    return input("Enter one of the following: \n"
    "\t'mammal'\n"
    "\t'bird'\n"
    "\t'fish'\n"
    "\t'reptile'\n"
    "\t'amphibian'\n"
    "> ").lower()


def get_species():
    """Prompt the user for the species name."""

    return input("Enter species name: ").lower()


def get_tree_name(input_class):
    """From the wildlife class name, return the appropriate tree."""

    if input_class == "mammal":
        return mammals_seen
    elif input_class == "bird":
        return birds_seen
    elif input_class == "fish":
        return fish_seen
    elif input_class == "reptile":
        return reptiles_seen
    elif input_class == "amphibian":
        return amphibians_seen


########################################################################
# Main control loop
#
# This will repeat until the program is terminated.
########################################################################
while True:
    option = get_option() # Prompt the user for the option.

    # OPTION 1: Make entry
    if option == 1:
        input_class = get_class()
        tree_name = get_tree_name(input_class)
        input_species = get_species()

        if input_species in tree_name:
            print("Species already seen. Not added.")
        else:
            tree_name.insert(input_species)

    # OPTION 2: Remove entry
    # TODO: Make this work.
    #       This will require the creation of remove() and _remove() methods in BST.
    # elif option == 2:
    #     input_class = get_class()
    #     tree_name = get_tree_name(input_class)

    #     if len(tree_name) >= 1:
    #         input_species = get_species()
    #         tree_name.remove(input_species)
    #         # Remember to remove the species name from all_seen if it's already there
    #         if input_species in all_seen:
    #             all_seen.remove(input_species)
    #         print(f"'{input_species}' has been removed.")
    #     else:
    #         print("ERROR: can't remove from an empty tree.")

    # OPTION 3: View entries by class
    elif option == 3:
        input_class = get_class()
        tree_name = get_tree_name(input_class)

        for species_name in tree_name:
            print(f"'{species_name}'", end = " ")
        print("\n") # We want a newline here

    # OPTION 4: View all entries
    elif option == 4:
        for species in mammals_seen:
            if species not in all_seen:
                all_seen.insert(species)
        for species in birds_seen:
            if species not in all_seen:
                all_seen.insert(species)
        for species in fish_seen:
            if species not in all_seen:
                all_seen.insert(species)
        for species in reptiles_seen:
            if species not in all_seen:
                all_seen.insert(species)
        for species in amphibians_seen:
            if species not in all_seen:
                all_seen.insert(species)

        for species_name in tree_name:
            print(f"'{species_name}'", end = " ")
        print("\n") # We want a newline here

    # INVALID OPTION
    else:
        print("ERROR: invalid option")