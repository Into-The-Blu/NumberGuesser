import json
import os

#scoreboard = [63,42,24,21,20,19,18,17,16,12]

f = open(f"{os.getcwd()}/Python/NumberGuesser v0.1/scoreboard.json", mode="r", encoding="utf-8")

scoreboard = json.load(f)

scoreboard = json.loads(scoreboard)

print(scoreboard)

#{
#    "scoreboard": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
#}

