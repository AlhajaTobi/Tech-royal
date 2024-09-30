scores = [12,40,30,50,67,10,94]
print("string address after declearation", id(scores))
scores[0]
scores[1] = 80
print(scores[1])
print(scores[0])
print(len(scores))
print("string address after modification", id(scores))

name = "jesse"
print("name address after declaration", id(name))

name += "akarele"
print("name address after modification", id(name))

additional_scores =[12,49,10]
print(scores + additional_scores)
print(scores)
for index in range(len(scores)):
	scores[index] += 10
print(scores)
 #print(scores*3)
print(scores [-1])
reverse_list = []
'''
for index in range(len(scores) -1 , 0, -1):
	reverse_list += [scores[index]]
'''
#reverse_list = scores[::-1]

#print(reverse_list)

scores.append(20)
print(scores)

scores.extend([5,6,7,8])
print(scores)
scores.insert(2,69)
print(scores)