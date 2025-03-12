from models import Vehicle, Driver
def manage_vehicles(session):
    while True:
        print("\nVehicle Management")
        print("1. Create a Vehicle")
        print("2. Delete a Vehicle")
        print("3. Display All Vehicles")
        print("4. Find Vehicle by ID")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            year = int(input("Enter vehicle year: "))
            driver_id = input("Enter driver ID (optional, leave blank if none): ")
            driver = session.query(Driver).get(driver_id) if driver_id else None
            vehicle = Vehicle(make=make, model=model, year=year, driver=driver)
            session.add(vehicle)
            session.commit()
            print("Vehicle created successfully!")
        elif choice == "2":
            vehicle_id = input("Enter Vehicle ID to delete: ")
            vehicle = session.query(Vehicle).get(vehicle_id)
            if vehicle:
                session.delete(vehicle)
                session.commit()
                print("Vehicle deleted successfully!")
            else:
                print("Vehicle not found.")
        elif choice == "3":
            vehicles = session.query(Vehicle).all()
            for vehicle in vehicles:
                print(vehicle)
        elif choice == "4":
            vehicle_id = input("Enter Vehicle ID: ")
            vehicle = session.query(Vehicle).get(vehicle_id)
            if vehicle:
                print(vehicle)
            else:
                print("Vehicle not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
