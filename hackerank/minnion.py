VOWELS=['A','E','I','O','U']



def minion_game(string):

    # your code goes here
    size = len(string)
    kevin=stuart=0
    for x in range(size):
        letter=string[x]
        if letter in VOWELS:
           kevin+=size-x 
        else:
           stuart+=size-x
      
    if kevin < stuart:
        print ("Stuart",stuart)
    if kevin > stuart:    
        print ("Kevin",kevin)
    if kevin == stuart:    
        print ("Draw")
        

           
if __name__ == '__main__':
    s = input()
    minion_game(s)