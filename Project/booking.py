class Booking:
    def __init__(self, customer, court, time_slot):
        self.customer = customer
        self.court = court
        self.time_slot = time_slot

    def __str__(self):
        return (
            f"{self.customer.name} booked "
            f"{self.court.name} at {self.time_slot}"
        )
