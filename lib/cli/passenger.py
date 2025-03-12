
from models import Passenger
def manage_passengers(session):
    while True:
        print("\nPassenger Management")
        print("1. Add a Passenger")
        print("2. Delete a Passenger")
        print("3. View All Passengers")
        print("4. Find Passenger by Name")
        print("5. View Passenger's Trips")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter passenger's name: ")
            contact_info = input("Enter contact info (optional): ")
            try:
                passenger = Passenger(name=name, contact_info=contact_info)
                session.add(passenger)
                session.commit()
                print("Passenger added successfully!")
            except Exception as e:
                print(f"Error adding passenger: {e}")
        elif choice == "2":
            passenger_id = input("Enter Passenger ID to delete: ")
            passenger = session.query(Passenger).get(passenger_id)
            if passenger:
                session.delete(passenger)
                session.commit()
                print("Passenger deleted successfully!")
            else:
                print("Passenger not found.")
        elif choice == "3":
            passengers = session.query(Passenger).all()
            for passenger in passengers:
                print(passenger)
        elif choice == "4":
            name = input("Enter passenger's name to search: ")
            passengers = session.query(Passenger).filter(Passenger.name == name).all()

            if passengers:
                for passenger in passengers:
                    print(passenger)
            else:
                print("No passengers found.")
        elif choice == "5":
            passenger_id = input("Enter Passenger ID to view trips: ")
            passenger = session.query(Passenger).get(passenger_id)
            if passenger:
                if passenger.trips:
                    for trip in passenger.trips:
                        print(trip)
                else:
                    print("No trips found for this passenger.")
            else:
                print("Passenger not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
