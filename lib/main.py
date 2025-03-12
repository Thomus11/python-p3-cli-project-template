
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cli.menu import TransportManagementCLI
from cli.driver import manage_drivers
from cli.vehicle import manage_vehicles
from cli.route import manage_routes
from cli.passenger import manage_passengers
from cli.trip import manage_trips
from models.models import Base

def main():
    
    engine = create_engine('sqlite:///transport.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cli = TransportManagementCLI()

    while True:
        choice = cli.display_main_menu()
        if choice == "1":
            manage_drivers(session)
        elif choice == "2":
            manage_vehicles(session)
        elif choice == "3":
            manage_routes(session)
        elif choice == "4":
            manage_passengers(session)
        elif choice == "5":
            manage_trips(session)
        elif choice == "0":
            print("Exiting the Transport Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
