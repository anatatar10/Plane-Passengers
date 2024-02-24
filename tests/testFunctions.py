import unittest
import infrastructure.airport as airport
from infrastructure import sortBy
import domain
import application.controller as cont



class FunctionsTestClass(unittest.TestCase):
    def setUp(self):
        self.passenger1 = airport.plane.passenger.Passenger("Claudia", "Popa", "123abc")
        self.passenger2 = airport.plane.passenger.Passenger("Robert", "Chinezu", "552cva")
        self.passenger3 = airport.plane.passenger.Passenger("Sebastian", "Moisescu", "536nsf")

        self.plane1 = airport.plane.Plane("1", "wizz", 5, "Paris",
                                          [domain.passenger.Passenger("Ana", "Tatar", "111aaa"),
                                           domain.passenger.Passenger("Anamaria", "Anca", "111bbb"),
                                           domain.passenger.Passenger("Mihai", "Horea", "111ccc")])
        self.plane2 = airport.plane.Plane("2", "tarom", 10, "Dubai",
                                          [domain.passenger.Passenger("David", "Bobb", "223abc"),
                                           domain.passenger.Passenger("Ioana", "Vlad", "223gda")])
        self.plane3 = airport.plane.Plane("3", "Lufthansa", 15, "Bucharest",
                                          [domain.passenger.Passenger("Georgiana", "Moldovan", "444abc"),
                                           domain.passenger.Passenger("Denisa", "Muntean", "555ccc"),
                                           domain.passenger.Passenger("George", "Oltean", "666ddd")])
        self.plane4 = airport.plane.Plane("4", "Qatar", 30, "New York", [domain.passenger.Passenger("Laura", "Anton", "631fae")])

        self.airport1 = airport.Airport([self.plane1, self.plane2])
        self.airport2 = airport.Airport([self.plane1, self.plane2, self.plane3])
        self.airport3 = airport.Airport([self.plane4])

        self.plane11 = airport.plane.Plane("1", "wizz", 5, "Paris",
                                      [domain.passenger.Passenger("Ana", "Tatar", "111aaa"),
                                       domain.passenger.Passenger("Anamaria", "Anca", "111bbb"),
                                       domain.passenger.Passenger("Mihai", "Horea", "111ccc"),
                                       domain.passenger.Passenger("Cosmin", "Pop", "213cc")])
        self.plane22 = airport.plane.Plane("2", "tarom", 10, "Paris",
                                      [domain.passenger.Passenger("David", "Bobb", "223abc"),
                                       domain.passenger.Passenger("Ioana", "Vlad", "223gda")])
        self.plane33 = airport.plane.Plane("3", "Lufthansa", 15, "Paris",
                                      [domain.passenger.Passenger("Georgiana", "Moldovan", "444abc"),
                                       domain.passenger.Passenger("Denisa", "Muntean", "555ccc"),
                                       domain.passenger.Passenger("George", "Oltean", "666ddd")])
        self.plane44 = airport.plane.Plane("4", "Qatar", 30, "Dubai",
                                      [domain.passenger.Passenger("Laura", "Anton", "631fae")])
        self.plane55 = airport.plane.Plane("5", "Singapore Airline", 35, "Dubai",
                                      [domain.passenger.Passenger("Mircea", "Eliade", "935gfs"),
                                       domain.passenger.Passenger("Mihai", "Eminescu", "258dgg")])

        self.airport4 = airport.Airport([self.plane11, self.plane22, self.plane33, self.plane33, self.plane44, self.plane55])

        self.controller = cont.Controller()

    def test_createPassenger(self):
        self.assertEqual(self.passenger1.firstName, "Claudia")
        self.assertEqual(self.passenger1.lastName, "Popa")
        self.assertEqual(self.passenger1.passportNumber, "123abc")

        self.assertEqual(self.passenger2.firstName, "Robert")
        self.assertEqual(self.passenger2.lastName, "Chinezu")
        self.assertEqual(self.passenger2.passportNumber, "552cva")

        self.assertEqual(self.passenger3.firstName, "Sebastian")
        self.assertEqual(self.passenger3.lastName, "Moisescu")
        self.assertEqual(self.passenger3.passportNumber, "536nsf")

    def test_setFirstName(self):
        self.passenger1.firstName = "Maria"
        self.assertEqual(self.passenger1.firstName, "Maria")
        self.passenger2.firstName = "Roberta"
        self.assertEqual(self.passenger2.firstName, "Roberta")
        self.passenger3.firstName = "Sabina"
        self.assertEqual(self.passenger3.firstName, "Sabina")

    def test_setLastName(self):
        self.passenger1.lastName = "Popescu"
        self.assertEqual(self.passenger1.lastName, "Popescu")
        self.passenger2.lastName = "Chinez"
        self.assertEqual(self.passenger2.lastName, "Chinez")
        self.passenger3.lastName = "Moise"
        self.assertEqual(self.passenger3.lastName, "Moise")

    def test_setPassportNumber(self):
        self.passenger1.passportNumber = "999ccc"
        self.assertEqual(self.passenger1.passportNumber, "999ccc")
        self.passenger2.passportNumber = "222fff"
        self.assertEqual(self.passenger2.passportNumber, "222fff")
        self.passenger3.passportNumber = "333fff"
        self.assertEqual(self.passenger3.passportNumber, "333fff")

    def test_passengerStringRepresentation(self):
        self.assertEqual(str(self.passenger1), "Passenger(Claudia Popa, 123abc)")
        self.assertEqual(str(self.passenger2),"Passenger(Robert Chinezu, 552cva)")
        self.assertEqual(str(self.passenger3),"Passenger(Sebastian Moisescu, 536nsf)")

    def test_createPlane(self):
        self.assertEqual(self.plane1.nameNumber, "1")
        self.assertEqual(self.plane1.airline, "wizz")
        self.assertEqual(self.plane1.numberOfSeats, 5)
        self.assertEqual(self.plane1.destination, "Paris")

        self.assertEqual(self.plane2.nameNumber, "2")
        self.assertEqual(self.plane2.airline, "tarom")
        self.assertEqual(self.plane2.numberOfSeats, 10)
        self.assertEqual(self.plane2.destination, "Dubai")

        self.assertEqual(self.plane3.nameNumber, "3")
        self.assertEqual(self.plane3.airline, "Lufthansa")
        self.assertEqual(self.plane3.numberOfSeats, 15)
        self.assertEqual(self.plane3.destination, "Bucharest")

    def test_setNameNumber(self):
        self.plane1.nameNumber = "10"
        self.assertEqual(self.plane1.nameNumber, "10")
        self.plane2.nameNumber = "20"
        self.assertEqual(self.plane2.nameNumber, "20")
        self.plane3.nameNumber = "30"
        self.assertEqual(self.plane3.nameNumber, "30")

    def test_setAirline(self):
        self.plane1.airline = "Emirates"
        self.assertEqual(self.plane1.airline, "Emirates")
        self.plane2.airline = "Qatar"
        self.assertEqual(self.plane2.airline, "Qatar")
        self.plane3.airline = "flydubai"
        self.assertEqual(self.plane3.airline, "flydubai")

    def test_setNumOfSeats(self):
        self.plane1.numberOfSeats = 50
        self.assertEqual(self.plane1.numberOfSeats, 50)
        try:
            self.plane1.numberOfSeats = -2
        except ValueError as ve:
            print(ve)

    def test_setDestination(self):
        self.plane1.destination = "London"
        self.assertEqual(self.plane1.destination, "London")
        self.plane2.destination = "Rome"
        self.assertEqual(self.plane2.destination, "Rome")
        self.plane3.destination = "Targu Mures"
        self.assertEqual(self.plane3.destination, "Targu Mures")

    def test_setListOfPassengers(self):
        self.plane1.listOfPassengers = [("Anca", "Vultur", "123"), ("Mihai", "Viteazu", "987abc")]
        self.assertEqual(str(self.plane1.listOfPassengers), "[('Anca', 'Vultur', '123'), ('Mihai', 'Viteazu', '987abc')]")

        self.plane2.listOfPassengers = [("Robert", "Chinezu", "552cva"), ("Anamaria", "Anca", "111bbb")]
        self.assertEqual(str(self.plane2.listOfPassengers), "[('Robert', 'Chinezu', '552cva'), ('Anamaria', 'Anca', '111bbb')]")

        self.plane3.listOfPassengers = ("Sebastian", "Moisescu", "536nsf")
        self.assertEqual(str(self.plane3.listOfPassengers), "('Sebastian', 'Moisescu', '536nsf')")

    def test_planeRepresentation(self):
        self.assertEqual(str(self.plane1), "Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)])")
        self.assertEqual(str(self.plane2), "Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])")
        self.assertEqual(str(self.plane3), "Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])")

    def test_addPassenger(self):
        self.plane1.addPassenger("Robert", "Pana", "341ags")
        self.assertEqual(len(self.plane1.listOfPassengers), 4)
        self.plane2.addPassenger("Silvia", "Robu", "5134asd")
        self.assertEqual(len(self.plane2.listOfPassengers), 3)
        self.plane3.addPassenger("Radu", "Serghei", "382ddd")
        self.assertEqual(len(self.plane3.listOfPassengers), 4)

    def test_getAllPassengers(self):
        self.assertEqual(str(self.plane1.getAllPassengers()), "[Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]")
        self.assertEqual(str(self.plane2.getAllPassengers()), "[Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]")
        self.assertEqual(str(self.plane3.getAllPassengers()), "[Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)]")

    def test_getPassengerAtGivenIndex(self):
        self.assertEqual(str(self.plane1.getPassengerAtGivenIndex(0)), "Passenger(Ana Tatar, 111aaa)")
        self.assertEqual(str(self.plane1.getPassengerAtGivenIndex(1)), "Passenger(Anamaria Anca, 111bbb)")
        try:
            self.plane1.getPassengerAtGivenIndex(-5)
        except IndexError as ie:
            print(ie)

    def test_updatePassengerAtGivenIndex(self):
        self.plane1.updatePassengerAtGivenIndex(0, "Mary", "Jones", "452abc")
        self.assertEqual(str(self.plane1.getPassengerAtGivenIndex(0)), "Passenger(Mary Jones, 452abc)")
        self.plane2.updatePassengerAtGivenIndex(1, "Mary", "Jones", "452abc")
        self.assertEqual(str(self.plane2.getPassengerAtGivenIndex(1)), "Passenger(Mary Jones, 452abc)")
        try:
            self.plane3.updatePassengerAtGivenIndex(-4, "Mary", "Jones", "452abc")
        except IndexError as ie:
            print(ie)

    def test_deletePassengerAtGivenIndex(self):
        self.plane1.deletePassengerAtGivenIndex(2)
        self.assertEqual(len(self.plane1.listOfPassengers), 2)
        self.plane2.deletePassengerAtGivenIndex(1)
        self.assertEqual(len(self.plane2.listOfPassengers), 1)
        try:
            self.plane3.deletePassengerAtGivenIndex(-5)
        except IndexError as ie:
            print(ie)

    def test_SortPassengersByLastName(self):
        self.plane1.sortPassengersByLastNameAscending()
        self.assertEqual(str(self.plane1), """Plane(1, wizz, 5, Paris and [Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc), Passenger(Ana Tatar, 111aaa)])""")
        self.plane1.sortPassengersByLastNameDescending()
        self.assertEqual(str(self.plane1), """Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Mihai Horea, 111ccc), Passenger(Anamaria Anca, 111bbb)])""")

        self.plane2.sortPassengersByLastNameAscending()
        self.assertEqual(str(self.plane2), """Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])""")
        self.plane2.sortPassengersByLastNameDescending()
        self.assertEqual(str(self.plane2), """Plane(2, tarom, 10, Dubai and [Passenger(Ioana Vlad, 223gda), Passenger(David Bobb, 223abc)])""")

        self.plane3.sortPassengersByLastNameAscending()
        self.assertEqual(str(self.plane3), """Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])""")
        self.plane3.sortPassengersByLastNameDescending()
        self.assertEqual(str(self.plane3), """Plane(3, Lufthansa, 15, Bucharest and [Passenger(George Oltean, 666ddd), Passenger(Denisa Muntean, 555ccc), Passenger(Georgiana Moldovan, 444abc)])""")

    def test_checkPrefix(self):
        self.assertEqual(self.plane1.checkPrefix("Ana"), 2)
        self.assertEqual(self.plane1.checkPrefix("Mi"), 1)
        self.assertEqual(self.plane3.checkPrefix("Georg"), 2)

    def test_concatenationNumPassDest(self):
        self.assertEqual(str(self.plane1.concatenationNumPassDest()), "3Paris")
        self.assertEqual(str(self.plane2.concatenationNumPassDest()), "2Dubai")
        self.assertEqual(str(self.plane3.concatenationNumPassDest()), "3Bucharest")

    def test_createAirport(self):
        self.assertEqual(str(self.airport1.listOfPlanes), "[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])]")
        self.assertEqual(str(self.airport2.listOfPlanes), "[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])]")
        self.assertEqual(str(self.airport3.listOfPlanes), "[Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])]")

    def test_setListOfPlanes(self):
        self.airport1.listOfPlanes = [("3", "Lufthansa", 15, "Bucharest",
                                          [domain.passenger.Passenger("Georgiana", "Moldovan", "444abc"),
                                           domain.passenger.Passenger("Denisa", "Muntean", "555ccc"),
                                           domain.passenger.Passenger("George", "Oltean", "666ddd")])]
        self.assertEqual(str(self.airport1.listOfPlanes), "[('3', 'Lufthansa', 15, 'Bucharest', [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])]")

    def test_airportRepresentation(self):
        self.assertEqual(str(self.airport1), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])])")
        self.assertEqual(str(self.airport2), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])])")
        self.assertEqual(str(self.airport3), "Airport([Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])])")

    def test_addPlane(self):
        self.airport1.addPlane("3", "Lufthansa", 15, "Bucharest", [domain.passenger.Passenger("Georgiana", "Moldovan", "444abc"), domain.passenger.Passenger("Denisa", "Muntean", "555ccc"), domain.passenger.Passenger("George", "Oltean", "666ddd")])
        self.assertEqual(len(self.airport1.listOfPlanes), 3)
        self.airport2.addPlane("4", "Qatar", 30, "New York", [domain.passenger.Passenger("Laura", "Anton", "631fae")])
        self.assertEqual(len(self.airport2.listOfPlanes), 4)
        self.airport3.addPlane("4", "Qatar", 30, "New York", [domain.passenger.Passenger("Laura", "Anton", "631fae")])
        self.assertEqual(len(self.airport3.listOfPlanes), 2)

    def test_getAllPlanes(self):
        self.assertEqual(str(self.airport1.getAllPlanes()), "[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])]")
        self.assertEqual(str(self.airport2.getAllPlanes()), "[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])]")
        self.assertEqual(str(self.airport3.getAllPlanes()), "[Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])]")

    def test_getPlaneAtGivenIndex(self):
        self.assertEqual(str(self.airport1.getPlaneAtGivenIndex(0)), "Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)])")
        try:
            self.airport1.getPlaneAtGivenIndex(-1)
        except IndexError as ie:
            print(ie)
        try:
            self.airport3.getPlaneAtGivenIndex(3)
        except IndexError as ie:
            print(ie)

    def test_updatePlaneAtGivenIndex(self):
        self.airport1.updatePlaneAtGivenIndex(0, "4", "Qatar", 30, "New York", [("Laura", "Anton", "631fae")])
        self.assertEqual(str(self.airport1.getPlaneAtGivenIndex(0)), "Plane(4, Qatar, 30, New York and [('Laura', 'Anton', '631fae')])")
        try:
            self.airport1.updatePlaneAtGivenIndex(-1, "4", "Qatar", 30, "New York", [("Laura", "Anton", "631fae")])
        except IndexError as ie:
            print(ie)
        try:
            self.airport3.updatePlaneAtGivenIndex(3, "4", "Qatar", 30, "New York", [("Laura", "Anton", "631fae")])
        except IndexError as ie:
            print(ie)

    def test_deletePlaneAtGivenIndex(self):
        self.airport1.deletePlaneAtGivenIndex(0)
        self.assertEqual(len(self.airport1.listOfPlanes), 1)
        try:
            self.airport1.deletePlaneAtGivenIndex(-1)
        except IndexError as ie:
            print(ie)
        try:
            self.airport3.deletePlaneAtGivenIndex(3)
        except IndexError as ie:
            print(ie)

    def test_sortPlanesByNumOfPassengersAscending(self):
        self.airport1.sortPlanesByNumOfPassengersAscending()
        self.assertEqual(str(self.airport1), "Airport([Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)])])")
        self.airport2.sortPlanesByNumOfPassengersAscending()
        self.assertEqual(str(self.airport2), "Airport([Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])])")
        self.airport3.sortPlanesByNumOfPassengersAscending()
        self.assertEqual(str(self.airport3), "Airport([Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])])")

    def test_sortPlanesByNumOfPassengersDescending(self):
        self.airport1.sortPlanesByNumOfPassengersDescending()
        self.assertEqual(str(self.airport1), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])])")
        self.airport2.sortPlanesByNumOfPassengersDescending()
        self.assertEqual(str(self.airport2), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])])")
        self.airport3.sortPlanesByNumOfPassengersDescending()
        self.assertEqual(str(self.airport3), "Airport([Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])])")

    def test_sortPlanesByPrefixAscending(self):
        self.airport1.sortPlanesByPrefixAscending()
        self.assertEqual(str(self.airport1), "Airport([Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)])])")
        self.airport2.sortPlanesByPrefixAscending()
        self.assertEqual(str(self.airport2), "Airport([Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])])")
        self.airport3.sortPlanesByPrefixAscending()
        self.assertEqual(str(self.airport3), "Airport([Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])])")

    def test_sortPlanesByPrefixDescending(self):
        self.airport1.sortPlanesByPrefixDescending()
        self.assertEqual(str(self.airport1), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])])")
        self.airport2.sortPlanesByPrefixDescending()
        self.assertEqual(str(self.airport2), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])])")
        self.airport3.sortPlanesByPrefixAscending()
        self.assertEqual(str(self.airport3), "Airport([Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])])")

    def test_sortPlanesByConcatenationAscending(self):
        self.airport1.sortPlanesByConcatenationAscending()
        self.assertEqual(str(self.airport1), "Airport([Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)])])")
        self.airport2.sortPlanesByConcatenationAscending()
        self.assertEqual(str(self.airport2), "Airport([Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)]), Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)])])")
        self.airport3.sortPlanesByConcatenationAscending()
        self.assertEqual(str(self.airport3), "Airport([Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])])")

    def test_sortPlanesByConcatenationDescending(self):
        self.airport1.sortPlanesByConcatenationDescending()
        self.assertEqual(str(self.airport1), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])])")
        self.airport2.sortPlanesByConcatenationDescending()
        self.assertEqual(str(self.airport2), "Airport([Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])])")
        self.airport3.sortPlanesByConcatenationDescending()
        self.assertEqual(str(self.airport3), "Airport([Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])])")

    def test_identifyPlanesPassportThreeLetters(self):
        self.assertEqual(str(self.airport1.identifyPlanesPassportThreeLetters()), "[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])]")
        self.assertEqual(str(self.airport2.identifyPlanesPassportThreeLetters()), "[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]), Plane(2, tarom, 10, Dubai and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)])]")
        self.assertEqual(str(self.airport3.identifyPlanesPassportThreeLetters()), "[Plane(4, Qatar, 30, New York and [Passenger(Laura Anton, 631fae)])]")

    def test_identifyPassengersGivenPlaneGivenString(self):
        self.assertEqual(str(self.airport1.identifyPassengersGivenPlaneGivenString("1", "M")), "[Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)]")
        self.assertEqual(str(self.airport2.identifyPassengersGivenPlaneGivenString("3", "D")), "[Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc)]")
        self.assertEqual(str(self.airport3.identifyPassengersGivenPlaneGivenString("4", "o")), "[Passenger(Laura Anton, 631fae)]")

    def test_identifyPlanesPassengerGivenName(self):
        self.assertEqual(str(self.airport1.identifyPlanesPassengerGivenName("Ana", "Tatar")), "[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc)])]")
        self.assertEqual(str(self.airport2.identifyPlanesPassengerGivenName("Georgia", "Oltean")), "[]")
        self.assertEqual(str(self.airport2.identifyPlanesPassengerGivenName("Denisa", "Muntean")), "[Plane(3, Lufthansa, 15, Bucharest and [Passenger(Georgiana Moldovan, 444abc), Passenger(Denisa Muntean, 555ccc), Passenger(George Oltean, 666ddd)])]")

    def test_groupKPassengers(self):
        self.assertEqual(str(self.plane11.groupKPassengers(3)), "[[Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Cosmin Pop, 213cc)], [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Cosmin Pop, 213cc)], [Passenger(Ana Tatar, 111aaa), Passenger(Mihai Horea, 111ccc), Passenger(Cosmin Pop, 213cc)], [Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc), Passenger(Cosmin Pop, 213cc)]]")
        try:
            print(self.plane22.groupKPassengers(-3))
        except ValueError as ve:
            print(ve)
        self.assertEqual(str(self.plane22.groupKPassengers(2)), "[[Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]]")

    def test_groupKPlanes(self):
        self.assertEqual(str(self.airport4.groupKPlanes(3)), "[[Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc), Passenger(Cosmin Pop, 213cc)]), Plane(2, tarom, 10, Paris and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(5, Singapore Airline, 35, Dubai and [Passenger(Mircea Eliade, 935gfs), Passenger(Mihai Eminescu, 258dgg)])], [Plane(1, wizz, 5, Paris and [Passenger(Ana Tatar, 111aaa), Passenger(Anamaria Anca, 111bbb), Passenger(Mihai Horea, 111ccc), Passenger(Cosmin Pop, 213cc)]), Plane(2, tarom, 10, Paris and [Passenger(David Bobb, 223abc), Passenger(Ioana Vlad, 223gda)]), Plane(5, Singapore Airline, 35, Dubai and [Passenger(Mircea Eliade, 935gfs), Passenger(Mihai Eminescu, 258dgg)])]]")
        try:
            print(self.airport4.groupKPlanes(-2))
        except ValueError as ve:
            print(ve)
        try:
            print(self.airport4.groupKPlanes(20))
        except ValueError as ve:
            print(ve)

    def test_Controller(self):
        self.controller.addPlaneInAirport("1", "qq", 30, "a")
        self.controller.addPassengerInPlane("1", "aa", "bb", "123")
        self.controller.addPassengerInPlane("1", "ana", "sabina", "5sf")
        self.controller.addPlaneInAirport("22", "blueair", 30, "b")
        self.controller.addPassengerInPlane("22", "cristi", "bb", "123")
        self.controller.addPassengerInPlane("22", "david", "mm", "123abc")
        print(self.controller.identifyPlanesPassengerGivenNameInPlane("aa", "bb"))


