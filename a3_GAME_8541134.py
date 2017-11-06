# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.
#Name(First,Last): Peter Farah 
# Student number: 8541134
# Course: IT1 1120 
# Assignment Number 3 Part B

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]
     

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     for i in range(0,len(deck),2):
        dealer.append(deck[i])
     for j in range (1,len(deck),2):
        other.append(deck[j])

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    pairs=[]
    counter = 0
    a=sorted(l)
    if a[0][0]==a[1][0] and len(a)==2:
        no_pairs=[]
        return no_pairs
    for i in range(len(a)-3):
        if a[i][0]==a[i+1][0] and  a[i][0]==a[i+2][0] and a[i][0]==a[i+3][0]:
              pairs.append(a[i])
              pairs.append(a[i+1])
              pairs.append(a[i+2])
              pairs.append(a[i+3])
        elif a[i][0]==a[i+1][0] and  a[i][0]!=a[i+2][0]:
              pairs.append(a[i])
              pairs.append(a[i+1])
        if a[-3][0]==a[-2][0]:
            pairs.append(a[-3])
            pairs.append(a[-2])  
        elif a[-2][0]==a[-1][0]:
            pairs.append(a[-1])
            pairs.append(a[-2])
    
        
    pairs=sorted(pairs)
    no_pairs=list((set(l)-set(pairs)))
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    print(' '.join(deck))

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     
     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     x=int(input("Give me an integer between 1 and "+str(n)+':'))
     while x>n or x<1:
        x=int(input("Invalid number. Please enter integer between 1 and "+str(n)+':'))
        ##TRY AND EXCEPT ValueError
     return x

    
def numbers_player_taking(x):#,dealer):
    '''(int)-> None
    This function accepts a value x that is >0 and prints the correct suffix of the
    number chosen(st,nd,rd,th). This is the robot
    speaking during the players turn.
    This specific function deals with cards so it will display:
    ex:
    x=1 "You asked for my 1st card"
    x=2 "You asked for my 2nd card"...

    '''
    #la=len(dealer)
    if x==1:
        print("You asked for my 1st card")
    elif x==2:
        print("You asked for my 2nd card")
    elif x==3:
        print("You asked for my 3rd card")
    elif x>4:
        print("You asked for my "+str(x)+"th card")
def numbers_dealer_taking(x):#,dealer):
        '''(int)-> None
    This function accepts a value x that is >0 and prints the correct suffix of the
    number chosen(st,nd,rd,th). This is the robot
    speaking during its turn.
    This specific function deals with cards so it will display:
    ex:
    x=1 "You asked for my 1st card"
    x=2 "You asked for my 2nd card"...'''
        if x==1:
            print("I took your 1st card")
        elif x==2:
            print("I took your 2nd card")
        elif x==3:
            print("I took your 3rd card")
        elif x>4:
            print("I took your "+str(x)+"th card")
def player_turn(human,dealer):
    '''(list of string,list of string)-> list of string
    This is the main function for the players turn. It plays the players turn while calling
    other functions related to the game. It accepts lists of strings in this case the
    humans cards in list format and the dealers cards in list format.
    It plays the game and returns a new list of cards removing any pairs and shuffling.
    '''
    
    print("******************")
    print("Your turn")
    print("Your current deck of cards is:")
    a=print_deck(human)
    print('I have '+str(len(dealer))+' cards. If 1 stands for my first card and '+
    str(len(dealer))+' stands for my last card,\nwhich of my cards would you like?')
    x=get_valid_input(len(dealer))
    numbers_player_taking(x)#,dealer)
    x=x-1#If x is 1 for example, it will take index 0 in the list
    print('\n')
    print("Here it is. It is "+dealer[x])
    print('\n')
    print("With the "+dealer[x]+" added, your current deck of cards is:")
    print('\n')
    human.append(dealer[x])
    dealer.pop(x)
    print_deck(human)
    print('\n')
    print("And after discarding pairs and shuffling, your deck is:")
    print('\n')
    human=remove_pairs(human)
    random.shuffle(human)
    print_deck(human)
    return(human)
    

def dealer_turn(dealer,human):
    '''(list of string,list of string)-> list of string
    This is the main function for the dealers turn. It plays the dealers turn while calling
    other functions related to the game. It accepts lists of strings in this case the
    dealers cards in list format and the humans cards in list format.
    It plays the game and returns a new list of cards removing any pairs and shuffling.
    '''
    print("******************")
    print("My turn.")
    x=random.randint(1,len(human))
    numbers_dealer_taking(x)#,human)
    x=x-1#If x is 1 for example, it will take index 0 in the list
    dealer.append(human[x])
    human.pop(x)
    dealer=remove_pairs(dealer)
    random.shuffle(dealer)
    return(dealer)
    wait_for_player()
    
def play_game():
    '''()->None
    This function plays the game'''

    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)

    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
     
    dealer=remove_pairs(dealer)
    human=remove_pairs(human)
     
    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE
    
    while len(human)!=1 and len(dealer)!=1:
        human= player_turn(human,dealer)
        wait_for_player()
        dealer= dealer_turn(dealer,human)
        wait_for_player()

    
    while len(dealer)>=1:
        
            if len(dealer)==2:
                human= player_turn(human,dealer)
                if len(human)==0:
                    break
                
                    
            elif len(dealer)==1:
                dealer = dealer_turn(dealer,human)
                if len(dealer)==0:
                    break


    if len(human)==0:
        print("Ups. You do not have any more cards\nCongratulations! You, Human, win !")
    else:
        print("Ups. I do not have any more cards\nYou lost! I, Robot, win !")
                
                
# main
play_game()
