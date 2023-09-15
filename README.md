# What is this Project about?

# Hotel Reservation System

This is a simple Python program for a hotel reservation system. The program utilizes the Pandas library to manage hotel data, customer bookings, and credit card information. Let's break down the main components of this code:

**Data Loading:**
The program loads data from CSV files for hotels, credit cards, and card security. It uses Pandas DataFrames to manipulate and access this data effectively.

**Classes:**
- `Hotel`: Represents a hotel and provides methods for booking and checking availability.
- `SpaHotel`: Inherits from `Hotel` and extends its functionality (although currently, it only has a placeholder method).
- `ReservationTicket`: Generates a reservation ticket for a hotel booking.
- `SpaReservationTicket`: Generates a reservation ticket for a spa booking.
- `CreditCard`: Represents a credit card and validates it against a list of cards.
- `SecureCreditCard`: Inherits from `CreditCard` and adds an authentication step.

**Main Loop:**
The program's main loop allows users to input a hotel ID, checks its availability, validates a credit card, and books a hotel. Optionally, it offers spa booking with a separate reservation ticket.

This code serves as a basic example of a hotel reservation system. Further enhancements can be made to handle more complex scenarios, databases, or real-time payment processing.

To run this code, ensure you have the required CSV files ('hotels.csv', 'cards.csv', 'card_security.csv') with appropriate data.
