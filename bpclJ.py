TollPriceList = [9.50, 18.75, 37.00]

bikeCount = 0
carCount = 0
truckCount = 0

running = True

while running:
    print("\n========== TOLL GATE SYSTEM ==========")
    print("1. Register Vehicle")
    print("2. Show Totals")
    print("3. End Day")
    print("4. Show Report")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        vehicle = input("Enter vehicle (B = Bike, C = Car, T = Truck): ")
        if vehicle == "B":
            bikeCount = bikeCount + 1
            fee = TollPriceList[0]
            print("Bike registered.")
        elif vehicle == "C":
            carCount = carCount + 1
            fee = TollPriceList[1]
            print("Car registered.")
        elif vehicle == "T":
            truckCount = truckCount + 1
            fee = TollPriceList[2]
            print("Truck registered.")
        else:
            fee = 0
            print("Invalid vehicle type. Please enter B, C, or T.")

        if fee > 0:
            print("Fee: R", fee)

    elif choice == "2":
        totalVehicles = bikeCount + carCount + truckCount
        totalIncome = (bikeCount * TollPriceList[0]) + (carCount * TollPriceList[1]) + (truckCount * TollPriceList[2])
        print("\n--- Current Totals ---")
        print("Total Vehicles:", totalVehicles)
        print("Total Income: R", totalIncome)

    elif choice == "3":
        totalVehicles = bikeCount + carCount + truckCount
        totalIncome = (bikeCount * TollPriceList[0]) + (carCount * TollPriceList[1]) + (truckCount * TollPriceList[2])
        print("\n--- DAY SUMMARY ---")
        print("Vehicles:", totalVehicles)
        print("Income: R", totalIncome)
        bikeCount = 0
        carCount = 0
        truckCount = 0
        print("Counters reset for a new day.")

    elif choice == "4":
        totalVehicles = bikeCount + carCount + truckCount
        totalIncome = (bikeCount * TollPriceList[0]) + (carCount * TollPriceList[1]) + (truckCount * TollPriceList[2])
        print("\n========== TOLL GATE REPORT ==========")
        print("Motor Bikes:", bikeCount, "Vehicles, R", bikeCount * TollPriceList[0])
        print("Cars:", carCount, "Vehicles, R", carCount * TollPriceList[1])
        print("Trucks:", truckCount, "Vehicles, R", truckCount * TollPriceList[2])
        print("--------------------------------------")
        print("Total vehicles:", totalVehicles)
        print("Total income: R", totalIncome)

    elif choice == "5":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Please select 1-5.")