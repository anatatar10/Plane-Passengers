import domain.passenger as p

class PassengerValidation:
    '''
    Checks if a passenger is valid.
    '''
    #first name, last name, passport number

    def validate(self, p):
        '''
        Checks if passenger respects the conditions defined by the programmer.
        in: an instance class Passenger
        out: -
        '''
        errors = 0

        if p.Passenger.firstName() == "":
            print("First name invalid!")
            errors += 1

        if p.Passenger.lastName() == "":
            print("Last name invalid!")
            errors += 1

        if p.Passenger.passportNumber() == "":
            print("Passport number invalid!")
            errors += 1

        if errors>0:
            raise ValueError(errors)