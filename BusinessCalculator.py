print("\n\n BUSINESS CALCULATOR MENU")
choose = input(" 1] Simple Interest \n 2] Compound Interest \n 3] Exit \n Choose [1/2/3]")

if choose == '1':
    principal = float(input("Enter Principal Amount:"))
    interest_rate = float(input("Enter Interest Rate: "))
    time = float(input("Enter Time (in years): "))
    interest = principal * interest_rate * time
    print("Interest=", interest)

elif choose == '2':
     principal = float(input("Enter Principal Amount:"))
     interest_rate = float(input("Enter Interest Rate: "))
     time_in_years = float(input("Enter Time (in years): "))
     compound_interest = principal * pow((1+(interest_rate/100)),time_in_years)
     print("Compound Interest=", compound_interest)

else:
     print("Invalid choice. Please select a valid option.")

    