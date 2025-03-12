
from models import Route
def manage_routes(session):
    while True:
        print("\nRoute Management")
        print("1. Create a Route")
        print("2. Delete a Route")
        print("3. Display All Routes")
        print("4. Find Route by Start Location")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            start = input("Enter start location: ")
            end = input("Enter end location: ")
            distance = int(input("Enter distance in km: "))
            duration = int(input("Enter estimated duration in minutes: "))
            route = Route(start_location=start, end_location=end, distance_km=distance, estimated_duration_min=duration)
            session.add(route)
            session.commit()
            print("Route created successfully!")
        elif choice == "2":
            route_id = input("Enter Route ID to delete: ")
            route = session.query(Route).get(route_id)
            if route:
                session.delete(route)
                session.commit()
                print("Route deleted successfully!")
            else:
                print("Route not found.")
        elif choice == "3":
            routes = session.query(Route).all()
            for route in routes:
                print(route)
        elif choice == "4":
            start_location = input("Enter start location: ")
            routes = session.query(Route).filter_by(start_location=start_location).all()
            if routes:
                for route in routes:
                    print(route)
            else:
                print("No routes found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
