import random 
count =1
while count <= 10:
       
	random_user1 = random.randrange(1 , 10)
	random_user2 = random.randrange(1,  10)
	print (int(random_user1),(random_user2))


user_answer = int(input(" "))
answer_check = random_user1- random_user2

if user_answer == answer_check:
	print("Yes")
if user_answer != answer_check:
	print("No")
count+=1
print(f(final_score))



