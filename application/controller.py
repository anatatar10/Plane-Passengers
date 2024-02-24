from infrastructure.airport import Airport
from infrastructure import searchBy as searchBy

class Controller:
    def __init__(self):
        self.__repo = Airport()

    def addPassengerInPlane(self, nameNumber, firstName, lastName, passportNumber):
        self.__repo.searchPlaneByNameNumber(nameNumber).addPassenger(firstName, lastName, passportNumber)

    def getAllPassengersInPlane(self, nameNumber):
        return self.__repo.searchPlaneByNameNumber(nameNumber).getAllPassengers()

    def getPassengerAtGivenIndexInPlane(self, nameNumber, index):
        return self.__repo.searchPlaneByNameNumber(nameNumber).getPassengerAtGivenIndex(index)

    def updatePassengerAtGivenIndexInPlane(self, nameNumber, index, firstName, lastName, passportNumber):
        self.__repo.searchPlaneByNameNumber(nameNumber).updatePassengerAtGivenIndex(index, firstName, lastName, passportNumber)

    def deletePassengerAtGivenIndexInPlane(self, nameNumber, index):
        self.__repo.searchPlaneByNameNumber(nameNumber).deletePassengerAtGivenIndex(index)

    def addPlaneInAirport(self, nameNumber, airline, numberOfSeats, destination):
        self.__repo.addPlane(nameNumber, airline, numberOfSeats, destination)

    def getAllPlanesInAirport(self):
        return self.__repo.getAllPlanes()

    def getPlaneAtGivenIndexInAirport(self, index):
        return self.__repo.getPlaneAtGivenIndex(index)

    def updatePlaneAtGivenIndexInAirport(self, index, nameNumber, airline, numberOfSeats, destination):
        return self.__repo.updatePlaneAtGivenIndex(index, nameNumber, airline, numberOfSeats, destination)

    def deletePlaneAtGivenIndexInAirport(self, index):
        self.__repo.deletePlaneAtGivenIndex(index)

    def sortPassengersByLastNameInPlaneAsc(self, nameNumber):
        return self.__repo.searchPlaneByNameNumber(nameNumber).sortPassengersByLastNameAscending()

    def sortPassengersByLastNameInPlaneDesc(self, nameNumber):
        return self.__repo.searchPlaneByNameNumber(nameNumber).sortPassengersByLastNameDescending()

    def sortPlanesByNumOfPassengersInAirportAscending(self):
        return self.__repo.sortPlanesByNumOfPassengersAscending()

    def sortPlanesByNumOfPassengersInAirportDescending(self):
        return self.__repo.sortPlanesByNumOfPassengersDescending()

    def sortPlanesByPrefixInAirportAscending(self, prefix):
        return self.__repo.sortPlanesByPrefixAscending(prefix)

    def sortPlanesByPrefixInAirportDescending(self, prefix):
        return self.__repo.sortPlanesByPrefixDescending(prefix)

    def sortPlanesByConcatenationInAirportAscending(self):
        return self.__repo.sortPlanesByConcatenationAscending()

    def sortPlanesByConcatenationInAirportDescending(self):
        return self.__repo.sortPlanesByConcatenationDescending()

    def identifyPlanesPassportThreeLettersinAirport(self):
        return self.__repo.identifyPlanesPassportThreeLetters()

    def identifyPassengersGivenPlaneGivenStringInPlane(self, nameNumber, givenString):
        return self.__repo.identifyPassengersGivenPlaneGivenString(nameNumber, givenString)

    def identifyPlanesPassengerGivenNameInPlane(self, givenFirstName, givenLastName):
        return self.__repo.identifyPlanesPassengerGivenName(givenFirstName, givenLastName)

    def groupKPassengers(self, nameNumber, k):
        #return self.__repo[self.__repo.searchPlaneByNameNumber(nameNumber)].groupKPassengers(k)
        return self.__repo.searchPlaneByNameNumber(nameNumber).groupKPassengers(k)

    def groupKPlanes(self, k):
        return self.__repo.groupKPlanes(k)

    @property
    def airport(self):
        return self.__repo.listOfPlanes