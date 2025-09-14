# Pokédex CLI

A simple command-line Pokédex application that fetches Pokémon information using the PokéAPI. Get detailed information about any Pokémon right from your terminal!

## Features

- 🔍 Search for any Pokémon by name
- 📊 Display Pokémon stats (HP, Attack, Defense, etc.)
- 🏷️ Show Pokémon types and abilities
- 📋 Display Pokémon order number
- 🔄 Continuous search until you decide to quit
- 🚫 Error handling for invalid Pokémon names

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Make sure you have Python installed on your system
2. Install the required library:
   ```bash
   pip install requests
   ```
3. Download or clone this repository
4. Run the script:
   ```bash
   python pokedex.py
   ```

## How to Use

1. Run the program
2. Enter a Pokémon name when prompted (e.g., "pikachu", "charizard")
3. View the detailed information about the Pokémon
4. Enter another Pokémon name to continue searching
5. Type 'q' to quit the program

## Example Output

```
Enter a Pokémon name or q to quit: pikachu
Name: Pikachu
Type(s): electric
Order: 35
Abilities:
- static
- lightning-rod
Stats:
- hp: 35
- attack: 55
- defense: 40
- special-attack: 50
- special-defense: 50
- speed: 90
```

## API Used

This project uses the [PokéAPI](https://pokeapi.co/) - a free RESTful API for Pokémon data.

## Error Handling

- If you enter an invalid Pokémon name, the program will display "Pokémon not found. Please try again."
- The program will continue running until you choose to quit with 'q'

## About This Project

This project was created as part of my learning journey in working with APIs for the first time. It was developed with the assistance of AI to help me understand the fundamentals of:
- Making HTTP requests to external APIs
- JSON data parsing and manipulation
- Error handling in API calls
- Building interactive command-line applications

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source. Feel free to use and modify as needed for educational purposes.
