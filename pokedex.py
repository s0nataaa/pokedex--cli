import requests

while True:
    ask = input("Enter a Pokémon name or q to quit: ")

    if ask.lower() == 'q':
        print("See you next time, champ!")
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{ask.lower()}"
    response = requests.get(url)
    

    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name'].capitalize()}")
        print("Type(s):", end=" ")
        print(", ".join(t['type']['name'] for t in data['types']))
        print(f"Order: {data['order']}")
        print("Abilities:")
        for abilities in data['abilities']:
            print(f"- {abilities['ability']['name']}")
        print("Stats:")
        for stat in data['stats']:
            print(f"- {stat['stat']['name']}: {stat['base_stat']}")
    else:
        print("Pokémon not found. Please try again.")
