import random

print("Generate random numbers")

answer = 0


for times in range(10):
  user_random1 = random.randint(1, 10)
  user_random2 = random.randint(1, 20)
 
question = int(input(f"Please Enter the answer to the problem  {times + 1} {user_random1}2-{user_random2}: "))
if question == question: 
   print("Yes correct")
else:
  print("Not Correct")
answer += question