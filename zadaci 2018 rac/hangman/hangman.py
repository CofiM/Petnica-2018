
name = raw_input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
word = "alfabet"
guess = raw_input
turns = 10
correct = 0
failed = 0
kraj = False

while not kraj       
             
 
    for char in word:      

        if char in guesses:    
    
            print(char),

            correct += 1

        else:
    
            print(_),     
       
            failed += 1    




    if failed == 6:        
        print("You losed")
        kraj = True
    if correct == len(word):
        print(word)
        print("You won")
        kraj = True
    #