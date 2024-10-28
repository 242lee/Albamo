keyboard = "".join(input() for _ in range(4))
shotgun_points = input()

key_positions = [keyboard.index(key) for key in shotgun_points]
average_position = sum(key_positions) // 9

print(keyboard[average_position])
