import random 

answer = random.randint(1,20)
print ("I'm guessing a number from 1 to 20.")

count = 0

while(True):
  count = count + 1
  print("Can you guess it?")
  prediction = int(input())
  if prediction > answer: 
    print('The answer is too high. ')
  elif prediction < answer:
    print('The answer is too low. ')
  else: 
    print('It is correct!')
    break

print("you have attempted " + str(count) + " times. ") 
