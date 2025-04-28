import random
randnumber=random.randint(1, 100)
#print(randnumber) 
userguess = None
guesses = 0  

while(userguess != randnumber):
      userguess = int(input("enter your guess:"))
      guesses += 1
      if(userguess==randnumber):
          print("you guessesd right")
      else:
           if(userguess>randnumber):
              print("enter a larger num")
           else:
              print("enter the smaller number")    
    
        
print(f"you guesed the number {guesses} guessses") 
with open("highscore.txt","r") as f:   
    hiscore = (f.read())  

if(guesses<hiscore):
    print("you broke highscore")        
with open("highscore.txt","w") as f:
    f.write(str(guesses))