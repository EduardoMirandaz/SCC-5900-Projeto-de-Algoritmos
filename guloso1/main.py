pots_amount, competitors_amount = [int(i) for i in input().split()]

while pots_amount + competitors_amount != 0:

    pots = []
    competitors = []

    for i in range(pots_amount):
        pots.append(int(input()))

    for j in range(competitors_amount):
        competitors.append(int(input()))

    pots.sort(reverse=True)
    competitors.sort(reverse=True)


    heights_sum = 0
    last_pot_index = -1
    
    while pots:
        if competitors:
            c = competitors.pop() # gets the smallest competitor height
            if c >= pots[last_pot_index]: # if their height is higher or equal to the diameter of the smallest pot, we breaks it
                heights_sum += c
                pots.pop() # < BoOom >, the pot explodes exactly here! 
        else:
            print('no') # if we still have pots, but no more competitors, we print "no" (./pernalonga.png)
            break
    else: # if the loop ended "without an interruption", we were able to break all the pots! 
        print(heights_sum)

    
    pots_amount, competitors_amount = [int(i) for i in input().split()]




