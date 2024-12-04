import random

name = input("Enter your name: ")
EMPTY, HIT, MISS, SUNK = "~", "X", "O", "S"

field = [[EMPTY for _ in range(7)] for _ in range(7)]
player_field = [[EMPTY for _ in range(7)] for _ in range(7)]
ships = {3: 1, 2: 2, 1: 4}
ship_positions = []
leaderboard = []


for length, count in ships.items():
    for _ in range(count):
        placed = False
        while not placed:
            x, y = random.randint(0, 6), random.randint(0, 6)
            direction = random.choice(["H", "V"])
            positions = [
                (x + i, y) if direction == "H" else (x, y + i) for i in range(length)
            ]
            if all(
                0 <= nx < 7 and 0 <= ny < 7 and field[ny][nx] == EMPTY
                and not any(
                    0 <= nx + dx < 7 and 0 <= ny + dy < 7 and field[ny + dy][nx + dx] != EMPTY
                    for dx in range(-1, 2)
                    for dy in range(-1, 2)
                )
                for nx, ny in positions
            ):
                for nx, ny in positions:
                    field[ny][nx] = str(length)
                ship_positions.append(positions)
                placed = True

shots = 0
while True:
    print("\033[H\033[J", end="")
    print("  A B C D E F G")
    for i, row in enumerate(player_field):
        print(f"{i + 1} " + " ".join(row))

    while True:
        move = input("Enter the coordinates of the shot (for example, B3): ").upper()
        if len(move) == 2 and move[0] in "ABCDEFG" and move[1].isdigit() and 1 <= int(move[1]) <= 7:
            x, y = ord(move[0]) - ord("A"), int(move[1]) - 1
            if player_field[y][x] in {HIT, MISS}:
                print("You've already shot here! Try again.")
                continue
            break
        print("Invalid input! Try again.")

    shots += 1
    if field[y][x].isdigit():
        player_field[y][x] = HIT
        ship_id = field[y][x]
        field[y][x] = HIT

        sunk = True
        for pos in ship_positions:
            if any(field[ny][nx] == ship_id for nx, ny in pos):
                sunk = False
                break
        if sunk:
            for pos in ship_positions:
                if any(field[ny][nx] == ship_id for nx, ny in pos):
                    for nx, ny in pos:
                        player_field[ny][nx] = SUNK
            print("The ship is destroyed!")
        else:
            print("Hit!")
    else:
        player_field[y][x] = MISS
        print("Miss!")

    if all(all(cell not in "123" for cell in row) for row in field):
        print("\033[H\033[J", end="")
        print("  A B C D E F G")
        print("\n".join(f"{i + 1} " + " ".join(row) for i, row in enumerate(player_field)))
        print(f"Victory! You're done {shots} shots.")
        name = input("Enter your name: ")
        leaderboard.append((name, shots))
        leaderboard.sort(key=lambda x: x[1])
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Leaderboard:")
            for rank, (name, shots) in enumerate(leaderboard, start=1):
                print(f"{rank}. {name}: {shots} shots")

        break
