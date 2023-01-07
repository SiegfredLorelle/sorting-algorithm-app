import string
import sys

class sorting_algorithm_app:
    
    # Maps user input, used when checking user input
    input_keys = {
        "sort": {1: "selection", 2: "bubble", 3: "insertion", 4: "merge"},
        "type_of_elements": {1: "integer", 2: "letter"},
        "sort_mode": {1: "ascending", 2: "descending"},
    }

    def __init__(self):
        """ Start the app upon instaniating the app """
        print("\nSorting Algorithm Application")
        print("Programmed by: Siegfred Lorrelle C.")
        self.main_menu()

    def main_menu(self):
        """ Main Menu allows user to choose which sorting algorithm to use """
        print("\nMain Menu")
        print("\n[1] Selection Sorting")
        print("[2] Bubble Sorting")
        print("[3] Insertion Sorting")
        print("[4] Merge Sorting")

        # Asks user which sort to use, with input checks
        while True:
            try:
                sort_choice = int(input("\nWhich sort to use?  "))
                # If user input is not in input keys then it is invalid, ask again
                if sort_choice not in self.input_keys["sort"]:
                    print("Error: Accepted input are only 1, 2, 3 or 4! Try Again!")
                    continue
            # If user input is not an integer, then it is invalid, ask again
            except (TypeError, ValueError):
                print("Error: Accepted input are only 1, 2, 3 or 4! Try Again!")
                continue
            else:
                break

        # Ask the elements of the list to sort, and whether to sort it ascending or descending
        sort_mode, user_list = self.configure_list()
        # Sort the list and return a sorted list
        sorted_list = self.sort(sort_choice, sort_mode, user_list)
        print(f"Final Sorted List: {sorted_list}")

        # Ask user to try again or not, with input checks
        while True:
            try:
                user_reply = input("\nDo you want to try again? [y/n]:  ")
                if user_reply[0].lower() == "y":
                    return self.main_menu()
                elif user_reply[0].lower() == "n":
                    sys.exit("\nSorting Algorithm App is closing ...")
            except IndexError:
                continue

    def configure_list(self):
        """ Ask the elements of the list and whether to sort it ascending or descending """
        # Asks the number of elements of the list, with input checks
        while True:
            try:
                num_of_elements = int(input("\nHow many elements are there on your list?  "))
                # If number of elements is less than 0, then ask again
                if num_of_elements <= 0:
                    print("Error: Number of elements must be a positive integer! Try Again!")
                    continue
            # If number of element is not an integer,then ask again
            except (TypeError, ValueError):
                print("Error: Number of elements must be an integer! Try Again!")
                continue
            else:
                break

        # Ask the type of element whether it is integer or letter
        while True:
            try:
                type_of_elements = int(input("\nType of elements: [1] integer or [2] letter:  "))
                # If type of element is not in input keys, then it is invalid, ask again
                if type_of_elements not in self.input_keys["type_of_elements"]:
                    print("Error: Type of elements can only be 1 (int) or 2 (letters)! Try Again!")
                    continue
            # If type of element is not an integer, then ask again
            except (TypeError, ValueError):
                print("Error: Type of elements can only be 1 (int) or 2 (letters)! Try Again!")
                continue
            else:
                break

        # Ask the sort mode whether it is ascending or descending
        while True:
            try:
                sort_mode = int(input("\nSort mode: [1] ascending, [2] descending:  "))
                # If sort mode is not in input keys, then it is invalid, ask again
                if sort_mode not in self.input_keys["sort_mode"]:
                    print("Error: Sort Mode can only be 1 (ascending) or 2 (descending)! Try Again!")
                    continue
            # If type of element is not an integer, then ask again
            except (TypeError, ValueError):
                print("Error: Sort Mode can only be 1 (ascending) or 2 (descending)! Try Again!")
                continue
            else:
                break

        print()

        # Ask the elements of the list
        user_list = []

        for counter in range(num_of_elements):
            while True:
                try:
                    element = input(f"Enter your element[{counter + 1}]:  ").upper()
                    # If chosen type of elements is letter, then ensure given element is only ony letter, if not, then ask again
                    if self.input_keys["type_of_elements"][type_of_elements] == "letter":
                        if element not in string.ascii_uppercase:
                            print("Element with type letter must be a letter (A-Z)! Try Again!")
                            continue
                        elif len(element) != 1:
                            print("Element with type letters must only be 1 letter! Try Again!")
                            continue
                    # If chosen type of element is integer, then convert element to int
                    elif self.input_keys["type_of_elements"][type_of_elements] == "integer":
                        element = int(element)
                    user_list.append(element)
                # Catches errors if input is invalid, then ask again
                except (TypeError, ValueError):
                    print("Element with type integer must be an integer! Try Again!")
                    continue
                else:
                    break

        return sort_mode, user_list


    def sort(self, sort_choice, sort_mode, user_list):
        """ Determine which sort to use depending on sort choice """
        print(f"\nUnsorted List: {user_list}")

        if self.input_keys["sort"][sort_choice] == "selection":
            return self.selection_sort(sort_mode, user_list)
        elif self.input_keys["sort"][sort_choice] == "bubble":
            return self.bubble_sort(sort_mode, user_list)
        elif self.input_keys["sort"][sort_choice] == "insertion":
            return self.insertion_sort(sort_mode, user_list)
        elif self.input_keys["sort"][sort_choice] == "merge":
            return self.merge_sort(sort_mode, user_list)


    def selection_sort(self, sort_mode, user_list):
        """ Loop through the list, find the smallest/greatest, then swap it if necessary """
        for i in range(len(user_list) - 1):
            element_to_swap_index = i
            for j in range(i + 1, len(user_list)):
                if self.input_keys["sort_mode"][sort_mode] == "ascending" and user_list[element_to_swap_index] > user_list[j]:
                    element_to_swap_index = j
                elif self.input_keys["sort_mode"][sort_mode] == "descending" and user_list[element_to_swap_index] < user_list[j]:
                    element_to_swap_index = j
            user_list[i], user_list[element_to_swap_index] = user_list[element_to_swap_index], user_list[i]
            print(f"Pass {i+1}: {user_list}")

        return user_list

    def bubble_sort(self, sort_mode, user_list):
        """ Loop through the list, check if the next is element is greater/smaller, then swap it if necessary """
        for i in range(len(user_list) - 1):
            for j in range(0, len(user_list) - i - 1):
                if self.input_keys["sort_mode"][sort_mode] == "ascending" and user_list[j] > user_list[j+1]:
                    user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
                elif self.input_keys["sort_mode"][sort_mode] == "descending" and user_list[j] < user_list[j+1]:
                    user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
            print(f"Pass {i+1}: {user_list}")

        return user_list

    def insertion_sort(self, sort_mode, user_list):
        """ Loop through the list, place the next element to its correct position """
        for i in range(1, len(user_list)):
            j = i

            if self.input_keys["sort_mode"][sort_mode] == "ascending":
                while j > 0 and user_list[j] < user_list[j-1]:
                    user_list[j], user_list[j-1] = user_list[j-1], user_list[j]
                    j -= 1
            elif self.input_keys["sort_mode"][sort_mode] == "descending":
                while j > 0 and user_list[j] > user_list[j-1]:
                    user_list[j], user_list[j-1] = user_list[j-1], user_list[j]
                    j -= 1
            print(f"Pass: {i}: {user_list}")

        return user_list


    def merge_sort(self, sort_mode, user_list):
        """ Split the list into half recursively until one element is left, then merge them while sorting """
        # Stop splitting if one element is left
        if len(user_list) == 1:
            return user_list

        # Split the list into left and right in the center
        center_index = len(user_list) // 2
        left_sublist = user_list[:center_index]
        right_sublist = user_list[center_index:]

        # Inform user about the list
        print(f"split => left: {left_sublist} right: {right_sublist}")

        # Split the both halves again
        left = self.merge_sort(sort_mode, left_sublist)
        right = self.merge_sort(sort_mode, right_sublist)

        # After splitting, sort them by appending the left and right elements into merged list
        merged_list = []
        while True:
            # Stop merging if left and right list is empty
            if len(left) == 0 and len(right) == 0:
                break
            # If left list still have elements, and right list do not, then put all left elements to merged list
            elif len(left) != 0 and len(right) == 0:
                merged_list += left
                left.clear()
            # If right list still have elements, and left list do not, then put all right elements to merged list
            elif len(left) == 0 and len(right) != 0:
                merged_list += right
                right.clear()
            # If left and right still have elements, check their first element and append one of them to merged list, remove the added element to left/right list
            else:
                if self.input_keys["sort_mode"][sort_mode] == "ascending":
                    if left[0] < right[0]:
                        merged_list.append(left[0])
                        left.pop(0)
                    else:
                        merged_list.append(right[0])
                        right.pop(0)
                elif self.input_keys["sort_mode"][sort_mode] == "descending":
                    if left[0] > right[0]:
                        merged_list.append(left[0])
                        left.pop(0)
                    else:
                        merged_list.append(right[0])
                        right.pop(0)

        # Inform user about the sorted merged list
        print(f"merge => {merged_list}")
        return merged_list


if __name__ == "__main__":
    app = sorting_algorithm_app()