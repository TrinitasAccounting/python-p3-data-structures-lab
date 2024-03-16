spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [food['name'] for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spicy_food_names = [food for food in spicy_foods if food['heat_level'] > 5]
    return spicy_food_names

def print_spicy_foods(spicy_foods):
    [print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * "🌶"}')  for food in spicy_foods]


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_food = [food for food in spicy_foods if food['cuisine'] == cuisine]
    return matching_food[0]

def print_spiciest_foods(spicy_foods):
    [print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * "🌶"}')  for food in spicy_foods  if food["heat_level"] > 5]

def get_average_heat_level(spicy_foods):
    list_of_spice_values = [food['heat_level'] for food in spicy_foods]
    average_spice = sum(list_of_spice_values) / len(list_of_spice_values)
    return average_spice

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
