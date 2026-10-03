import random
#variables
run = 0
card = 0
cardsum = 0
wins = 0
losses = 0
overallresult = 0
nextcard = 0
cardshand = []
cardsnum = []

def createdeck():
    global deck, cardslist,suits
    ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    deck.append("⭐ Star Card⭐")
    deck.append("⭐ Star Card⭐")
    random.shuffle(deck)
def getcardvalue(cardsum,card):
    if "Jack" in card or "Queen" in card or "King" in card:
        return 10
    elif "Ace" in card:
        if cardsum + 11 >21:
            return 1 
        return 11
    elif card =="⭐ Star Card⭐":
        return 0
    else:
        ranknumber = card.split()[0]
        return int(ranknumber)
def getcard():
    global cardsum, cardshand, cardsnum, nextcard, card
    nextcard = 0
    card = deck.pop()
    cardshand.append(card) 
    cardsnum.append(getcardvalue(cardsum, card))
    print(f"Your cards are {', '.join(cardshand)}")
    cardsum = sum(cardsnum)

print("         ♠️ ♥️  -Welcome to Blackjack!-♦️ ♣️ ")
startmenu = input("What do you want to do?(P to play/H for help): ")
if startmenu.lower() in ["h", "help"]:
    print("""               📖 -HELP-📖\n
In blackjack, the aim of the game is to get the sum of your \n
cards to as near to 21 as possible without going over 21.\n
            🎮 -HOW TO PLAY-🎮\n
You and the dealer both receive two cards. The dealer flips \n
one of theirs over and the game begins. On each turn, you can \n
choose to hit, which means you draw a card, or stand, which \n
means you stick with your current total. After you stand, the \n
dealer flips their other card over and then draws cards until \n
they reach 17, at which they must stand.\n
              🔢 -CARD VALUES-🔢\n
In blackjack, Kings, Queens and Jacks are all worth 10, and Aces \n
are worth either 1 or 11, depending on whether an 11 makes you bust.\n
          👑 -HOW TO WIN(or lose 😭)-👑\n
If your total is more than the dealers at the end of the game, \n
you win. Likewise, if the dealers total is more, they win. \n
If either you or the dealers total exceeds 21, you are bust \n
and must show your cards to the other person. If you or the \n
dealer get 21 on your first two cards, you get blackjack and \n
you immediately win and start a new game.\n
         ✨ -oh look theres a new card-✨\n
In this version of blackjack, there is also a card called the \n
star card. There are only 2 in the deck and if you get one you\n
get to look at your next card!
""")
elif startmenu.lower() in ["p", "play"]:
    run = 1
    while run==1:
        createdeck()
        for i in range(2):
            getcard()
        if cardsum == 21:
            print("🎉Blackjack! You win!🎉")
            wins += 1
            run = 0
            break
        elif cardsum > 21:
            print("💥Bust! Dealer wins!")
            losses += 1
            run = 0
            break
        while True:
            hitstand = input("Do you want to hit or stand?(H/S)").lower()
            if hitstand == "h" or hitstand == "hit":
                getcard()
            if card == "⭐ Star Card⭐":
                nextcard = deck[-1]
                print("You drew a Star Card! The next card in the deck is", nextcard)
            if cardsum == 21:
                    print("🎉Blackjack! You win!🎉")
                    wins += 1
                    break
            elif cardsum > 21:
                print("💥Bust! Dealer wins!")
                losses += 1
                break
            if hitstand == "s" or hitstand =="stand":
                print("Your total score is", cardsum)
                run = 0
                break