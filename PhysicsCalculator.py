print("\n\n PHYSICS CALCULATOR MENU")
choose = input(" 1] Force \n 2] Momentum \n 3] Velocity \n 4] Acceleration \n 5] Exit \n Choose [1/2/3/4/5]\n")

if choose == '1':
    mass = float(input("Enter Mass: "))
    acceleration = float(input("Enter Acceleration: "))
    force = mass * acceleration
    print("Force=", force)

elif choose == '2':
     mass = float(input("Enter Mass: "))
     velocity = float(input("Enter Velocity: "))
     momentum = mass * velocity
     print("Momentum=", momentum)

elif choose == '3':
     displacement = float(input("Enter Displacement: "))
     time = float(input("Enter Time: "))
     velocity = displacement * time
     print("Momentum=", velocity)

elif choose == '4':
     initial_velocity = float(input("Enter Initial Velocity: "))
     final_velocity = float(input("Enter Final Velocity: "))
     time = float(input("Enter time: "))
     acceleration = (final_velocity - initial_velocity)/time
     print("Momentum=", acceleration)
else:
     print("Thank you for using my Physics Calculator Program")

    