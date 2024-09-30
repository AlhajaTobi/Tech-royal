def maximum(firstnumber, secondnumber, thirdnumber):

	if firstnumber >= secondnumber and firstnumber >= thirdnumber:
		return firstnumber
	elif secondnumber >= firstnumber and secondnumber >= thirdnumber:
		return secondnumber 
	else:
		return thirdnumber


	
print(maximum(-5,20,50))



