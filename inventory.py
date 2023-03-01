import tkinter as tk


# Open a master-list to store the shoe objects
shoes = []

# Create the shoe class initialised with these five properties
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


        pass


# The get cost and get quantity loop through the shoes list and return
# the cost and quantity components of the objects into their respective lists and display these

def get_cost():
    costs = []
    for indx in range(len(shoes)):
        costs.append(shoes[indx].cost)

    print(costs)


    pass




def get_quantity():
    quantities = []
    for indx in range(len(shoes)):
        quantities.append(shoes[indx].quantity)

    print(quantities)
    pass



# This allows the objects actual data to be displayed as a string in the console
def __str__(self):
    return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"



# This function opens the inventory file, skips the first line using the next command,
# Then loops through the txt file lines strips and splits the words by the comma then appends the data into the
# relevant position relative to the initialised object
# A shoe object is created for each line and the cost and quantity class instances are changed into numeric data points.
def read_shoes_data():

    with open('inventory.txt', 'r') as file:
        next(file)
        try:
            for lines in file:
                boy = lines.strip()
                new = boy.split(",")
                shoes.append(Shoe(new[0], new[1], new[2], float(new[3]), int(new[4])))
        except:
            print("File directory cannot be found.")

    pass





# This function allows the user to create a new shoe object to the shoe list
def capture_shoes():

    shoe_info = input("Please enter data about the shoe in this format (country, code, product, cost, quantity)")
    info_real = shoe_info.split(", ")
    shoes.append(Shoe(info_real[0], info_real[1], info_real[2], info_real[3], info_real[4]))


    pass





# This function loops through the shoe list and prints all the objects variables to the console
def view_all():

    for indx in range(len(shoes)):
        print(shoes[indx].country, shoes[indx].code, shoes[indx].product, shoes[indx].cost, shoes[indx].quantity, "\n")

    pass




# This function loops through the shoes list and creates a new list for quantites of all the shoes
# The lowest quantity shoe is then found with the min functionthe index of this object is then found
# The program then interacts with the user asking for inputs concernign the re-stock
# The user chooses the amount to restock, the program then changes and displays the new quantity for the user
# The inventory file is then opened and the program finds the line with the shoe that needs a re-stock
# The new data from the shoes list is then written over the previous data
def re_stock():

    for indx in range(len(shoes)):
        quantities = []
        for indx in range(len(shoes)):
            quantities.append(shoes[indx].quantity)

        re_up = min(quantities)
        ind = quantities.index(re_up)

        print(f"The shoe that needs restocking is: {shoes[ind]}")
        print(f"The current quantity for this shoe is: {shoes[ind].quantity}")
        response = input("Do you want to add more shoes to the inventory? (y/n): ")
        if response.lower() == 'y':
            qty_to_add = int(input("Enter the quantity to add: "))
            shoes[ind].quantity = int(shoes[ind].quantity) + qty_to_add
            print(f"The new quantity for this shoe is: {shoes[ind].quantity}")

            with open('inventory.txt', 'r') as file:
                lines = file.readlines()
            lines[
                ind + 1] = f"{shoes[ind].country}, {shoes[ind].code}, {shoes[ind].product}, {shoes[ind].cost}, {shoes[ind].quantity}\n"
            with open('inventory.txt', 'w') as file:
                file.writelines(lines)
        else:
            print("No shoes were added to the inventory.")


    pass






# This function allows the user to search through the shoes using the shoe codes provided
# A codes list is created, the function loops through the shoes list and takes the codes
# There is then a conditional that the input code matches a shoe at which point all the object data is displayed
def search_shoe():
    while True:
        choice = input("Enter the shoe code you want to search for:")
        codes = []

        for indx in range(len(shoes)):
            codes.append(shoes[indx].code)

            if choice.upper() == shoes[indx].code:
                print(f"{shoes[indx].country}, {shoes[indx].code}, "
                      f"{shoes[indx].product}, {shoes[indx].cost}, {shoes[indx].quantity}\n")
                break
        else:
            print("This is an invalid code, please ensure all contained characters are correct.")


        pass




# This section loops through the shoe list and takes the data for quantity and costs
# The two lists are then looped through and using the zip function they are multiplied and appended to a new
# list which displays the stock values, this is then printed at the end of the other object data points
def value_per_item():
    costs = []
    quantities = []
    stock_values = []
    for indx in range(len(shoes)):
        costs.append(shoes[indx].cost)
        quantities.append(shoes[indx].quantity)

    for i1, i2 in zip(costs, quantities):
        stock_values.append(i1*i2)

    for indx in range(len(shoes)):
        print(f"{shoes[indx].country}, {shoes[indx].code}, {shoes[indx].product},"
              f" {shoes[indx].cost}, {shoes[indx].quantity}, {stock_values[indx]}\n")

    pass





# This function acquires the quantity data, then finds the shoe
# with the largest quantity and prints the data for this shoe (For sale)
def highest_qty():

    quantities = []
    for indx in range(len(shoes)):
        quantities.append(shoes[indx].quantity)

    many = max(quantities)
    ind = quantities.index(many)
    print(f"FOR SALE: {shoes[ind].country}, {shoes[ind].code}, {shoes[ind].product},"
          f" {shoes[ind].cost}, {shoes[ind].quantity}\n")

    pass






# Earlier I imported the tkinter package as tk in order to develop a simple GUI menu.
# It is a simple page with a title, all the function labels and buttons to trigger the code.


def menu():
    menu_window = tk.Tk()
    menu_window.title("Menu")
    tk.Label(menu_window, text = "Menu").grid(row = 0, column = 0)
    tk.Label(menu_window, text = "Get Cost  ").grid(row = 1, column =0)
    register_button = tk.Button(menu_window, text = " ", command = lambda: get_cost())
    register_button.grid(row = 1, column = 1)

    tk.Label(menu_window, text = "Get Quantity  ").grid(row=2, column=0)
    add_task_button = tk.Button(menu_window, text=" ", command=lambda: get_quantity())
    add_task_button.grid(row=2, column=1)

    tk.Label(menu_window, text="Capture Shoe  ").grid(row=3, column=0)
    view_all_tasks_button = tk.Button(menu_window, text=" ", command=lambda: capture_shoes())
    view_all_tasks_button.grid(row=3, column=1)

    tk.Label(menu_window, text="View all shoes  ").grid(row=4, column=0)
    view_my_tasks_button = tk.Button(menu_window, text=" ", command=lambda: view_all())
    view_my_tasks_button.grid(row=4, column=1)

    tk.Label(menu_window, text="Re-stock  ").grid(row=5, column=0)
    view_my_tasks_button = tk.Button(menu_window, text=" ", command=lambda: re_stock())
    view_my_tasks_button.grid(row=5, column=1)

    tk.Label(menu_window, text="Search for a shoe  ").grid(row=6, column=0)
    view_my_tasks_button = tk.Button(menu_window, text=" ", command=lambda: search_shoe())
    view_my_tasks_button.grid(row=6, column=1)

    tk.Label(menu_window, text="Shoe's stock value  ").grid(row=7, column=0)
    view_my_tasks_button = tk.Button(menu_window, text=" ", command=lambda: value_per_item())
    view_my_tasks_button.grid(row=7, column=1)

    tk.Label(menu_window, text="Highest quantity shoe ").grid(row=8, column=0)
    view_my_tasks_button = tk.Button(menu_window, text="", command=lambda: highest_qty())
    view_my_tasks_button.grid(row=8, column=1)

    menu_window.mainloop()



# Initial reading and menu trigger

read_shoes_data()
menu()



