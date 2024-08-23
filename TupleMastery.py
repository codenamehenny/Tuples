#1. Tuple Mastery in Python
#Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination).
itineraries = []


def format_itineraries(traveler_name, origin, destination):
    itineraries.append((traveler_name, origin, destination))
    new_index = len(itineraries) - 1
    print(f"\n'Itinerary {new_index + 1}: {itineraries[new_index][0]} - From {itineraries[new_index][1]} to {itineraries[new_index][2]}' has been added")
    return itineraries

def add_flight():
    while True:
        print("\nWelcome to the Flight Tracker!")
        print("1. Add itinerary\n2. View itineraries \n3. Quit")
        try:
            option = int(input("Choose an option number: "))
            if option == 1:
                traveler_name = input("What's the traveler's name? ")
                origin = input("Where is the flight coming from? ")
                destination = input("Where is the flight going? ")
                format_itineraries(traveler_name, origin, destination)
            elif option == 2:
                print("Here are the scheduled flights:")
                for index, intinerary in enumerate(itineraries):
                    print(f"Itinerary {index + 1}: {intinerary[0]} - From {intinerary[1]} to {intinerary[2]}")
            elif option == 3:
                break
        except ValueError:
            print("Invalid input, please select a number")

add_flight()