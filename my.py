class Train:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats

    def check_availability(self, num_seats):
        return self.available_seats >= num_seats

    def book_tickets(self, num_seats):
        if self.check_availability(num_seats):
            self.available_seats -= num_seats
            return True
        else:
            return False


class TicketBookingSystem:
    def __init__(self, train, username):
        self.train = train
        self.username = username

    def display_menu(self):
        print("1. Check Seat Availability")
        print("2. Book Tickets")
        print("3. Exit")

    def get_user_choice(self):
        return int(input("Enter your choice: "))

    def check_seat_availability(self):
        print(f"Available seats: {self.train.available_seats}")

    def book_tickets(self):
        num_seats = int(input("Enter the number of seats to book: "))
        if self.train.book_tickets(num_seats):
            print(f"Tickets booked successfully for {num_seats} seat(s).")
        else:
            print("Sorry, not enough seats available.")

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.check_seat_availability()
            elif choice == 2:
                self.book_tickets()
            elif choice == 3:
                print("Exiting the ticket booking system. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    total_seats = 50  # Adjust the total number of seats as needed
    train = Train(total_seats)
    username = input("Enter your username: ")
    ticket_system = TicketBookingSystem(train, username)
    ticket_system.run()
