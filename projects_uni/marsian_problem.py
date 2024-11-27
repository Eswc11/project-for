import random
weights = [random.randint(1, 711), random.randint(1, 712), 713]
weights[2] -= weights[0] + weights[1]
coordinates = random.sample(range(1, 8), 3)
total_cargo = 0

print("Martian Cargo Finder!")
print("Find all three boxes by entering their coordinates.")
print("The total weight of the boxes must be 713 kg.")

while total_cargo != 713:
    guesses = input("Enter 3 coordinates (1-7) separated by spaces: ").split()

    try:
        guesses = [int(g) for g in guesses]
        if len(set(guesses)) != 3 or any(g < 1 or g > 7 for g in guesses):
            raise ValueError
    except ValueError:
        print("Invalid input. Make sure coordinates are unique and between 1-7.")

    if sorted(guesses) == sorted(coordinates):
        total_cargo = sum(weights)
        print(f"Congratulations! Total weight: {total_cargo} kg.")
        if total_cargo == 713:
            print("The cargo has been fully recovered!")
            break
    else:
        print("Incorrect coordinates! Boxes moved to new locations.")
        coordinates = random.sample(range(1, 8), 3)
        weights = [random.randint(1, 711), random.randint(1, 712), 713]
        weights[2] -= weights[0] + weights[1]
