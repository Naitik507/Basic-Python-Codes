def process():

    count = 0

    def inpt(count):
        
        words = [
    "apple", "brick", "charm", "doubt", "eagle", "flame", "grape", "haste", "index", "jelly",
    "knife", "lemon", "mango", "noble", "ocean", "piano", "quake", "raven", "smile", "trust",
    "ultra", "vivid", "wrist", "xenon", "youth", "zebra", "angel", "brave", "crown", "drift",
    "enter", "frost", "globe", "hover", "ideal", "joint", "karma", "lunar", "medal", "novel",
    "orbit", "petal", "quilt", "reign", "scale", "table", "unite", "vigor", "whale", "xerox",
    "yield", "zesty", "adore", "blend", "climb", "daisy", "ember", "fjord", "grind", "heart",
    "inbox", "jumpy", "kneel", "latch", "mirth", "nudge", "oxide", "plush", "quirk", "rider",
    "spine", "throb", "urged", "vocal", "waltz", "xylem", "yacht", "zonal", "abide", "blaze",
    "crane", "dealt", "evoke", "fable", "gloom", "hound", "inlet", "jaunt", "knead", "liver",
    "mimic", "ninth", "opine", "purse", "quake", "risky", "shine", "truce", "upset", "vapor"]

        word = words[9] # I was not able to access the "Random" Module!

        inp = input("Enter your guess: ")
        
        
        if word == inp.lower():
            count+=1
            print(f"WELL DONE YOU GUESSED THE WORD IN YOUR {count} CHANCE!!")
        elif inp.lower() == "khat507":
            print(word)
        elif len(inp) == len(word) and inp.lower() != word:
        
            for i,v in enumerate(inp):
                if word[i] == v:
                    print(f"{v} is at the right place!")
                elif v in word:
                    print(f"{v} is not at the correct place but present in the answer!")
                else:
                    print(f"{v} is not present!")
            count+=1
            inpt(count)
        elif len(inp) > len(word):
            print("The word is too long!")
            print(f"The length of the answer is {len(word)}")
            count+=1
            inpt(count)
        elif len(inp) < len(word):
            print("The word is too short!")
            print(f"The length of the answer is {len(word)}")
            count+=1
            inpt(count)

    print("Hey welcome to khat's WORDLE!")
    print("You have to guess the word of length 5")
    print("Good Luck!")
    inpt(count)

if __name__ == "__main__":

    try:
        process()

    except ValueError:
        print("You are giving an invalid value type!")

    except Exception as E:
        print(E)
