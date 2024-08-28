## context
{"Language":"en_us","Programming Language":"Python","Original Requirements":"Create a hello world game","Project Name":"hello_world_game","Product Goals":["Provide a simple and intuitive gaming experience","Ensure ease of use for all user levels","Engage users with a creative take on the classic 'Hello, World!' concept"],"User Stories":["As a player, I want to be able to easily start the game and understand the objective","As a player, I want to receive clear feedback when I successfully complete a task in the game","As a player, I want the game to be visually appealing and fun to play","As a player, I want to be able to play the game on my computer or mobile device"],"Competitive Analysis":["ClassicHelloWorld: Too basic, lacks engagement","HelloWorldAdventures: More interactive but complex, less accessible","SayHelloGame: Visually appealing but limited in gameplay"],"Competitive Quadrant Chart":"quadrantChart\n    title \"Game Engagement and Accessibility\"\n    x-axis \"Low Engagement\" --> \"High Engagement\"\n    y-axis \"Low Accessibility\" --> \"High Accessibility\"\n    quadrant-1 \"Potential for Improvement\"\n    quadrant-2 \"Engaging but Complex\"\n    quadrant-3 \"Accessible but Boring\"\n    quadrant-4 \"Optimal Balance\"\n    \"ClassicHelloWorld\": [0.2, 0.8]\n    \"HelloWorldAdventures\": [0.7, 0.4]\n    \"SayHelloGame\": [0.6, 0.6]\n    \"Our Target Product\": [0.5, 0.7]","Requirement Analysis":"The game should have a simple interface and mechanics while providing a unique twist on the traditional 'Hello, World!' program.","Requirement Pool":[["P0","Core game mechanics that involve interaction with the 'Hello, World!' concept"],["P1","Responsive design to accommodate various screen sizes"],["P1","Basic audio feedback for user actions"]],"UI Design draft":"A clean and simple interface with a playful font and colorful graphics. The game will have a main screen with a start button and a game area where the hello world interactions occur.","Anything UNCLEAR":"The original requirements are quite vague. Clarification is needed on what specific interactions or challenges the user expects in the game."}

-----

## format example
[CONTENT]
{
    "Implementation approach": "We will ...",
    "File list": [
        "main.py",
        "game.py"
    ],
    "Data structures and interfaces": "\nclassDiagram\n    class Main {\n        -SearchEngine search_engine\n        +main() str\n    }\n    class SearchEngine {\n        -Index index\n        -Ranking ranking\n        -Summary summary\n        +search(query: str) str\n    }\n    class Index {\n        -KnowledgeBase knowledge_base\n        +create_index(data: dict)\n        +query_index(query: str) list\n    }\n    class Ranking {\n        +rank_results(results: list) list\n    }\n    class Summary {\n        +summarize_results(results: list) str\n    }\n    class KnowledgeBase {\n        +update(data: dict)\n        +fetch_data(query: str) dict\n    }\n    Main --> SearchEngine\n    SearchEngine --> Index\n    SearchEngine --> Ranking\n    SearchEngine --> Summary\n    Index --> KnowledgeBase\n",
    "Program call flow": "\nsequenceDiagram\n    participant M as Main\n    participant SE as SearchEngine\n    participant I as Index\n    participant R as Ranking\n    participant S as Summary\n    participant KB as KnowledgeBase\n    M->>SE: search(query)\n    SE->>I: query_index(query)\n    I->>KB: fetch_data(query)\n    KB-->>I: return data\n    I-->>SE: return results\n    SE->>R: rank_results(results)\n    R-->>SE: return ranked_results\n    SE->>S: summarize_results(ranked_results)\n    S-->>SE: return summary\n    SE-->>M: return summary\n",
    "Anything UNCLEAR": "Clarification needed on third-party API integration, ..."
}
[/CONTENT]

## nodes: "<node>: <type>  # <instruction>"
- Implementation approach: <class 'str'>  # Analyze the difficult points of the requirements, select the appropriate open-source framework
- File list: typing.List[str]  # Only need relative paths. ALWAYS write a main.py or app.py here
- Data structures and interfaces: typing.Optional[str]  # Use mermaid classDiagram code syntax, including classes, method(__init__ etc.) and functions with type annotations, CLEARLY MARK the RELATIONSHIPS between classes, and comply with PEP8 standards. The data structures SHOULD BE VERY DETAILED and the API should be comprehensive with a complete design.
- Program call flow: typing.Optional[str]  # Use sequenceDiagram code syntax, COMPLETE and VERY DETAILED, using CLASSES AND API DEFINED ABOVE accurately, covering the CRUD AND INIT of each object, SYNTAX MUST BE CORRECT.
- Anything UNCLEAR: <class 'str'>  # Mention unclear project aspects, then try to clarify it.


## constraint
Language: Please use the same language as Human INPUT.
Format: output wrapped inside [CONTENT][/CONTENT] like format example, nothing else.

## action
Follow instructions of nodes, generate output and make sure it follows the format example.
