### This exercise uses Python lists to create medical records

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# add one person
insurance_costs.append(8320.0)
names.append("Priscilla")

#combine the lists
medical_records = list(zip(insurance_costs,names))

  print(list(medical_records))

#check how many records there are
num_medical_records = len(medical_records)

  print("There are " +  str(num_medical_records) + " medical records.")

#what is the first record
first_medical_record = medical_records[:1]
    print("Here is the first medical record: " + str(first_medical_record))

#sort records by costs
medical_records.sort()
  print("Here are the medical records sorted by insurance cost: " + str(medical_records))

#who have the cheapest and priciest three costs
cheapest_three = list(medical_records[:3])
  print(cheapest_three)

priciest_three = list(medical_records[-3:])
  print(priciest_three)

#how many times does the name Paul occurr
occurrences_paul = names.count("Paul")
  print(occurrences_paul)

#get the middle five records
middle_five_records = list(medical_records[3:8])
  print(middle_five_records)
