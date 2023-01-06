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

        sort_mode, user_list = self.configure_list()
        sorted_list = self.sort(sort_choice, sort_mode, user_list)
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
                        # element = ord(element)
                    elif self.input_keys["type_of_elements"][type_of_elements] == "integer":
                        element = int(element)
                    user_list.append(element)
                except (TypeError, ValueError):
                    print("Element with type integer must be an integer! Try Again!")
                    continue
                else:
                    break

        return sort_mode, user_list


    def sort(self, sort_choice, sort_mode, user_list):
        print(f"\nUnsorted List: {user_list}")
        if self.input_keys["sort"][sort_choice] == "selection":
            return self.selection_sort(sort_mode, user_list)
        elif self.input_keys["sort"][sort_choice] == "bubble":
            return self.bubble_sort(sort_mode, user_list)
        elif self.input_keys["sort"][sort_choice] == "insertion":
            return self.insertion_sort(sort_mode, user_list)
        elif self.input_keys["sort"][sort_choice] == "merge":
            return self.merge_sort(sort_mode, user_list)
        else:
            print("ERROR")

    def selection_sort(self, sort_mode, user_list):

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
        
        for i in range(len(user_list) - 1):
            for j in range(0, len(user_list) - i - 1):
                if self.input_keys["sort_mode"][sort_mode] == "ascending" and user_list[j] > user_list[j+1]:
                    user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
                elif self.input_keys["sort_mode"][sort_mode] == "descending" and user_list[j] < user_list[j+1]:
                    user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
            print(f"Pass {i+1}: {user_list}")
        
        return user_list
    
    def insertion_sort(self, sort_mode, user_list):
        
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
        
        if len(user_list) == 1:
            return user_list

        center_index = len(user_list) // 2
        left_sublist = user_list[:center_index]
        right_sublist = user_list[center_index:]

        print(f"split => left: {left_sublist} right: {right_sublist}")

        left = self.merge_sort(sort_mode, left_sublist)
        right = self.merge_sort(sort_mode, right_sublist)

        merged_list = []
        while True:
            if len(left) == 0 and len(right) == 0:
                break
            elif len(left) != 0 and len(right) == 0:
                merged_list += left
                left.clear()
            elif len(left) == 0 and len(right) != 0:
                merged_list += right
                right.clear()
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
                else:
                    print("ERROR")

        print(f"merge => {merged_list}")
        return merged_list

app = sorting_algorithm_app()


# TODO
# TRY AGAIN OR EXIT FUNC AFTER EVERY SORT
# REMOVE EMERGENCY ERROR PRINTS