'''Model for aircraft flights.'''

# Defining a class
class Flight:
    # by convention, class names use CamelCase - with capital start
    '''A flight with a particular passenger aircraft.'''

    def __init__(self, number, aircraft):
        # Esstablish an invariant that will persist during the lifetime
        # of the Flight object
        if not number[:2].isalpha(): # If the first 2 elements of the string
                                     # are not letter
            raise ValueError('No airline code in {}'.format(number))
        
        if not number[:2].isupper():
            raise ValueError('Invalid airline code {}'.format(number))

        if not (number[2:].isdigit() and int(number[2:]) < 10000):
            raise ValueError('Invalid route number {}'.format(number))

        self._number = number
        # Why _number?
        # Avoid name clash with number()
        # By convention, implementation details start with underscore
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        # To not deal with the fact that row indicies are 1 based while 
        # python lists are 0 based, we are going to skip the first entry
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def _parse_seat(self, seat):
        # This method begins with a underscore(_) because its an implementation detail
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError('Invalid seat letter {}'.format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError('Invalid seat row {}'.format(row_text))

        if row not in rows:
            raise ValueError('Invalid row number {}'.format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        '''
        Allocate a seat to a passenger, 
        
        Args:
            seat: A seaet designator such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable
        '''
        
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} is already occupied'.format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger (self, from_seat, to_seat):
        '''
        Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the
                    passenger to be moved.

            to_ seat; The new seat designator.
        '''
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError('No passenger to relocate in seat {}'.format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError('Seat {} already occupied'.format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        '''An iterable series of passenger seating locations'''
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

# Create boarding passes in alphabetical order for the passengers on the Flight
# NOTE: Following the Separation of concerns rule we won't put this in the Flight
# class
# Remember that functions are objects too!
def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {}".format(passenger) 
    output += "Flight: {}".format(flight_number) 
    output += "Seat: {}".format(seat)
    output += "Aircraft: {}".format(aircraft) + " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print (card)
    print ()

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row = 6))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Rich Mickey")
    return f
