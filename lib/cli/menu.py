
class TransportManagementCLI:
    def print_header(self, title):
        """Print a header for menu sections."""
        print("\n" + "="*40)
        print(f"{title:^40}")
        print("="*40)

    def display_main_menu(self):
        """Display the main menu options."""
        self.print_header("TRANSPORT MANAGEMENT SYSTEM")
        print("1. Manage Drivers")
        print("2. Manage Vehicles")
        print("3. Manage Routes")
        print("4. Manage Passengers")
        print("5. Manage Trips")
        print("0. Exit")
        return input("\nSelect an option: ")
