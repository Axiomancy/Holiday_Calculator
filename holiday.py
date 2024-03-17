"""
1)Create a program that uses functions to calculate a user's total holiday cost,
which includes the plane cost, hotel cost, and car-rental cost.
2)Prompt the user for holiday information needed to caculate each 
of the costs(plane, hotel and car-rental).
3)Calculate the total cost of all the user's selected holiday options.
4)create the following four functions:
    1.hotel_cost: This function will take num_nights as an argument,
    and return a total cost for the hotel stay.
    2.plane_cost: This function will take city_flight as an argument
    and return a cost for the flight based on th chosen city.
    3.car_rental: This function will take rental_days as an argument
    and return the total cost of the car rental.
    4.holiday_cost: This function will take the three arguments
    hotel_cost, plane_cost, car_rental. Using these three
    arguments, call all three of the above functions with
    respective arguments and finally return a total cost for your
    holiday.
5)Print out all the details about the holiday in a readable way

"""
import tkinter as tk
from tkinter import messagebox

# Calculates the total cost of the hotel stay per night
def hotel_cost(num_nights, y):
    total_cost = int(num_nights * 250) * y
    return(total_cost)

# Calculates the total cost of the flight times by number of passengers
def plane_cost(city_flight, x):
    city_flight = city_flight.lower()  # Convert input to lowercase
    if city_flight in ['milan']:
        cost = 80
    elif city_flight in ['berlin']:
        cost = 50
    elif city_flight in ['paris']:
        cost = 35
    else:
        return "Invalid city code"
    total_cost = cost * x
    return total_cost

# Calculates the cost of the car rental per day
def car_rental(rental_days):
    total_car_cost = int(rental_days * 50)
    return(total_car_cost)

# Calculates the total cost of the holiday using all previous functions
def holiday_cost(city_flight, x, num_nights, y, rental_days):
    total_holiday_cost = plane_cost(city_flight, x) + hotel_cost(num_nights, y) + car_rental(rental_days)
    return(total_holiday_cost)

"""Additional Tkinter code functionality"""
# Function to calculate the total cost of the holiday
def calculate_cost():
    city_flight = city_var.get().lower()
    x = int(passenger_entry.get())
    num_nights = int(nights_entry.get())
    y = int(rooms_entry.get())
    rental_days = int(car_entry.get())
    
    total_cost = holiday_cost(city_flight, x, num_nights, y, rental_days)
    messagebox.showinfo("Total Cost", f"The total cost of your holiday is £{total_cost}")

# Create the main window
root = tk.Tk()
root.title("Holiday Maker")

# Create labels and entries for user input
tk.Label(root, text="Select City:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
city_var = tk.StringVar()
city_var.set("Milan")
city_dropdown = tk.OptionMenu(root, city_var, "Milan", "Berlin", "Paris")
city_dropdown.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number of Passengers:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
passenger_entry = tk.Entry(root)
passenger_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Number of Nights:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
nights_entry = tk.Entry(root)
nights_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Number of Rooms:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
rooms_entry = tk.Entry(root)
rooms_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Number of Car Rental Days:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
car_entry = tk.Entry(root)
car_entry.grid(row=4, column=1, padx=5, pady=5)

# Create a button to calculate the total cost
calculate_button = tk.Button(root, text="Calculate Cost", command=calculate_cost)
calculate_button.grid(row=5, columnspan=2, padx=5, pady=5)

# Run the GUI
root.mainloop()


# Greet the user.
print(('____' * 18) + '''\nGreetings! And welcome to 'The Holiday Maker!'
please select from the following options to build your dream holiday!... ''')
print('____' * 18)

# Using a while loop, prompt the user for input
# Validate city selection is within function
# The cost is attached to the city selected respectively
# If invalid input given, user will be re-prompted
while True:
    city_flight = input('''Please choose from one of the available city 
bookings from the list below...
--Milan--\t:£80/pp
--Berlin--\t:£50/pp
--Paris--\t:£35/pp
 :''').lower()
    if city_flight.isalpha() and city_flight in ['milan', 'berlin', 'paris']:
        break
    else:
        print("Invalid input. Please enter a city from the list")

print('____' * 18)
# Use while loop to prompt the user for input
# Validate a numeric passenger quantity selected
# Cast to integer
# If invalid, user will be re-prompted
while True:
    x = input('''Next, please enter the number of people flying to the selected city: \n''')
    if x.isnumeric():
        x = int(x)
        break
    else:
        print("Invalid input. Please enter the number of passengers in a numeric format(for example... 2)")

print('____' * 18)
# Use while loop to prompt the user for input 
# Validate num nights numeric selection
# Cast to integer
# If invalid, user will be re-prompted
while True:
    num_nights = input('''Please enter the number of nights you would like to stay in your destination.
The cost is £250/pp: \n''')
    if num_nights.isnumeric():
        num_nights = int(num_nights)
        break
    else:
        print("Invalid input. Please enter number of nights in a numeric format(for example... 4)")

print('____' * 18)
# Use while loop to prompt the user for input
# Validate rooms needed numeric format selection
# Cast to integer
# If invalid, user will be re-prompted
while True:
    y = input('''Next, please enter the number rooms needed per night for your stay. 
The cost is £250/per room: \n''')
    if y.isnumeric():
        y = int(y)
        break
    else:
        print("Invalid input. Please enter the rooms needed in a numeric format(for example... 1)")

print('____' * 18)
# Using a while loop to prompt the user a final time for input
# validate car rental days numeric selection
# Cast to integer
# If invalid, user will be re-prompted
while True:
    rental_days = input('''Finally, please enter the number of days you would to rent a car for,
if you do not require a vehicle please enter '0'.
The cost of rental is £50/per day. thank you: \n''')
    if rental_days.isnumeric():
        rental_days = int(rental_days)
        break
    else:
        print("Invalid input. Please enter a whole number or 0")

print('____' * 18)
# Calculate total cost of all selected holiday options
# Print cost
final_total = holiday_cost(city_flight, x, num_nights, y, rental_days)
print(f'This is the final cost of your holiday £{final_total}')
print('____' * 18)

# Print details and prices for clarity including a final TOTAL
print('Please review your selected holiday itinerary below: \n')
print(f'''Destination\t\t:{city_flight}
Flight tickets\t\t:{x}
Hotel stay\t\t:{num_nights}
Hotel rooms\t\t:{y}
Car rental\t\t:{rental_days}
*TOTAL COST*\t\t:{final_total}''')
print('____' * 18)
print('Enjoy your trip & thank you for using')
print(('*' * 12)+'HOLIDAY MAKER'+('*' * 12))
