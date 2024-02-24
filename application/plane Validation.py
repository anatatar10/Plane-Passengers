import infrastructure.plane as plane

class PlaneValidation:
    '''
    Checks if a plane is valid.
    '''
    #nameNumber, airline, number of seats, destination and list of passengers

    def validate(self, plane):
        '''
        Checks if plane respects the conditions defined by the programmer.
        IN: an instance class Plane
        OUT: -
        CONDIS: -
        '''
        errors = 0
    #nameNumber, airline, number of seats, destination and list of passengers

        if plane.Plane.airline() =="":
            print("Airline invalid")
            errors += +1

        if plane.Plane.numberOfSeats() < 0 or plane.Plane.numberOfSeats < plane.Plane.len(listOfPassengers):
            print("Number of seats invalid!")
            errors += +1

        if errors > 0:
            raise ValueError(errors)