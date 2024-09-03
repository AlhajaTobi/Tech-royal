"""
 get the number of people ordering
store as number_of_people
store the differnt types of pizza
get slices per box 
get the total of boxes needed.
get the slices total
get leftover 
get the totalcost

"""

import math

def main():

         number_of_people = int(input("Enter number of people ordering for:  "))

         print("Enter the pizza type: \n Sapa, \n Small Money,\n Big Boys, \n Odogwu:")
         pizza_type = input().strip()

	slices_per_box = 0
        price_per_box  = 0
	
  	if  pizza-type == "Sapa":
            slices_per_box = 4
            price_per_box = 2000
      elif   pizza_type == "Small Money":
	     slices_per_box = 6
             price_per_box  = 2400
       elif  pizza_type == "Big Boys":
             slices_per_box = 8
             price_per_box = 3000
 	elif pizza_type =="odogwu":
             slices_per_box = 12
             price_per_box = 4200
     	else:
 	     print("Invalid pizza type order")
             return

	pizza_boxes_needed = math.celi(number_of_people / slices_per_box)
	total_slices = pizza_boxes_needed * slices_per_box
	leftover_slices = total_slices - number_of_people
	total_cost = pizza_boxes_needed * price_per_box

	
	print("Number of boxes of pizza to buy", pizza_boxes_needed)
	print("Number of leftover slices", leftover_slices)
	print("Total cost: NGN", total_cost)


pizza_order()
   
