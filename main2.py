import pandas as pd
from abc import ABC, abstractmethod

# we only supply the id column as string for our ease of comparisons in the code
df = pd.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    watermark = "The Real Estate Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

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

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book(self):
        pass


# ABSTRACT CLASS BELOW
class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking details:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


class SpaReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your Spa reservation!
        Here is your Spa booking details:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
