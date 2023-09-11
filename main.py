import pandas

df = pandas.read_csv('hotels.csv')


class Hotel:
    def __int__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __int__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


# main loop of the program goes below----------
print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
