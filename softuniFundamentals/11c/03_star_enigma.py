import re

how_many = int(input())
pattern_keys = r"(?i)[s,t,a,r]"
pattern_message = r"@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([A|D])![^@\-!:>]*->(\d+)"
attacked_planets = []
destroyed_planets = []

for _ in range(how_many):
    encrypted_message = input()
    decrypted_message = ""

    looking_for_key = re.findall(pattern_keys, encrypted_message)
    key = len(looking_for_key)

    for character in encrypted_message:
        symbol = ord(character) - key
        decrypted_message += chr(symbol)

    break_down = re.search(pattern_message, decrypted_message)
    if break_down:
        planet_name = break_down.group(1)
        attack_type = break_down.group(3)

        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)

attacked_planets.sort()
destroyed_planets.sort()
print(f"Attacked planets: {len(attacked_planets)}")
for x in attacked_planets:
    print(f"-> {x}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for y in destroyed_planets:
    print(f"-> {y}")
