from models import Trip, Driver, Vehicle, Route, Passenger
def manage_trips(session):
    while True:
        print("\nTrip Management")
        print("1. Schedule a Trip")
        print("2. Delete a Trip")
        print("3. View All Trips")
        print("4. Add Passenger to a Trip")
        print("5. Remove Passenger from a Trip")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            driver_id = input("Enter Driver ID: ")
            vehicle_id = input("Enter Vehicle ID: ")
            route_id = input("Enter Route ID: ")
            scheduled_time = input("Enter scheduled time (YYYY-MM-DD HH:MM): ")
            try:
                driver = session.query(Driver).get(driver_id)
                vehicle = session.query(Vehicle).get(vehicle_id)
                route = session.query(Route).get(route_id)
                if not (driver and vehicle and route):
                    raise ValueError("Invalid Driver, Vehicle, or Route ID provided.")
                trip = Trip(driver=driver, vehicle=vehicle, route=route, scheduled_time=scheduled_time)
                session.add(trip)
                session.commit()
                print("Trip scheduled successfully!")
            except Exception as e:
                print(f"Error scheduling trip: {e}")
        elif choice == "2":
            trip_id = input("Enter Trip ID to delete: ")
            trip = session.query(Trip).get(trip_id)
            if trip:
                session.delete(trip)
                session.commit()
                print("Trip deleted successfully!")
            else:
                print("Trip not found.")
        elif choice == "3":
            trips = session.query(Trip).all()
            for trip in trips:
                print(f"Trip ID: {trip.id}, Driver: {trip.driver.name}, Route: {trip.route}, Scheduled: {trip.scheduled_time}")
        elif choice == "4":
            trip_id = input("Enter Trip ID: ")
            passenger_id = input("Enter Passenger ID to add: ")
            try:
                trip = session.query(Trip).get(trip_id)
                passenger = session.query(Passenger).get(passenger_id)
                if trip and passenger:
                    trip.add_passenger(passenger)
                    session.commit()
                    print("Passenger added to trip successfully!")
                else:
                    raise ValueError("Invalid Trip ID or Passenger ID.")
            except Exception as e:
                print(f"Error adding passenger to trip: {e}")
        elif choice == "5":
            trip_id = input("Enter Trip ID: ")
            passenger_id = input("Enter Passenger ID to remove: ")
            try:
                trip = session.query(Trip).get(trip_id)
                passenger = session.query(Passenger).get(passenger_id)
                if trip and passenger:
                    if passenger in trip.passengers:
                        trip.passengers.remove(passenger)
                        session.commit()
                        print("Passenger removed from trip successfully!")
                    else:
                        print("Passenger is not part of this trip.")
                else:
                    raise ValueError("Invalid Trip ID or Passenger ID.")
            except Exception as e:
                print(f"Error removing passenger from trip: {e}")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
