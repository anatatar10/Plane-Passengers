import infrastructure.plane as plane
from infrastructure import sortBy
from infrastructure import searchBy
from infrastructure import backtrackFunction
from infrastructure import searchBy

class Airport: #planeRepository
    def __init__(self, listOfPlanes = None):
        """
        Creating a repository containing planes
        """
        self.__listOfPlanes = []
        if listOfPlanes is not None:
            for planes in listOfPlanes:
                if isinstance(planes, plane.Plane):
                    self.__listOfPlanes.append(planes)

    @property
    def listOfPlanes(self):
        """
        Get the list of planes in the airport
        :return:
        :rtype: list
        """
        return self.__listOfPlanes[:]

    @listOfPlanes.setter
    def listOfPlanes(self, newListOfPlanes = []):
        """
        Set the list of planes in the airport
        :return:
        :rtype: list
        """

        self.__listOfPlanes = newListOfPlanes[:]

    def __isPlaneUnique(self, pl):
        for x in self.__listOfPlanes:
            if x == pl:
                return False
        return True

    def __str__(self):
        """
        Return the string representation of the airport.
        :return:
        :rtype:
        """

        return f"Airport({self.__listOfPlanes})"

    def addPlane(self, nameNumber, airline, numberOfSeats, destination, listOfPassengers = []):
        """
        CRUD operation: add plane to the airport repository
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
        :return:
        """
        if numberOfSeats > 0 and len(listOfPassengers) < numberOfSeats:
            self.__listOfPlanes.append(plane.Plane(nameNumber, airline, numberOfSeats, destination, listOfPassengers))

        else:
            raise ValueError("Too many passengers")

    def getAllPlanes(self):
        """
        CRUD operation: Get all the planes from the airport repository
        :return:
        """
        return self.__listOfPlanes[:]

    def __isIndexCorrectPlane(self, index):
        """
        Check if the index is correct in the list of planes
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__listOfPlanes) or 0 == index == len(self.__listOfPlanes)

    def getPlaneAtGivenIndex(self, index):
        """
        Get a plane at a given index
        :param index:
        :type index: int
        :return:
        :rtype: Airport
        """
        if self.__isIndexCorrectPlane(index):
            return self.__listOfPlanes[index]
        else:
            raise IndexError("Index invalid")

    def __getitem__(self, index):
        return self.getPlaneAtGivenIndex(index)

    def updatePlaneAtGivenIndex(self, index, nameNumber, airline, numberOfSeats, destination, listOfPassengers = []):
        """
        Update a plane at a given index
        :param index:
        :type index: int
        :param nameNumber:
        :type nameNumber: int, str
        :param airline:
        :type airline: str
        :param numberOfSeats:
        :type numberOfSeats: int
        :param destination:
        :type destination: str
        :param listOfPassengers:
        :type listOfPassengers: list
        :return:
        :rtype: Plane
        """
        if self.__isIndexCorrectPlane(index):
            a = self.__listOfPlanes[index]
            a.nameNumber = nameNumber
            a.airline = airline
            a.numberOfSeats = numberOfSeats
            a.destination = destination
            a.listOfPassengers = listOfPassengers
            return a
        else:
            raise IndexError("Index out of range")

    def deletePlaneAtGivenIndex(self, index):
        """
        Delete a plane by index
        :param index:
        :type index: int
        :return:
        :rtype: Airport
        """
        if self.__isIndexCorrectPlane(index):
            del self.__listOfPlanes[index]
        else:
            raise IndexError("Index out of range")

    def sortPlanesByNumOfPassengersAscending(self):
        """
        Ex 4: Sort planes according to the number of passengers in ascending order
        :return:
        """
        self.__listOfPlanes = sortBy.bubbleSort(self.__listOfPlanes, criterian=lambda p1, p2: len(p1.listOfPassengers) > len(p2.listOfPassengers))

    def sortPlanesByNumOfPassengersDescending(self):
        """
        Ex 4: Sort planes according to the number of passengers in descending order
        :return:
        """
        self.__listOfPlanes = sortBy.bubbleSort(self.__listOfPlanes, criterian=lambda p1, p2: len(p1.listOfPassengers) < len(p2.listOfPassengers))

    def sortPlanesByPrefixAscending(self, prefix = ""):
        """
        Ex 5: Sort planes according to the number of passengers with the first name starting with a given substring in ascending order
        :param prefix:
        :return:
        """
        self.__listOfPlanes = sortBy.bubbleSort(self.__listOfPlanes, criterian=lambda p1, p2: p1.checkPrefix(prefix) > p2.checkPrefix(prefix))

    def sortPlanesByPrefixDescending(self, prefix = ""):
        """
        Ex 5: Sort planes according to the number of passengers with the first name starting with a given substring in descending order
        :param prefix:
        :return:
        """
        self.__listOfPlanes = sortBy.bubbleSort(self.__listOfPlanes, criterian=lambda p1, p2: p1.checkPrefix(prefix) < p2.checkPrefix(prefix))

    def sortPlanesByConcatenationAscending(self):
        """
        Ex 6: Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination ascending
        :return:
        """
        self.__listOfPlanes = sortBy.bubbleSort(self.__listOfPlanes, criterian=lambda p1, p2: p1.concatenationNumPassDest() > p2.concatenationNumPassDest())

    def sortPlanesByConcatenationDescending(self):
        """
        Ex 6: Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination descending
        :return:
        """
        self.__listOfPlanes = sortBy.bubbleSort(self.__listOfPlanes, criterian=lambda p1, p2: p1.concatenationNumPassDest() < p2.concatenationNumPassDest())

    def identifyPlanesPassportThreeLetters(self): #7
        """
        Ex 7: Identify  planes  that  have  all the passengers  with  passport  numbers  starting  with  the  same 3 letters
        :return:
        :rtype: list
        """
        result = []
        for pl in self.__listOfPlanes:
            if len(searchBy.searchBy(pl.listOfPassengers[0].passportNumber[0:3], pl.listOfPassengers[1:], condition=lambda x1, x2: x1 == x2.passportNumber[0:3])) == len(pl.listOfPassengers) - 1:
                result.append(pl)
        return result[:]

    def identifyPassengersGivenPlaneGivenString(self, givenNameNumber, stringParameter = ""):
        """
        Ex 8: Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  namecontain a string given as parameter
        :param givenNameNumber:
        :param stringParameter:
        :return:
        """
        result = []
        for pl in self.__listOfPlanes:
            if pl.nameNumber == givenNameNumber:
                return(searchBy.searchBy(stringParameter, pl.listOfPassengers, condition=lambda x1, x2: x1.lower() in x2.firstName.lower() or x1.lower() in x2.lastName.lower()))


    def identifyPlanesPassengerGivenName(self, givenFName = "", givenLName = ""):
        """
        Ex 9: Identify plane/planes where there is a passenger with given name
        :param givenFName:
        :param givenLName:
        :return:
        """
        result = []
        for pl in self.__listOfPlanes:
            if len(searchBy.searchBy(givenFName+givenLName, pl.listOfPassengers, condition=lambda x1, x2: x1 == x2.firstName+x2.lastName)) > 0:
                result.append(pl)
        return result[:]

    def searchPlaneByNameNumber(self, nameNumber):
        return searchBy.searchBy(nameNumber, self.listOfPlanes, condition=lambda x1, x2: x1 == x2.nameNumber)[0]

    def groupKPlanes(self, k):
        """
        Form  groups  of  𝒌  planes  with  the  same  destination  but  belonging  to  different  airline companies (𝒌 is a value given by the user)
        :param k:
        :return:
        """
        if k > 1 and k <= len(self.__listOfPlanes):
            return list(backtrackFunction.backtrackFunction(k, self.__listOfPlanes, [], isCorrect=lambda x:
            len(searchBy.searchBy(x[-1].airline, x, lambda a, b: a.upper() == b.airline.upper())) == 1 and
            len(searchBy.searchBy(x[-1].destination, x, lambda a, b: a.upper() == b.destination.upper())) == len(x)))
        else:
            raise ValueError("K not valid")

if __name__ == "__main__":
    repo = Airport([plane.Plane("1", "wizz", 10, "Paris", [plane.passenger.Passenger("Ana", "Tatar", "aaa111dad"),
                                                         plane.passenger.Passenger("Anamaria", "Vlad", "aaa111aaa")]),
                    plane.Plane("2", "tarom", 20, "Dubai", [plane.passenger.Passenger("David", "Bobb", "aaa222ddd"),
                                                          plane.passenger.Passenger("Anamaria", "Tatar", "222")]),
                    plane.Plane("3", "lufthansa", 5, "London", [plane.passenger.Passenger("Anastasia", "Horea", "444"),
                                                              plane.passenger.Passenger("Cristina", "Anca", "555"),
                                                              plane.passenger.Passenger("Raluca", "Crisan", "666")])])
    #repo.updatePlaneAtGivenIndex(5, 2, "tarom", 2, 'bucharest', [plane.passenger.Passenger("Mihai", "Viteazu", 333)])
    #repo.deletePlaneAtGivenIndex(1)
    repo.identifyPlanesPassportThreeLetters()
    print(repo)

