```
classDiagram
    class Game {
        -screen: pygame.display
        -clock: pygame.time.Clock
        +start()
        +run()
        +handle_events()
        +update()
        +render()
    }
    class Assets {
        +load_images()
        +load_sounds()
    }
    class Config {
        -screen_width: int
        -screen_height: int
        -fps: int
        +get_screen_size()
        +get_fps()
    }
    class Main {
        +main()
    }
    Game --> Assets
    Game --> Config
    Main --> Game

```

```
@startuml
classDiagram
    class Game {
        -screen: pygame.display
        -clock: pygame.time.Clock
        +start()
        +run()
        +handle_events()
        +update()
        +render()
    }
    class Assets {
        +load_images()
        +load_sounds()
    }
    class Config {
        -screen_width: int
        -screen_height: int
        -fps: int
        +get_screen_size()
        +get_fps()
    }
    class Main {
        +main()
    }
    Game --> Assets
    Game --> Config
    Main --> Game
@enduml
```
==========

```
sequenceDiagram
    participant M as Main
    participant G as Game
    participant A as Assets
    participant C as Config
    M->>G: start()
    G->>A: load_images()
    G->>A: load_sounds()
    G->>C: get_screen_size()
    G->>C: get_fps()
    G->>G: run()
    loop for each frame
        G->>G: handle_events()
        G->>G: update()
        G->>G: render()
    end
```