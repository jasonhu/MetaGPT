# System
Role: You are a professional software engineer, and your main task is to review and revise the code. You need to ensure that the code conforms to the google-style standards, is elegantly designed and modularized, easy to read and maintain.
Language: Please use the same language as the user requirement, but the title and code should be still in English. For example, if the user speaks Chinese, the specific text of your answer should also be in Chinese.
ATTENTION: Use '##' to SPLIT SECTIONS, not '#'. Output format carefully referenced "Format example".

# Context
## System Design
{"Implementation approach":"To create a simple and educational 'Hello, World!' game, we will use Python along with the Pygame library for the graphical interface. Pygame is an open-source library that is well-suited for creating games and multimedia applications, and it is simple enough for this project while providing the necessary functionality for a user-friendly interface.","File list":["main.py","game.py","assets.py"],"Data structures and interfaces":"classDiagram\n    class Game {\n        -display: Surface\n        -clock: Clock\n        +start()\n        +run()\n        +display_message(text: str)\n    }\n    class assets {\n        +get_message() str\n        +get_congratulatory_message() str\n    }\n    Game --> assets\n","Program call flow":"sequenceDiagram\n    participant G as Game\n    participant A as assets\n    G->>A: get_message()\n    A-->>G: return 'Hello, World!'\n    G->>G: display_message('Hello, World!')\n    G->>A: get_congratulatory_message()\n    A-->>G: return 'Congratulations!'\n    G->>G: display_message('Congratulations!')\n","Anything UNCLEAR":"The original requirement does not specify the desired level of interactivity or complexity in the game mechanics. Clarification on whether the game should include challenges or interactive elements beyond displaying the message would be helpful."}

## Task
{"Required packages":["pygame==2.1.2"],"Required Other language third-party packages":["No third-party dependencies required"],"Logic Analysis":[["main.py","Contains the entry point of the application, initializes the Game class, and starts the game loop."],["game.py","Holds the Game class which manages the display, clock, and game flow, including displaying messages."],["assets.py","Contains utility functions to retrieve messages and assets for the game."]],"Task list":["main.py","game.py","assets.py"],"Full API spec":"<none>","Shared Knowledge":"`assets.py` contains functions that provide text messages for the game, which are used by the Game class in `game.py`.","Anything UNCLEAR":"The user requirement does not specify if there are any additional features or complexity desired in the game beyond the basic 'Hello, World!' message display. Clarification on this would help in planning the project scope accurately."}

## Code Files



-----

## Code to be Reviewed: main.py
```Code
import pygame
from pygame.locals import QUIT, KEYDOWN

from game import Game
from assets import get_message, get_congratulatory_message

## Initialize Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

## Main Program
def main():
    # Initialize Pygame and create a window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hello, World! Game")
    
    # Initialize the Game object
    game = Game(screen)

    # Main game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:  # Example of interaction: exit on any key press
                game.display_message(get_congratulatory_message())
                clock.tick(1)  # Wait for 1 second before closing
                running = False

        # Display the initial message
        game.display_message(get_message())
        
        # Update the display and tick the clock
        pygame.display.flip()
        clock.tick(FPS)

    # Clean up and quit the game
    pygame.quit()

if __name__ == "__main__":
    main()

```



-----

# Code Review Format example 1
## Code Review: main.py
1. No, we should fix the logic of class A due to ...
2. ...
3. ...
4. No, function B is not implemented, ...
5. ...
6. ...

## Actions
1. Fix the `handle_events` method to update the game state only if a move is successful.
   ```python
   def handle_events(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return False
           if event.type == pygame.KEYDOWN:
               moved = False
               if event.key == pygame.K_UP:
                   moved = self.game.move('UP')
               elif event.key == pygame.K_DOWN:
                   moved = self.game.move('DOWN')
               elif event.key == pygame.K_LEFT:
                   moved = self.game.move('LEFT')
               elif event.key == pygame.K_RIGHT:
                   moved = self.game.move('RIGHT')
               if moved:
                   # Update the game state only if a move was successful
                   self.render()
       return True
   ```
2. Implement function B

## Code Review Result
LBTM

-----

# Code Review Format example 2
## Code Review: main.py
1. Yes.
2. Yes.
3. Yes.
4. Yes.
5. Yes.
6. Yes.

## Actions
pass

## Code Review Result
LGTM

-----



# Instruction: Based on the actual code, follow one of the "Code Review Format example".
- Note the code filename should be `main.py`. Return the only ONE file `main.py` under review.

## Code Review: Ordered List. Based on the "Code to be Reviewed", provide key, clear, concise, and specific answer. If any answer is no, explain how to fix it step by step.
1. Is the code implemented as per the requirements? If not, how to achieve it? Analyse it step by step.
2. Is the code logic completely correct? If there are errors, please indicate how to correct them.
3. Does the existing code follow the "Data structures and interfaces"?
4. Are all functions implemented? If there is no implementation, please indicate how to achieve it step by step.
5. Have all necessary pre-dependencies been imported? If not, indicate which ones need to be imported
6. Are methods from other files being reused correctly?

## Actions: Ordered List. Things that should be done after CR, such as implementing class A and function B

## Code Review Result: str. If the code doesn't have bugs, we don't need to rewrite it, so answer LGTM and stop. ONLY ANSWER LGTM/LBTM.
LGTM/LBTM