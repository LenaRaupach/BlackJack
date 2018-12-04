import Chips
import Deck
import Hand


'''
Black Jack card game. 
3. Oktober 2018
'''

__author__ = 'Lena Raupach'


def take_bet():
    while True:
        try:
            bet = str(int(input("What is your bet? ")))
            if int(bet) > chips.total:
                print("\nYou just have " + str(chips.total) + " chips. ")
                continue
            print("Thanks! Your bet is " + bet + ".")
            break
        except ValueError:
            print("Error, enter an integer! Try again! \n")
    return bet


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)


def player_wins():
    if 21 - hand.value < 21 - handDealer.value:
        print("____________________________________________________________________")
        print("CONGRATULATIONS, YOU WON!")
        print("____________________________________________________________________")
        return True


def both_win():
    if hand.value == handDealer.value:
        return True


def hit_or_stand(deck, hand):
    global playing
    des = "None"
    while des.lower() != 'hit' and des.lower() != 'stand':
        des = input("Hit or Stand? ").lower()
    if des == "hit":
        hit(deck, hand)
    elif des == "stand":
        if player_wins() == True:
            chips.win_bet()
        elif both_win():
            print("____________________________________________________________________")
            print("IT'S A DRAW! NOBODY GETS A CHIP.")
            print("____________________________________________________________________")
        else:
            print("____________________________________________________________________")
            print("YOU LOSE! ")
            print("____________________________________________________________________")
            chips.lose_bet()
        playing = False


def alterPlayer(player):
    if player == 'player':
        return 'dealer'
    elif player == 'dealer':
        return 'player'
    else:
        print("ERROR: alterPlayer() gets wrong name.\n")

def show_some(hand_dealer, hand_player):
    print("\nDealer: " + str(["***Hidden***"] + hand_dealer.cards[1:]))
    print("Player: " + str(hand_player) + '\n')

def show_all(hand_dealer, hand_player):
    print("\nAll of Dealer: " + str(hand_dealer))
    print("All of Player: " + str(hand_player) + '\n')


'''
End of game scenarios.
'''
def player_busts():
    if hand.value > 21:
        print("____________________________________________________________________")
        print("SORRY, YOU BUSTED! ")
        print("____________________________________________________________________")
        return True
    else:
        return False

def dealer_busts():
    if handDealer.value > 21:
        print("____________________________________________________________________")
        print("THE DEALER BUSTED! YOU WON!")
        print("____________________________________________________________________")
        return True





if __name__ == "__main__":
    chips = Chips.Chips()

    while True:
        deck = Deck.Deck()
        deck.shuffle()
        hand = Hand.Hand()
        handDealer = Hand.Hand()
        playing = True

        print("\nWelcome to Blackjack! \n"
              "Notice that the first card of the dealer is hidden. \nGood Luck! \n")

        chips.bet = take_bet()
        hand.add_card(deck.deal())
        hand.add_card(deck.deal())
        handDealer.add_card(deck.deal())
        handDealer.add_card(deck.deal())
        if hand.value == 21:
            print("____________________________________________________________________")
            print("BLACK JACK! YOU WON!")
            print("____________________________________________________________________")
            chips.win_bet()
            playing = False
        elif handDealer.value == 21:
            print("____________________________________________________________________")
            print("DEALER GOT A BLACK JACK! YOU LOSE!")
            print("____________________________________________________________________")
            chips.lose_bet()
            playing = False


        show_some(handDealer, hand)

        while playing:
            hit_or_stand(deck, hand)

            if playing == False: break

            if player_busts():
                chips.lose_bet()
                playing = False
                break

            if handDealer.value < 17:
                hit(deck, handDealer)
                if dealer_busts():
                    chips.win_bet()
                    playing = False
                    break
            show_some(handDealer, hand)

        show_all(handDealer, hand)
        print("Dealer's value: \t" + str(handDealer.value))
        print("Your value: \t" + str(hand.value))
        print("Your total: ")
        chips.print_total()
        if chips.total == 0:
            print("____________________________________________________________________")
            print("YOUR CHIPS ARE EMPTY")
            print("____________________________________________________________________")
            break
        play_again = input("Play again? Enter yes or no. ")
        if play_again.lower() == 'yes':
            print("\n\nWell, then play again! \n")
            continue
        while play_again.lower() != 'no':
            play_again = input("\nPlay again? Yes or No?\n")
            if play_again == 'yes':
                print("\n\nWell, then play again! \n")
                continue
        else:
            break
