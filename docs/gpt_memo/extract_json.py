import json

# JSON string provided in the question
json_string = '''
{
    "Implementation approach": "To create a simple and engaging 'Hello, World!' game, we will use the Pygame library for the game engine. Pygame is an open-source library that is well-suited for creating 2D games and is easy to use, making it appropriate for our goal of keeping the architecture simple. We will design the game to be responsive and ensure that it can be played on both computers and mobile devices.",
    "File list": [
        "main.py",
        "game.py",
        "assets.py",
        "config.py"
    ],
    "Data structures and interfaces": "\\nclassDiagram\\n    class Game {\\n        -screen: pygame.display\\n        -clock: pygame.time.Clock\\n        +start()\\n        +run()\\n        +handle_events()\\n        +update()\\n        +render()\\n    }\\n    class Assets {\\n        +load_images()\\n        +load_sounds()\\n    }\\n    class Config {\\n        -screen_width: int\\n        -screen_height: int\\n        -fps: int\\n        +get_screen_size()\\n        +get_fps()\\n    }\\n    class Main {\\n        +main()\\n    }\\n    Game --> Assets\\n    Game --> Config\\n    Main --> Game\\n",
    "Program call flow": "\\nsequenceDiagram\\n    participant M as Main\\n    participant G as Game\\n    participant A as Assets\\n    participant C as Config\\n    M->>G: start()\\n    G->>A: load_images()\\n    G->>A: load_sounds()\\n    G->>C: get_screen_size()\\n    G->>C: get_fps()\\n    G->>G: run()\\n    loop for each frame\\n        G->>G: handle_events()\\n        G->>G: update()\\n        G->>G: render()\\n    end\\n",
    "Anything UNCLEAR": "The original requirements do not specify the exact gameplay mechanics or the visual design of the 'Hello, World!' interactions. Clarification on the desired gameplay elements and the visual style would be helpful in creating a more tailored experience for the users."
}
'''
json_string_valid = json.dumps(json_string)

# Parse the JSON string
data = json.loads(json_string_valid)

data2 = json.loads(data)
# Extract and print the 'content' value
print(data2['Data structures and interfaces'])
print("\n==========\n")
print(data2['Program call flow'])
