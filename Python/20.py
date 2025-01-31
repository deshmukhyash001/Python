my_dict = {
    'a': 10,
    'b': 20,
    'c': 5,
    'd': 15,
    'e': 30,
    'f': 25
}

# Extract and sort the values in descending order
sorted_values = sorted(my_dict.values(), reverse=True)

# Get the top 3 values
top_3_values = sorted_values[:3]

# Print the result
print("Highest 3 values in the dictionary are:")
print(top_3_values)