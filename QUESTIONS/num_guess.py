import random as r
rand_num = r.randrange(1,20) # Generating a random number between 1 and 19 print("Number to be guessed: ",rand_num)
print("Number to be guessed: ", rand_num)
i = 1
while True:
   print("Number Guessed: ",i)
   if(i == rand_num): # If the number guessed is correct the this block will be executed
     print("Random Number has been guessed successfully!")
     break # Break statements stops and exits from the Loop
   i += 1
print("End of the program...")