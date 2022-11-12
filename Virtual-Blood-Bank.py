print("The blood types are A+, A-, O+, O-, B+, B-, AB+, Ab-")

# Blood groups. There are 8 blood groups
bg=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
#blood reciving rule
brr={"A+":["A+","A-","O+","O-"],
     "O+":["O+","O-"],
     "B+":["B+","B-","O-","O+"],
     "AB+":["A+","A-","B+","B-","O+","O-","AB+","AB-"],
     "A-":["A-,O-"],
     "O-":["O-"],
     "B-":["B-","O-"],
     "AB-":["AB-","A-","B-","O-"]}
#blood info
bgI={"A+":[12.500,"2/7/23"],
     "O+":[11.300,"3/4/23"],
     "O-":[14.347,"6/1/23"],
     "B+":[12.500,"5/7/23"],
     "AB+":[10.350,"4/9/23"],
     "A-":[14.523,"6/12/23"],
     "B-":[12.567,"5/8/23"],
     "AB-":[14.324,"3/6/23"]}

while True:

     print("1 -> Donate")
     print("2 -> Use")
     print("3 -> Blood Information")
     print("4 -> Exit the program")
     option=input("Enter options 1,2,3, or 4:")
     if(option=="1"):
          blood_type=input("What type of blood are you donatating:  ")
          blood_quantity=float(input("How many liters of that type of blood are you donating? "))

          bgI[blood_type][0]+=blood_quantity
          print("The",blood_type,"has been increased by",blood_quantity,".")
          print("Thank you for donating")
     elif(option=="2"):
          btP=input("What is blood type of the patient that you are giving blood to:")
          print("These are the possible blood groups the patient can recieve")
          print(brr[btP])
          blood_type=input("what type of blood would you like to use:")
          blood_quantity=float(input(f"How much of {blood_type} would you like to use:"))
          if(blood_quantity>bgI[blood_type][0]):
               print("There is not enough blood in the blood bank for the amount of blood you need")
          else:
               bgI[blood_type][0]-=blood_quantity
               print("The",blood_type,"has been decreased by",blood_quantity,".")
               print("The patient recieved the blood")
               
     elif ( option == "3"):
          for i in bgI.keys():
               print(i , bgI[i])

     elif ( option == '4'):
          break

     else:
          print("Invalid input")