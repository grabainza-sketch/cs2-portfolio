# Exercise 1: My School Bag
# Create a list containing five school supplies
item = ["Notebook","Pen","Calculator","Laptop","Book"]

# Print a header for the school bag section
print("~~~~~~~~~~~~~~MY SCHOOL BAG~~~~~~~~~~~~~~")

# Display the first item in the list using index 0
print(item[0])

# Display the middle items using list slicing (indices 1 to 3)
print(item[1:4])

# Display the last item in the list using index 4
print(item[4])

# Ask the user to pick an index number and convert the input to an integer
take = int(input("Choose what to take (0-4): "))

# Print the item corresponding to the user's chosen index
print("You took the", item[take])

# Print an empty line for spacing between exercises
print("")

# Exercise 2: Travel Destination Manager
# Create a list containing five travel destinations
destinations = ["Cebu","Manila","Davao","Baguio","Palawan"]

# Print a header for the travel destination manager section
print("~~~~~~~~~~~~~~TRAVEL DESTINATION MANAGER~~~~~~~~~~~~~~")

# Loop through the list and print each destination one by one
for destination in destinations:
    print(destination)

# Use slicing to display destinations from index 1 up to (but not including) index 4
print("Destinations from index 1 to 3:")
print(destinations[1:4])

# Prompt the user to type a destination and remove any extra spaces
search_query = input("Enter a destination to search for: ").strip()

# Check if the user's input matches any destination in the list (ignoring uppercase/lowercase differences)
if any(search_query.lower() == d.lower() for d in destinations):
    print(f"Yes, {search_query} is in the list of destinations!")
else:
    print(f"{search_query} was not found in the list.")

# Update the destination at index 2 ("Davao") to "Iloilo"
destinations[2] = "Iloilo"

# Display the newly updated list of destinations
print("Updated Travel Destinations:")
print(destinations)
