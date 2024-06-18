import random
matches = []

while True:
    match = input("Enter a team (or 'stop' to stop): ")
    if match.lower() == "stop":
        break
    matches.append(match)
if len(matches) % 2 != 0:
    print("Odd number of teams entered. Adding a 'bye' to make it even.")
    matches.append(" yet to be fixed ")
random.shuffle(matches)
fixtures = []
for i in range(0, len(matches), 2):
    fixtures.append((matches[i], matches[i + 1]))
print("\nMatch Fixtures:")
for fixture in fixtures:
    print(f"{fixture[0]} vs {fixture[1]}")
