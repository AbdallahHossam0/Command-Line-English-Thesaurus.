import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        closeMatch = get_close_matches(word, data.keys(), 1, 0.75)
        if len(closeMatch) == 0:
            return ["Word not Found!, Please check it."]
        else:
            checkCloseMatch = input("Do you mean <<%s>> if yes press y or n to exit: " %closeMatch[0])
            if checkCloseMatch.lower() == 'y':
                return data[closeMatch[0]]
            else:
                return ["Word not Found!, Please check it."]

while True:
    word = input("\nEnter a Word: ")
    print("\n".join((translate(word))))


