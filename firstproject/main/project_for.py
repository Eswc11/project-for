import random
weights = [random.randint(50, 300) for _ in range(3)]
coordinates = [random.randint(1, 7) for _ in range(3)]

print("Martian Cargo Finder!")
print("Find all three boxes by entering their coordinates.")

print(f"(DEBUG) Initial weights: {weights}")
print(f"(DEBUG) Initial coordinates: {coordinates}")

while True:
    a = int(input('Enter 1st number (1-7): '))
    b = int(input('Enter 2nd number (1-7): '))
    c = int(input('Enter 3rd number (1-7): '))
    while True:
        try:
            a = int(input('Enter 1st number (1-7): '))
            if not (1 <= a <= 7):
                raise ValueError
            b = int(input('Enter 2nd number (1-7): '))
            if not (1 <= b <= 7):
                raise ValueError
            if a + b > 7:
                raise ValueError("The sum of the coordinates is illogical. Try again.")
            c = int(input('Enter 3rd number (1-7): '))
            if not (1 <= c <= 7):
                raise ValueError
            break
        except ValueError:
            print("Error: Please enter numbers between 1 and 7.")

    if sorted([a, b, c]) == sorted(coordinates):
        total_weight = sum(weights)
        print(f"Congratulations! You found all the boxes.")
        print(f"Total weight: {total_weight} kg")
        if total_weight == 713:
            print("Success! The cargo has been fully recovered!")
            break
        else:
            print(f"Error: The total weight ({total_weight} kg) does not match 713 kg.")
    else:
        print("Wrong coordinates! The boxes moved to new locations.")
        coordinates = [random.randint(1, 7) for _ in range(3)]
        weights = [random.randint(50, 300) for _ in range(3)]

        # print(f"(DEBUG) New weights: {weights}")
        # print(f"(DEBUG) New coordinates: {coordinates}")
