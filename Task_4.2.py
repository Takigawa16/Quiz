#Single Array
single_dim_array = [1, 2, 3, 4, 5]

#Two Dimensional Array
two_dim_array = [
    [1, 2, 3],
    ["apple", "banana", "cherry"],
    [True, False]
]

# Function to display single dimensional array
def display_single_dim_array():
 for element in single_dim_array:
  print(element)

# Function to display single dimensional array 
def display_two_dim_array():
 for element in two_dim_array:
  print(element)

# User Input
choice = input("Choose Array to display (1 for Single dimension Array, 2 for Two Dimensional Array) ")

# Display Based on the choice
if choice == '1':
  display_single_dim_array()
elif choice == '2':
  display_two_dim_array()
else:
   print("Invalid Choice ")
