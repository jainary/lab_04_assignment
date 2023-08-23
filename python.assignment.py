class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        found_flights = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                found_flights.append(flight)
        return found_flights

    def search_by_source(self, source):
        found_flights = []
        for flight in self.flights:
            if flight.source == source:
                found_flights.append(flight)
        return found_flights

    def search_between_cities(self, source, destination):
        found_flights = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                found_flights.append(flight)
        return found_flights

def main():
    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    flight_table = FlightTable()
    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_table.add_flight(flight)

    print("Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city: ")
        found_flights = flight_table.search_by_city(city)
    elif choice == 2:
        source = input("Enter the source city: ")
        found_flights = flight_table.search_by_source(source)
    elif choice == 3:
        source = input("Enter the source city: ")
        destination = input("Enter the destination city: ")
        found_flights = flight_table.search_between_cities(source, destination)
    else:
        print("Invalid choice.")
        return

    if found_flights:
        print("Flights matching the search:")
        for flight in found_flights:
            print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
    else:
        print("No flights found for the given search.")

if __name__ == "__main__":
    main()