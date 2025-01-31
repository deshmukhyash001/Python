class Vehicle:
    def __init__(self, vehicle_id, model, brand, year, price):
        self.vehicle_id = vehicle_id
        self.model = model
        self.brand = brand
        self.year = year
        self.price = price

    def display_info(self):
        print(f"ID: {self.vehicle_id}, Model: {self.model}, Brand: {self.brand}, Year: {self.year}, Price: ${self.price}")


class VehicleManagementSystem:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self):
        vehicle_id = input("Enter vehicle ID: ")
        model = input("Enter vehicle model: ")
        brand = input("Enter vehicle brand: ")
        year = input("Enter vehicle year: ")
        price = input("Enter vehicle price: ")

        vehicle = Vehicle(vehicle_id, model, brand, year, price)
        self.vehicles[vehicle_id] = vehicle
        print(f"Vehicle {vehicle_id} added successfully!")

    def display_all_vehicles(self):
        if self.vehicles:
            for vehicle in self.vehicles.values():
                vehicle.display_info()
        else:
            print("No vehicles found.")

    def update_vehicle(self):
        vehicle_id = input("Enter vehicle ID to update: ")
        if vehicle_id in self.vehicles:
            print("Leave blank if no change.")
            model = input("Enter new model: ")
            brand = input("Enter new brand: ")
            year = input("Enter new year: ")
            price = input("Enter new price: ")

            if model:
                self.vehicles[vehicle_id].model = model
            if brand:
                self.vehicles[vehicle_id].brand = brand
            if year:
                self.vehicles[vehicle_id].year = year
            if price:
                self.vehicles[vehicle_id].price = price

            print(f"Vehicle {vehicle_id} updated successfully!")
        else:
            print("Vehicle not found.")

    def delete_vehicle(self):
        vehicle_id = input("Enter vehicle ID to delete: ")
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]
            print(f"Vehicle {vehicle_id} deleted successfully!")
        else:
            print("Vehicle not found.")


def main():
    vms = VehicleManagementSystem()

    while True:
        print("\nVehicle Management System")
        print("1. Add Vehicle")
        print("2. View All Vehicles")
        print("3. Update Vehicle")
        print("4. Delete Vehicle")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vms.add_vehicle()
        elif choice == "2":
            vms.display_all_vehicles()
        elif choice == "3":
            vms.update_vehicle()
        elif choice == "4":
            vms.delete_vehicle()
        elif choice == "5":
            print("Exiting Vehicle Management System.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
