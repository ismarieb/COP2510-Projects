##Assignment 4
##Pair 32


##While not assigned, rank_to_value(card_rank) otherwise appears twice and is
##long, so it makes the code /a little bit/ cleaner to make a new function for
##it instead.

def rank_to_value(card_rank):
    if card_rank == "T":
        ans = 10
    elif card_rank == "J":
        ans = 11
    elif card_rank == "Q":
        ans = 12
    elif card_rank == "K":
        ans = 13
    elif card_rank == "A":
        ans = 14
    else:
        ans = int(card_rank)
    return ans


    


##Problem 1

##Driver: Ismarie Birriel
##Navigator: Kyle "Brick" Townsend

##Write a function is_flush that accepts a list of 5 cards and returns
##(True or False) whether all of the cards have the same suit.  Each card in
##the input will be represented as a two-character string.  The first
##character will be the rank:  'T' (Ten), 'J' (Jack), 'Q' (Queen), 'K' (King),
##'A' (Ace), or a digit 2-9.  The second character will be the suit:
##'S' (Spades), 'H' (Hearts), 'C' (Clubs), or 'D' (Diamonds).

def is_flush(hand):
    ans = True
    suit_flush = (hand[0])[1:]
    for x in hand:
        if x[1:] != suit_flush:
            ans = False
            break
    return ans



##Problem 2

##Driver: Kyle "Brick" Townsend
##Navigator: Ismarie Birriel

##Write a function high_card that accepts a list of 5 cards and returns the
##rank of the high card.  Cards will be specified the same way as in Problem 1.
##When deciding the high card, only the card rank matters:  Ace is the highest,
##followed by King, Queen, Jack, Ten, then the numbers 9 down to 2, in that
##order.  The high_card function should return the rank of the highest card
##(2-9, T, J, Q, K, or A).

def high_card(hand):
    ans = 0
    rank_temp = 0
    for x in hand:
        rank_temp = rank_to_value(x[:1])
        if rank_temp > ans:
            ans = rank_temp
    if ans == 10:
        ans = "T"
    elif ans == 11:
        ans = "J"
    elif ans == 12:
        ans = "Q"
    elif ans == 13:
        ans = "K"
    elif ans == 14:
        ans = "A"
    else:
        ans = int(ans)
    return ans


##Problem 3

##Driver: Ismarie Birriel
##Navigator: Kyle "Brick" Townsend

##Write a function is_straight that takes in a list of 5 cards and returns
##whether the ranks of the cards form a straight.  Cards will be specified the
##same way as in Problem 1.
##
##A straight is a set of cards in which the card ranks are consecutive.  Card
##ranks go from 2 to 9, then Ten, Jack, Queen, and King.  The Ace can count as
##the highest rank or the lowest rank when determining a straight.  Suit is
##irrelevant when determining whether the cards form a straight.
##
##Hint:  start by finding the high card, then determine if the next 4 lower
##ranks are present.  If the high card is an Ace, check whether the other
##ranks are King, Queen, Jack, and Ten OR 2, 3, 4, and 5.

def is_straight(hand):
    high = high_card(hand)
    rank_high = rank_to_value(high)
    ace_low = False
    if high == "A":
        ace_low_val = 1
        one_more = False
        two_more = False
        thr_more = False
        fou_more = False
        for x in hand:
            rank_temp = rank_to_value(x[:1])
            if rank_temp == (ace_low_val + 1):
                one_more =True
            if rank_temp == (ace_low_val + 2):
                two_more =True
            if rank_temp == (ace_low_val + 3):
                thr_more =True
            if rank_temp == (ace_low_val + 4):
                fou_more =True
        if one_more and two_more and thr_more and fou_more:
            ans = True
            ace_low = True
        else:
            ace_low = False
    if not ace_low: 
        one_less = False
        two_less = False
        thr_less = False
        fou_less = False
        for x in hand:
            rank_temp = rank_to_value(x[:1])
            if rank_temp == (rank_high - 1):
                one_less =True
            if rank_temp == (rank_high - 2):
                two_less =True
            if rank_temp == (rank_high - 3):
                thr_less =True
            if rank_temp == (rank_high - 4):
                fou_less =True
        if one_less and two_less and thr_less and fou_less:
            ans = True
        else:
            ans = False
    return ans

    


##Problem 4

##Driver: Kyle "Brick" Townsend
##Navigator: Ismarie Birriel

##Write a function max_of_a_kind that takes a list of 5 cards and returns the
##rank of the card that appears most frequently.  If there is a tie (two pairs
##or all five cards different), you should return the rank of the highest tied
##card (Ace high, followed by King, Queen, Jack, Ten, then 9 down to 2).  The
##suit is irrelevant to determining the max_of_a_kind.

##Hint:  you may wish to create a dictionary that counts how many times each
##rank appears.

def max_of_a_kind(hand):
    num_appearances = {"2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0, "T":0, "J":0, "Q":0, "K":0, "A":0}
    for card in hand:
        for key,val in num_appearances.items():
            if card[:1] == key:
                num_appearances[key] += 1
    max_val = 0
    for key,val in num_appearances.items():
        if val >= max_val:
            max_val = val
            ans = key
    return ans


'''
##Tests for P1
test = ['TS', 'JS', 'QS', 'KS', 'AS']
print("Output: " + str(is_flush(test)))##True
test = ['3H', '7H', 'QH', '9S', 'TH']
print("Output: " + str(is_flush(test)))##False

##Tests for P2
test = ['TS', 'JS', 'QS', 'KS', 'AS']
print("\nOutput: " + str(high_card(test)))##A
test = ['2H', '4C', '8D', '6H', '4S']
print("Output: " + str(high_card(test)))##8
test = ['9C', 'TD', 'TH', 'QS', 'QH']
print("Output: " + str(high_card(test)))##Q

##Tests for P3
test = ['TS', 'JS', 'QS', 'KS', 'AS']
print("\nOutput: " + str(is_straight(test)))##True
test = ['JS', 'KS', 'AS', 'QS', 'TS']
print("Output: " + str(is_straight(test)))##True
test = ['4H', '5S', '6D', '8D', '9H']
print("Output: " + str(is_straight(test)))##False
test = ['3C', '2D', '4C', 'AD', '5C']
print("Output: " + str(is_straight(test)))##True

##Tests for P4
test = ['2C', '2S', '2D', '2H', 'AD']
print("\nOutput: " + str(max_of_a_kind(test)))##2
test = ['3H', '8H', '6C', '9C', '6S']
print("Output: " + str(max_of_a_kind(test)))##6
test = ['TS', 'JS', 'QS', 'KS', 'AS']
print("Output: " + str(max_of_a_kind(test)))##A
test = ['QH', '9H', 'JH', 'JC', 'QD']
print("Output: " + str(max_of_a_kind(test)))##Q
'''
