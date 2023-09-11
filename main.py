import pandas
# we only supply the id column as string for our ease of comparisons in the code
df = pandas.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """ Book a hotel by changing its availability to no """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # index = false cause python shouldn't add another index
        df.to_csv("hotels.csv", index=False)
        pass

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


# main loop of the program goes below----------
print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
