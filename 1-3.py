# Create an empty dictionary to store name-favorite fruit pairs
fruit_preferences = {}

# Input names and favorite fruits
while True:
    name = input("Please enter a name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    
    favorite_fruits = input("Please enter your favorite fruits, separated by spaces: ").split()
    
    # Store the favorite fruits in the dictionary
    for fruit in favorite_fruits:
        if fruit in fruit_preferences:
            fruit_preferences[fruit].append(name)
        else:
            fruit_preferences[fruit] = [name]

# Query someone's favorite fruit
while True:
    query_name = input("Enter a name to query their favorite fruit (or 'quit' to stop): ")
    if query_name.lower() == 'quit':
        break
    
    if query_name in fruit_preferences:
        print(f"{query_name}'s favorite fruit(s): {', '.join(fruit_preferences[query_name])}")
    else:
        print(f"{query_name} has not shared their favorite fruit.")

# Query people who like a certain fruit
while True:
    query_fruit = input("Enter a fruit to find people who like it (or 'quit' to stop): ")
    if query_fruit.lower() == 'quit':
        break
    
    if query_fruit in fruit_preferences:
        print(f"People who like {query_fruit}: {', '.join(fruit_preferences[query_fruit])}")
    else:
        print(f"Nobody has listed {query_fruit} as their favorite fruit.")

# Example usage:
# Please enter a name (or 'quit' to stop): Bob
# Please enter your favorite fruits, separated by spaces: Apple banana watermelon
# Please enter a name (or 'quit' to stop): Alice
# Please enter your favorite fruits, separated by spaces: Banana strawberry
# Please enter a name (or 'quit' to stop): quit
# Enter a name to query their favorite fruit (or 'quit' to stop): Bob
# Bob's favorite fruit(s): Apple, banana, watermelon
# Enter a name to query their favorite fruit (or 'quit' to stop): John
# John has not shared their favorite fruit.
# Enter a fruit to find people who like it (or 'quit' to stop): Banana
# People who like Banana: Bob, Alice
# Enter a fruit to find people who like it (or 'quit' to stop): Grape
# Nobody has listed Grape as their favorite fruit.
# Enter a fruit to find people who like it (or 'quit' to stop): quit
