# Write a class train which has the method book_ticket , get_status and get_info for train running under indian railways

class Train:
    def __init__(self, name, train_number, number_of_seats, source, destination):
        self.name = name
        self.train_number = train_number
        self.number_of_seats = number_of_seats
        self.available_seats = number_of_seats  # Track available seats
        self.source = source
        self.destination = destination

    def book_ticket(self):
        """Books a ticket if available, otherwise shows a message."""
        if self.available_seats > 0:
            self.available_seats -= 1
            print(f"Ticket booked successfully! Remaining seats: {self.available_seats}")
        else:
            print("Sorry, no seats available.")

    def get_status(self):
        """Displays the number of available seats."""
        print(f"Train {self.train_number} - {self.name}")
        print(f"Available Seats: {self.available_seats}/{self.number_of_seats}")

    def get_info(self):
        """Displays train details."""
        print(f"Train Name: {self.name}")
        print(f"Train Number: {self.train_number}")
        print(f"Route: {self.source} → {self.destination}")
        print(f"Total Seats: {self.number_of_seats}")
        print(f"Available Seats: {self.available_seats}")

# Example Usage:
train1 = Train("Rajdhani Express", 12345, 10, "Delhi", "Mumbai")
train1.get_info()
train1.book_ticket()
train1.get_status()
