# wildlife_survey.py
# Author: Austin Hilderbrand
#
# This is one possible solution to the problem. Note that 
# much of the error handling has been left incomplete. 
# See if you can make this program more robust while also 
# reinforcing your understanding of sets in Python. 

#
# List declarations
#
mammals_seen = set()
birds_seen = set()
fish_seen = set()
reptiles_seen = set()
amphibians_seen = set()

all_seen = set()

#
# Function definitions
#

def get_option():
    """Prompt the user for the option.
    THIS MUST BE AN INTEGER FROM 1-4."""

    return int(input("Select one of the following:\n"
    "\t(1) Make entry\n"
    "\t(2) Remove entry\n"
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


def get_set_name(input_class):
    """From the wildlife class name, return the appropriate set."""

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
        set_name = get_set_name(input_class)
        input_species = get_species()

        if input_species in set_name:
            print("Species already seen. Not added.")
        else:
            set_name.add(input_species)

    # OPTION 2: Remove entry
    elif option == 2:
        input_class = get_class()
        set_name = get_set_name(input_class)

        if len(set_name) >= 1:
            input_species = get_species()
            set_name.remove(input_species)
            print(f"'{input_species}' has been removed.")
        else:
            print("ERROR: can't remove from an empty set.")

    # OPTION 3: View entries by class
    elif option == 3:
        input_class = get_class()
        set_name = get_set_name(input_class)

        print(set_name)

    # OPTION 4: View all entries
    elif option == 4:
        for species in mammals_seen:
            if species not in all_seen:
                all_seen.add(species)
        for species in birds_seen:
            if species not in all_seen:
                all_seen.add(species)
        for species in fish_seen:
            if species not in all_seen:
                all_seen.add(species)
        for species in reptiles_seen:
            if species not in all_seen:
                all_seen.add(species)
        for species in amphibians_seen:
            if species not in all_seen:
                all_seen.add(species)

        print(all_seen)

    # INVALID OPTION
    else:
        print("ERROR: invalid option")