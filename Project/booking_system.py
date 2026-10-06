# Sports Badminton Court Booking System

## Project Description

This project is a Sports Badminton Court Booking System developed using Python and Object-Oriented Programming (OOP).

The program allows a user to:

- Create a court booking
- Cancel an existing booking
- Show all current bookings
- Exit the program

The program runs through an interactive menu using Python `input()`.

## Main Business Rule

The same court cannot be booked by two customers at the same time.

For example:

- Maya books Court 1 at 10:00 → Booking confirmed
- Simon tries Court 1 at 10:00 → Booking rejected
- Maya cancels Court 1 at 10:00 → Booking cancelled
- Simon tries Court 1 at 10:00 again → Booking confirmed

This demonstrates that creating and cancelling bookings changes the state of the system.

## Classes

### Customer

The `Customer` class represents a customer.

Attributes:

- `customer_id`
- `name`

### Court

The `Court` class represents a badminton court.

Attributes:

- `court_id`
- `name`

### Booking

The `Booking` class represents one reservation.

It connects:

- A Customer object
- A Court object
- A time slot

### BookingSystem

The `BookingSystem` class manages the bookings.

Its responsibilities include:

- Creating bookings
- Checking for booking conflicts
- Cancelling bookings
- Showing current bookings
- Rejecting invalid booking data

## Project Structure

```text
sports_court_booking/
│
├── customer.py
├── court.py
├── booking.py
├── booking_system.py
├── main.py
└── README.md
```

## How to Run the Program

Open Terminal and go to the project folder.

Run: 
```bash 

cd ~/Downloads/sports_court_booking

 ls # list file in folder

python3 main.py

```

## Program Menu

When the program starts, the following menu is displayed:

```text
=== SPORTS BADMINTON COURT BOOKING SYSTEM ===

--- MENU ---
1. Create booking
2. Cancel booking
3. Show all bookings
4. Exit
```

The menu continues running until the user selects Exit.

## Creating a Booking

The user selects:

```text
1. Create booking
```

The program asks for:

- Customer name
- Court
- Time slot

Example:

```text
Enter customer name: Maya
Choose court (1-5): 1
Enter booking time: 10:00

Booking confirmed!
```

Before creating the booking, the system checks whether the selected court is already booked at that time.

## Cancelling a Booking

The user selects:

```text
2. Cancel booking
```

The program asks for:

- Customer name
- Court name
- Time slot

If the booking exists, it is removed from the bookings list.

```text
Booking cancelled.
```

If it does not exist:

```text
Booking not found.
```

After a booking is cancelled, that court and time slot can be booked again.

## Showing Current Bookings

The user selects:

```text
3. Show all bookings
```

Example:

```text
Current bookings:
Maya booked Court 1 at 10:00
Simon booked Court 2 at 11:00
```

If there are no bookings:

```text
No bookings found.
```

## Validation and Business Rules

The program checks for:

- Empty customer names
- Empty time slots
- Invalid court selections
- Duplicate bookings for the same court and time
- Cancellation of bookings that do not exist
- Invalid menu selections

Invalid bookings are rejected and are not added to the bookings list.

## Python Concepts Used

This project demonstrates:

- Classes and objects
- OOP concept
- `__init__`
- `self`
- Attributes
- Methods
- `__str__`
- Object relationships
- Lists
- Dictionaries
- `for` loops
- `while` loops
- `if`, `elif` and `else`
- `input()`
- `return`
- `continue`
- Validation 

## What I Learned

Through this project, I learned how different Python classes can work together in one connected program.

I also learned how to maintain the state of a program using a list of Booking objects.

One important part of the project was preventing duplicate bookings. Before a new booking is created, the program checks the existing bookings to see if the same court and time slot are already in use.

I also implemented cancellation. When a booking is cancelled, the Booking object is removed from the bookings list, making that court and time available again.

Finally, I improved the project by adding an interactive menu using a `while` loop and `input()`, allowing the user to create bookings, cancel bookings, display bookings, and exit the application.
