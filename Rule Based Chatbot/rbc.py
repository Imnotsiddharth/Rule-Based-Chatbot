def chat():
    print("Welcome to Siddharth's Chatbot!")
    name = input("What's your name? ")
    print("Nice to meet you,", name, "\n")
    
    while True:
        help()
        choice = input("->")
        if choice.lower() == "recommend":
            recommend()
        elif choice.lower() == "pack":
            pack()
        elif choice.lower() == "joke":
            joke()
        elif choice.lower() == "exit":
            print("Okay")
            break
        else:
            print("Please enter one of the 3\n")

def recommend():
    print("Mountains/Plains/Neither\n")
    rec = input("->").lower()
    if rec == "mountains":
        print("Cool. No pun intended. What about the Himalayas?")
        him = input("->")
        if him == "no":
            print("Hmm. I won't be of much help then.")
            return
        elif him == "yes":
            print("Great! Want packing suggestions?")
            ps = input("->")
            if ps == "yes":
                pack()
            else:
                return
    elif rec.lower() == "plains":
        print("Plains.")
    
    elif rec.lower() == "neither":
        return


def joke():
    print("Why don't scientists trust atoms? Because they make up everything! Ha!")
    print("Want another?")
    j = input("->")
    if j.lower() == "yes":
        print("Why did the man put his watch in the safe? He wanted to save time.")
    elif j.lower() == "no":
        print("No worries.")

def pack():
    print("1. Plan It Out.")  
    print("2. Choose the Right Luggage and Know Your Airline’s Baggage Policy.") 
    print("3. Carry Essentials + One Outfit in Your Carry-On Bag..") 
    print("4. Coordinate Your Outfits for Maximum Versatility.") 
    print("5. Layering Is Key.")   



def help():
    print("What do you want help with?\n")
    print("Travel Recommendations\nPacking Suggestions\nJoke\nExit\n")
    

if __name__ == "__main__":

    chat()