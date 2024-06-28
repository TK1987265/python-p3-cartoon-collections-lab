def roll_call_dwarves(dwarves):
    for index, name in enumerate(dwarves, 1):
        print(f"{index}. {name}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(items):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for item in items:
        if item in cheeses:
            return item
    return None

# Example usage:
if __name__ == "__main__":
    dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
    roll_call_dwarves(dwarves)

    planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
    print(summon_captain_planet)