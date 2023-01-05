class sorting_algorithm_app:
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

        sort_choice = input("\nWhich sort to use?  ")
        list_info = self.configure_list()
        sorted_list = self.sort(sort_choice, list_info)
        print(f"Final Sorted List: {sorted_list}")

    def configure_list(self):
        while True:
            try:
                num_of_elements = int(input("\nHow many elements are there on your list?  "))
            except (TypeError, ValueError):
                print("Number of elements must be an integer!")
                continue
            else:
                break
                
        type_of_elements = input("Type of elements: [1] integer or [2] letters:  ")
        sort_mode = input("Sort mode: [1] ascending, [2] descending, [3] alphabetically:  ")
        user_list = []
        for counter in range(num_of_elements):
            element = input("Enter your element:  ")
            user_list.append(element)
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