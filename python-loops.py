##In this project, you will use your new knowledge of Python loops to iterate through and analyze medical insurance cost data.

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# add costs into one sum

total_cost = 0

for cost in actual_insurance_costs:
  total_cost += cost
  
  print(total_cost)

# calculate average insurance cost

average_cost = total_cost/len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

#print out the cost for each person and see if its below,above or equal to average

for i in range(len(names)):
 name = names[i]
 insurance_cost = actual_insurance_costs[i] 
 print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")   
 if insurance_cost > average_cost:
   print("The insurance cost for " + name + " is above average.")
 elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is below average.")
 else:
   print("The insurance cost for " + name + " is equal to the average.") 

updated_estimated_costs = [cost*11/10 for cost in estimated_insurance_costs]
print(updated_estimated_costs)

