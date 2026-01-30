# garden_advice.py

def main():
    plant = input("Enter the type of plant: ")
    month = input("Enter the month (1-12): ")
    
    optimal_time = get_optimal_planting_time(plant)
    print(f"The optimal planting time for {plant} is: {optimal_time}")

# TODO: Create a function to get optimal planting time
def get_optimal_planting_time(plant):
    # Hardcoded values, consider replacing with a configuration
    planting_times = {
        "tomato": "April to June",
        "cucumber": "May to July",
        "lettuce": "March to August",
        "maize": "October to February"
    }
    
    # TODO: Add error handling for unknown plants
    return planting_times.get(plant.lower(), "Unknown plant type. Please try again.")


if __name__ == "__main__":
    main()
