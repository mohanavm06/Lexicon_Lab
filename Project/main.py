from customer import Customer
from court import Court
from booking_system import BookingSystem


def main():
    system = BookingSystem()

    # Create courtsg
    print("=== SPORTS BADMINTON COURT BOOKING SYSTEM ===")

    while True:
        print("\n--- MENU ---")
        print("1. Create booking")
        print("2. Cancel booking")
        print("3. Show all bookings")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        # CREATE BOOKING
        if choice == "1":
            name = input("Enter customer name: ")

            print("\nAvailable courts:")
            print("1. Court 1 -100Kr/hour")
            print("2. Court 2 -150Kr/hour")
            print("3. Court 3 -100Kr/hour")
            print("4. Court 4 -120Kr/hour")
            print("5. Court 5 -100Kr/hour")

            court_choice = input("Choose court (1-5): ")

            if court_choice not in courts:
                print("Invalid court selection.")
                continue

            selected_court = courts[court_choice]

            time_slot = input(
                "Enter booking time (for example 10:00): "
            )

            customer = Customer(customer_id, name)

            if system.create_booking(
                customer,
                selected_court,
                time_slot
            ):
                customer_id += 1

        # CANCEL BOOKING
        elif choice == "2":
            customer_name = input("Enter customer name: ")

            print("\nChoose court:")
            print("1. Court 1 -100Kr/hour")
            print("2. Court 2 -150Kr/hour")
            print("3. Court 3 -100Kr/hour")
            print("4. Court 4 -120Kr/hour")
            print("5. Court 5 -100Kr/hour")

            court_choice = input("Choose court (1-5): ")

            if court_choice not in courts:
                print("Invalid court selection.")
                continue

            selected_court = courts[court_choice]

            time_slot = input(
                "Enter booking time (for example 10:00): "
            )

            system.cancel_booking(
                customer_name,
                selected_court.name,
                time_slot
            )

        # SHOW BOOKINGS
        elif choice == "3":
            print("\n=== CURRENT BOOKINGS ===")
            system.show_bookings()

        # EXIT
        elif choice == "4":
            print("Thank you for using the booking system.")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
