def hit():
    ''' Implement the hit button '''
    global playing,chip_pool,deck,player_hand,dealer_hand,result,bet
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        print "Player hand is %s" %player_hand
        if player_hand.calc_val() > 21:
            result = 'Busted! '+restart_phrase
            chip_pool -=bet
            playing =False
    else:
        result = "Sorry, can't hit" + restart_phrase
    game_step()
def stand():
    global playing,chip_pool,deck,player_hand,dealer_hand,result,bet
    ''' This function will now play the dealers hand, since stand was chosen '''
    
    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand!"
            
    # Now go through all the other possible options
    else:
        
        # Soft 17 rule
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())
            
        # Dealer Busts    
        if dealer_hand.calc_val() > 21:
            result = 'Dealer busts! You win!' + restart_phrase
            chip_pool += bet
            playing = False
            
        #Player has better hand than dealer
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'You beat the dealer, you win!' + restart_phrase
            chip_pool += bet
            playing = False
        
        # Push
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'Tied up, push!' + restart_phrase
            playing = False
        
        # Dealer beats player
        else:
            result = 'Dealer Wins!' + restart_phrase
            chip_pool -= bet
            playing = False
    game_step()
def game_step():
    'Function to print game step/status on output'
    
    #Display Player Hand
    print ""
    print('Player Hand is: '),
    player_hand.draw(hidden =False)
    
    print 'Player hand total is: '+str(player_hand.calc_val())
    
    #Display Dealer Hand
    print('Dealer Hand is: '),
    dealer_hand.draw(hidden=True)
    
    # If game round is over
    if playing == False:
        print  " --- for a total of " + str(dealer_hand.calc_val() )
        print "Chip Total: " + str(chip_pool)
    # Otherwise, don't know the second card yet
    else: 
        print " with another card hidden upside down"
    
    # Print result of hit or stand.
    print result
    
    player_input()
