import string

class sorting_algorithm_app:
    
    input_keys = {
        "sort": {1: "selection", 2: "bubble", 3: "insertion", 4: "merge"},
        "type_of_elements": {1: "integer", 2: "letter"},
        "sort_mode": {1: "ascending", 2: "descending"},
    }

    def __init__(self):
        print("Sorting Algorithm Application")
        print("Programmed by: Siegfred Lorrelle C.")
        self.main_menu()

    def main_menu(self):
        print("\nMain Menu")
        print("\n[1] Selection Sorting")
        print("[2] Bubble Sorting")
        print("[3] Insertion Sorting")
        print("[4] Merge Sorting")

        while True:
            try:
                sort_choice = int(input("\nWhich sort to use?  "))
                if sort_choice not in self.input_keys["sort"]:
                    print("Error: Accepted input are only 1, 2, 3 or 4! Try Again!")
                    continue
            except (TypeError, ValueError):
                print("Error: Accepted input are only 1, 2, 3 or 4! Try Again!")
                continue
            else:
                break

        list_info = self.configure_list()
        sorted_list = self.sort(sort_choice, list_info)
        print(f"Final Sorted List: {sorted_list}")


    def configure_list(self):
        while True:
            try:
                num_of_elements = int(input("\nHow many elements are there on your list?  "))
                if num_of_elements <= 0:
                    print("Error: Number of elements must be a positive integer! Try Again!")
                    continue
            except (TypeError, ValueError):
                print("Error: Number of elements must be an integer! Try Again!")
                continue
            else:
                break

        while True:
            try:
                type_of_elements = int(input("\nType of elements: [1] integer or [2] letter:  "))
                if type_of_elements not in self.input_keys["type_of_elements"]:
                    print("Error: Type of elements can only be 1 (int) or 2 (letters)! Try Again!")
                    continue
            except (TypeError, ValueError):
                print("Error: Type of elements can only be 1 (int) or 2 (letters)! Try Again!")
                continue
            else:
                break

        while True:
            try:
                sort_mode = int(input("\nSort mode: [1] ascending, [2] descending:  "))
                if sort_mode not in self.input_keys["sort_mode"]:
                    print("Error: Sort Mode can only be 1 (ascending) or 2 (descending)! Try Again!")
                    continue
            except (TypeError, ValueError):
                print("Error: Sort Mode can only be 1 (ascending) or 2 (descending)! Try Again!")
                continue
            else:
                break

        print()
        
        user_list = []
        for counter in range(num_of_elements):
            while True:
                try:
                    element = input(f"Enter your element[{counter + 1}]:  ").upper()

                    if self.input_keys["type_of_elements"][type_of_elements] == "letter":
                        if element not in string.ascii_uppercase:
                            print("Element with type letter must be a letter (A-Z)! Try Again!")
                            continue
                        elif len(element) != 1:
                            print("Element with type letters must only be 1 letter! Try Again!")
                            continue
                        element = ord(element)
                    elif self.input_keys["type_of_elements"][type_of_elements] == "integer":
                        element = int(element)
                    user_list.append(element)
                except (TypeError, ValueError):
                    print("Element with type integer must be an integer! Try Again!")
                    continue
                else:
                    break

        return {"num of elements": num_of_elements,
                 "type of elements": type_of_elements,
                 "sort mode": sort_mode,
                 "list": user_list}


    def sort(self, sort_choice, list_info):
        if sort_choice == "1":
            return self.selection_sort(list_info)
        elif sort_choice == "2":
            return self.bubble_sort(list_info)
        elif sort_choice == "3":
            return self.insertion_sort(list_info)
        elif sort_choice == "4":
            return self.merge_sort(list_info)

    def selection_sort(self, list_info):
        print()


app = sorting_algorithm_app()


# TODO
# SORT ITSELF