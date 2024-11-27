import random
EMPTY, HIT, MISS, SUNK = "~", "X", "O", "S"


field = [[EMPTY for _ in range(7)] for _ in range(7)]
player_field = [[EMPTY for _ in range(7)] for _ in range(7)]
ships = {3: 1, 2: 2, 1: 4}
ship_positions = []


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
