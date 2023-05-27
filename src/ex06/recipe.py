cookbook = {
    'sandwich':
        {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
         'meal': 'lunch',
         'prep_time': 10},
    'cake':
        {'ingredients': ['flour', 'sugar', 'eggs'],
         'meal': 'dessert',
         'prep_time': 60},
    'salad':
        {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
         'meal': 'lunch',
         'prep_time': 15},
}


def add_recipe(book):
    print('>>> Enter a name:')
    recipe = input().strip().lower()
    while not recipe:
        recipe = input().strip().lower()
    print('>>> Enter ingredients:')
    ingredients = []
    ingredient = input().strip()
    while ingredient:
        ingredients.append(ingredient)
        ingredient = input().strip()
    print('>>> Enter meal type:')
    meal = input().strip()
    while not meal:
        meal = input().strip()
    print('>>> Enter preparation time:')
    time = input().strip()
    while not time and not time.isdigit():
        time = input().strip()
    book[recipe] = {'ingredients': ingredients, 'meal': meal, 'prep_time': time}
    print()


def remove_recipe(book):
    print('Please enter a recipe name to remove:')
    recipe = input('>> ').lower().strip()
    if recipe not in cookbook:
        print('Sorry, this recipe does not exist.')
    else:
        del book[recipe]
    print()


def print_recipe(book, recipe=None):
    if not recipe:
        print('Please enter a recipe name to get its details:')
        recipe = input('>> ').lower().strip()
        print()
    if recipe not in cookbook:
        print('Sorry, this recipe does not exist.')
    else:
        print(f'Recipe for {recipe}:')
        print(f'   Ingredients list: {book[recipe]["ingredients"]}')
        print(f'   To be eaten for {book[recipe]["meal"]}.')
        print(f'   Takes {book[recipe]["prep_time"]} minutes of cooking.\n')


def print_book(book):
    for recipe in book:
        print(f'- {recipe}')
    print()


def print_options():
    print('''List of available option:
   1: Add a recipe
   2: Delete a recipe
   3: Print a recipe
   4: Print the cookbook
   5: Quit
''')


def get_option():
    print('Please select an option:')
    option = input('>> ').strip()
    print()
    return option


print('Welcome to the Python Cookbook !')
print_options()

option = get_option()
while option != '5':
    if option == '1':
        add_recipe(cookbook)
    elif option == '2':
        remove_recipe(cookbook)
    elif option == '3':
        print_recipe(cookbook)
    elif option == '4':
        print_book(cookbook)
    else:
        print('Sorry, this option does not exist.\n')
        print_options()
    option = get_option()

print('Cookbook closed. Goodbye !')
