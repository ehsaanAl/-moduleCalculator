print("------ WELCOME ------")

proTally = 0 
trailerTally = 0 
retriTally = 0 
excludeTally = 0 


def main():
    
        credRange = [0, 20, 40, 60, 80, 100, 120]                      # The range is set to go up in 20s

        global proTally                                                # I have globalised the variables so they can be used inside and outside the loop
        global trailerTally 
        global retriTally  
        global excludeTally 
 
        while True: 
            try:
                passmark = int(input("\nPlease enter your credits at pass: ")) # Input pass credits
                defermark = int(input("\nPlease enter your credits at defer: ")) # Input defer credits
                failmark = int(input("\nPlease enter your credits at fail: ")) # Input fail credits

                totalMarks = passmark + defermark + failmark
            except ValueError:
                print("\nNot gonna lie to you, I'm gonna need an integer here bro")
                continue                                # Continue used here to loop  the program after 'integer required' statement is printed 
            break

        if passmark not in credRange:
            print ("\nSomething within range por favor")

        elif totalMarks != 120: 
            print ("\nThis doesn't even sum to 120, fix up bro?!?")

        elif passmark == 120:                           # if passmark equals 120, then 1 is added to the 'progress' tally
            print ("\nProgress")
            proTally += 1 
            global proList
            proList = [passmark, defermark, failmark]

        elif passmark == 100:
            print ("\nProgress (Module trailer)")                           # If passmark equals to 100 and the defer or fail mark equals 20, then 1 is added to the 'module trailer' tally
            trailerTally += 1 
            global trailList
            trailList = [passmark, defermark, failmark]

        if passmark <= 80 and passmark >= 0 and failmark < 80:              # If passmark is less than or equal to 80 and greater than or equal to 0 and failmark is less than 80, then 1 is added to the 'retri' tally
            print ("\nDo not progress - module retriever")
            retriTally += 1
            global retriList 
            retriList = [passmark, defermark, failmark]

        elif failmark >= 80:                                                # If failmark is greater than or equal to 80, then 1 is addded to the exclude tally 
            print ("\nExclude")
            excludeTally += 1 
            global excludeList
            excludeList = [passmark, defermark, failmark]

main()                                                                      # The defined function is called again here to signify the loop 
  

while True:                                                                 # After the user has inputted values and the outcomes are returned in the terminal, the user is promted to enter either y or q 

    userInput = input("\nWanna enter another set? (y/q):  ")
    
    if userInput == 'y':   
        main()
        continue
    else:
        userInput == 'q'
        print ("\nSee you soon! ;) \n\n")
    break

print("---------------------\n")

print("Horizantal Histogram\n\n")                                           # When 'q' is entered, the program ends and the horizontal histogram is displayed with results
print("Progress : ", proTally*"*")
print("Trailer : ", trailerTally*"*")
print("Retriever : ", retriTally*"*")
print("Exclude: ", excludeTally*"*")
print("\n", proTally + trailerTally + retriTally + excludeTally, " outcomes in total")                  # The histogram also displays the total outcomes 


1
stars = [proTally,trailerTally,retriTally,excludeTally]
maxval = max(stars)                                                     # Lines 88 to 97: https://stackoverflow.com/questions/64938921/is-it-possible-to-put-the-results-of-these-for-loops-into-one-line

print('---------------------\n')
print("Vertical Histogram\n")

choices = 'Progress | Trailer | Retriever | Exclude'
print(choices)
for i in range (maxval):
    a = ['*' if i < star else ' ' for star in stars]
    print (f'{a[0]:>4}{a[1]:>11}{a[2]:>11}{a[3]:>11}')

print('---------------------\n')

print("Progress: ", proList)                                                   # A list of the scores entered are also displayed 
print("Module Trailer: ", trailList)
print("Module Retriever: ", retriList)
print("Excluded: ", excludeList)


