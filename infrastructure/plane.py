import domain.passenger as passenger
from infrastructure import sortBy
from infrastructure import backtrackFunction
from infrastructure import searchBy

class Plane: #passengerRepository
    def __init__(self, nameNumber, airline, numberOfSeats, destination, listOfPassengers = []):
        """
        Create a plane object with number, airline, number of seats, destination and list of passengers
        :param nameNumber:
        :type nameNumber: str
        :param airline:
        :type airline: str
        :param numberOfSeats:
        :type numberOfSeats: int
        :param destination:
        :type destination: str
        :param listOfPassengers:
        :type listOfPassengers: list
        """
        self.__nameNumber = nameNumber
        self.__airline = airline
        if numberOfSeats > 0:
            self.__numberOfSeats = numberOfSeats
        else:
            raise ValueError("The number of seats must be > 0")
        self.__destination = destination



        """
        Creating a repository containing passengers
        """

        self.__listOfPassengers = []
        if listOfPassengers is not None:
            for passengers in listOfPassengers:
                if self.__numberOfSeats > len(self.listOfPassengers):
                    if isinstance(passengers, passenger.Passenger):
                        self.__listOfPassengers.append(passengers)
                else:
                    raise ValueError("No more seats available in the plane")



    # getter functions for the properties
    # the name of the function becomes the name of the property

    @property
    def nameNumber(self):
        """
        Get the name/number of the plane
        :return:
        :rtype: int, str
        """
        return self.__nameNumber

    @property
    def airline(self):
        """
        Get the airline of the plane
        :return:
        :rtype: str
        """
        return self.__airline

    @property
    def numberOfSeats(self):
        """
        Get the number of seats in the plane
        :return:
        :rtype: int
        """
        return self.__numberOfSeats


    @property
    def destination(self):
        """
        Get the destination of the plane
        :return:
        :rtype: str
        """
        return self.__destination

    @property
    def listOfPassengers(self):
        """
        Get the list of passengers in the plane
        :return:
        :rtype: list
        """
        return self.__listOfPassengers[:]

    # setter functions for the properties

    @nameNumber.setter
    def nameNumber(self, newNameNumber):
        """
        Set the name/number of the plane
        :return:
        :rtype: str
        """
        self.__nameNumber = newNameNumber


    @airline.setter
    def airline(self, newAirline):
        """
        Set the airline of the plane
        :return:
        :rtype: str
        """
        self.__airline = newAirline

    @numberOfSeats.setter
    def numberOfSeats(self, newNumberOfSeats):
        """
        Set the number of seats in the plane
        :return:
        :rtype: int
        """
        if newNumberOfSeats > 0:
            self.__numberOfSeats = newNumberOfSeats
        else:
            raise ValueError("The number of seats must be > 0")

    @destination.setter
    def destination(self, newDestination):
        """
        Set the destination of the plane
        :return:
        :rtype: str
        """
        self.__destination = newDestination

    @listOfPassengers.setter
    def listOfPassengers(self, newListOfPassengers = []):
        """
        Set the list of passengers in the plane
        :return:
        :rtype: list
        """
        if len(newListOfPassengers) < self.numberOfSeats:
            self.__listOfPassengers = newListOfPassengers[:]
        else:
            raise ValueError("The number of passengers must be less than the number of seats")

    def __str__(self):
        """
        Return the string representation of the plane.
        :return:
        :rtype:
        """

        return f"Plane({self.__nameNumber}, {self.__airline}, {self.__numberOfSeats}, {self.__destination} and {self.__listOfPassengers})"

    def __repr__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Check if two plane objects are equal by comparing their properties
        :param other:
        :type other: Plane
        :return:
        :rtype: bool
        """
        return self.__nameNumber == other.__nameNumber and self.__numberOfSeats == other.__numberOfSeats and self.__destination == other.__destination and self.__listOfPassengers[:] == other.__listOfPassengers[:]

    def __isPassportNumberUnique(self, passportNumber):
        """
        Check if the passport number is unique in the list of passengers
        :param passportNumber:
        :return:
        :rtype: bool
        """
        for x in self.__listOfPassengers:
            if x.passportNumber == passportNumber:
                return False
        return True

    def addPassenger(self, firstName, lastName, passportNumber):

        """
        CRUD operation: add passenger to the plane repository
        :param firstName:
        :type firstName: str
        :param lastName:
        :type lastName: str
        :param passportNumber:
        :type passportNumber: str
        :return:
        """

        if self.__isPassportNumberUnique(passportNumber):
            self.__listOfPassengers.append(passenger.Passenger(firstName, lastName, passportNumber))
        else:
            print("The passport number already exists")

    def getAllPassengers(self):
        """
        CRUD operation: get all passengers from the plane repository
        :return:
        :rtype: list
        """
        return self.__listOfPassengers[:]

    def __isIndexCorrect(self, index):
        """
        Check if the index is correct in the list of passengers
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__listOfPassengers) or 0 == index == len(self.__listOfPassengers)

    def getPassengerAtGivenIndex(self, index):
        """
        Get a passenger at a given index
        :param index:
        :type index: int
        :return:
        :rtype: Plane
        """
        if self.__isIndexCorrect(index):
            return self.__listOfPassengers[index]
        else:
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        return self.getPassengerAtGivenIndex(index)

    def updatePassengerAtGivenIndex(self, index, firstName, lastName, passportNumber):
        """
        Update a passenger at a given index
        :param index:
        :type index: int
        :param firstName:
        :type firstName: str
        :param lastName:
        :type lastName: str
        :param passportNumber:
        :type passportNumber: int
        :return:
        :rtype: Plane
        """
        if self.__isIndexCorrect(index):
            p = self.__listOfPassengers[index]
            p.firstName = firstName
            p.lastName = lastName
            p.passportNumber = passportNumber
            return p
        else:
            raise IndexError("Index out of range")

    def deletePassengerAtGivenIndex(self, index):
        """
        Delete a point by index
        :param index:
        :type index: int
        :return:
        :rtype: Plane
        """
        if self.__isIndexCorrect(index):
            del self.__listOfPassengers[index]
        else:
            raise IndexError("Index out of range")

    def sortPassengersByLastNameAscending(self):
        """
        ex 3: Sort the passengers in a plane by last name in ascending order
        :return:
        """
        self.__listOfPassengers = sortBy.bubbleSort(self.listOfPassengers, criterian=lambda p1, p2: p1.lastName > p2.lastName)

    def sortPassengersByLastNameDescending(self):
        """
        ex 3: sort the passengers in a plane by last name in ascending order
        :return:
        """
        self.__listOfPassengers = sortBy.bubbleSort(self.listOfPassengers, criterian=lambda p1, p2: p1.lastName < p2.lastName)

    def checkPrefix(self, prefix):
        """
        Function to check the number of passengers in a plane with the first name starting with a given substring
        :param prefix:
        :return:
        :rtype: int
        """
        count = 0
        for p in self.__listOfPassengers:
            if p.firstName[:len(prefix)] == prefix: ##first n letters according to the length of the given prefix
                count = count + 1
        return count

    def concatenationNumPassDest(self):
        """
        Function to concatenate the number of passengers in the plane and the destination
        :return:
        :rtype: str
        """
        stringLength = str(len(self.__listOfPassengers))
        string1 = stringLength + self.__destination
        return string1

    def groupKPassengers(self, k):
        """
        Form groups of 𝒌 passengers from the same plane but with different last names (𝒌 is a value given by the user)
        :param k: the no. of passengers in a group
        :return:
        """
        if k > 0:
            return list(backtrackFunction.backtrackFunction(k, self.__listOfPassengers, [], isCorrect=lambda x:
            len(searchBy.searchBy(x[-1].lastName, x, lambda a, b: a == b.lastName)) == 1))
        else:
            raise ValueError("K not valid")


if __name__ == "__main__":
    repo = Plane(1, "wizz", 5, "Paris", [passenger.Passenger("Ana", "Tatar", "111"),
                                         passenger.Passenger("Anamaria", "Vlad", "13413"),
                                         passenger.Passenger("Mihai", "Horea", "333")])
    print(repo.concatenationNumPassDest())
    print(repo)
