
from models import Driver
def manage_drivers(session):
    while True:
        print("\nDriver Management")
        print("1. Create a Driver")
        print("2. Delete a Driver")
        print("3. Display All Drivers")
        print("4. Find Driver by License Number")
        print("5. View Driver's Trips")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter driver's name: ")
            license_number = input("Enter license number: ")
            try:
                driver = Driver(name=name, license_number=license_number)
                session.add(driver)
                session.commit()
                print("Driver created successfully!")
            except Exception as e:
                print(f"Error creating driver: {e}")
        elif choice == "2":
            driver_id = input("Enter Driver ID to delete: ")
            driver = session.query(Driver).get(driver_id)
            if driver:
                session.delete(driver)
                session.commit()
                print("Driver deleted successfully!")
            else:
                print("Driver not found.")
        elif choice == "3":
            drivers = session.query(Driver).all()
            for driver in drivers:
                print(driver)
        elif choice == "4":
            license_number = input("Enter license number: ")
            driver = session.query(Driver).filter_by(license_number=license_number).first()
            if driver:
                print(driver)
            else:
                print("Driver not found.")
        elif choice == "5":
            driver_id = input("Enter Driver ID to view trips: ")
            driver = session.query(Driver).get(driver_id)
            if driver:
                if driver.trips:
                    for trip in driver.trips:
                        print(trip)
                else:
                    print("No trips found for this driver.")
            else:
                print("Driver not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
