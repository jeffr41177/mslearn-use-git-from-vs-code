# Define a sample dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Get a view of the dictionary values
values_view = my_dict.values()
print(f'{values_view}')

# Convert the view to a list (if needed) and find its length
total_items = len(list(values_view))

# Print the total number of items in the dictionary
print("Total items in the dictionary:", total_items)

