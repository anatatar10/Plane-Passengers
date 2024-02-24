from data_examples import dataExamples
from application import controller as cont


def printMenu():
    print("MENU:")
    print("-2 - print data examples")
    print("-1 - print menu")
    print(" 0 - exit program")
    print(" 1 - Add a passenger to the passenger repository(Plane)")
    print(" 2 - Get all passengers")
    print(" 3 - Get a passenger at a given index")
    print(" 4 - Update a passenger at a given index ")
    print(" 5 - Delete a passenger at a given index ")
    print(" 6 - Add a plane to the plane repository(Airport)")
    print(" 7 - Get all planes")
    print(" 8 - Get a plane at a given index")
    print(" 9 - Update a plane at a given index ")
    print(" 10 - Delete a plane at a given index ")
    print(" 11 - Sort the passengers in a plane by last name ascending")
    print(" 12 - Sort the passengers in a plane by last name descending")
    print(" 13 - Sort planes according to the number of passengers ascending")
    print(" 14 - Sort planes according to the number of passengers descending")
    print(" 15 - Sort planes according to the number of passengers with the first name starting with a given substring ascending")
    print(" 16 - Sort planes according to the number of passengers with the first name starting with a given substring descending")
    print(" 17 - Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination ascending")
    print(" 18 - Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination descending")
    print(" 19 - Identify  planes  that  have  all the passengers  with  passport  numbers  starting  with  the  same 3 letters")
    print(" 20 - Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  namecontain a string given as parameter")
    print(" 21 - Identify plane/planes where there is a passenger with given name")
    print(" 22 - Form groups of 𝒌 passengers from the same plane but with different last names (𝒌 is a value given by the user)")
    print(" 23 - Form  groups  of  𝒌  planes  with  the  same  destination  but  belonging  to  different  airline companies (𝒌 is a value given by the user)")
    print(" Add a plane first, then passengers ")

def start():
    print()
    controllerRepo = cont.Controller()
    printMenu()
    command = None
    while command != 0:  # while True
        try:  # catches all conversion errors
            command = int(input(">>> "))
            if command == -2:
                dataExamples()
            elif command == -1:
                printMenu()
            elif command == 0:
                print("program ended")
            elif command == 1:
                nameNumber = input("Name number of the plane: ")
                firstName = input("First name: ")
                lastName = input("Last name: ")
                passportNumber = input("Passport number: ")
                try:
                    controllerRepo.addPassengerInPlane(nameNumber, firstName, lastName, passportNumber)
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                nameNumber = input("Name number of the plane: ")
                try:
                    controllerRepo.getAllPassengersInPlane(nameNumber)
                except ValueError as ve:
                    print(ve)
            elif command == 3:
                nameNumber = input("Name number of the plane: ")
                index = int(input("Index of the plane: "))
                try:
                    controllerRepo.getPassengerAtGivenIndexInPlane(nameNumber, index)
                except IndexError as ie:
                    print(ie)
            elif command == 4:
                nameNumber = input("Name number of the plane: ")
                index = int(input("Index of the plane:"))
                firstName = input("New first name: ")
                lastName = input("New last name: ")
                passportNumber = input("New passport number: ")
                try:
                    controllerRepo.updatePassengerAtGivenIndexInPlane(nameNumber, index, firstName, lastName, passportNumber)
                except ValueError as ve:
                    print(ve)
            elif command == 5:
                index = int(input("Index of the plane: "))
                try:
                    controllerRepo.deletePlaneAtGivenIndexInAirport(index)
                except IndexError as ie:
                    print(ie)
            elif command == 6:
                nameNumber = input("Name number of the plane: ")
                airline = input("Airline: ")
                numberOfSeats = int(input("Number of seats: "))
                destination = input("Destination: ")
                try:
                    controllerRepo.addPlaneInAirport(nameNumber, airline, numberOfSeats, destination)
                except ValueError as ve:
                    print(ve)
            elif command == 7:
                print(controllerRepo.getAllPlanesInAirport())
            elif command == 8:
                index = int(input("Index of the plane: "))
                try:
                    print(controllerRepo.getPlaneAtGivenIndexInAirport(index))
                except IndexError as ie:
                    print(ie)
            elif command == 9:
                index = int(input("Index of the plane: "))
                nameNumber = input("New name number of the plane: ")
                airline = input("New airline: ")
                numberOfSeats = int(input("New number of seats: "))
                destination = input("New destination: ")
                print("If you also want to modify the list of passengers, please delete them(command = 5) or update them(command = 4) ")
                try:
                    controllerRepo.updatePlaneAtGivenIndexInAirport(index, nameNumber, airline, numberOfSeats, destination)
                except IndexError as ie:
                    print(ie)
            elif command == 10:
                index = int(input("Index of the plane: "))
                try:
                    controllerRepo.deletePlaneAtGivenIndexInAirport(index)
                except IndexError as ie:
                    print(ie)
            elif command == 11:
                nameNumber = input("Name number of the plane: ")
                try:
                    print(controllerRepo.sortPassengersByLastNameInPlaneAsc(nameNumber))
                except ValueError as ve:
                    print(ve)
            elif command == 12:
                nameNumber = input("Name number of the plane: ")
                try:
                    print(controllerRepo.sortPassengersByLastNameInPlaneDesc(nameNumber))
                except ValueError as ve:
                    print(ve)
            elif command == 13:
                print(controllerRepo.sortPlanesByNumOfPassengersInAirportAscending())
            elif command == 14:
                print(controllerRepo.sortPlanesByNumOfPassengersInAirportDescending())
            elif command == 15:
                prefix = input("Prefix: ")
                print(controllerRepo.sortPlanesByPrefixInAirportAscending(prefix))
            elif command == 16:
                prefix = input("Prefix: ")
                print(controllerRepo.sortPlanesByPrefixInAirportDescending(prefix))
            elif command == 17:
                print(controllerRepo.sortPlanesByConcatenationInAirportAscending())
            elif command == 18:
                print(controllerRepo.sortPlanesByConcatenationInAirportDescending())
            elif command == 19:
                print(controllerRepo.identifyPlanesPassportThreeLettersinAirport())
            elif command == 20:
                nameNumber = input("Name number of the plane: ")
                givenString = input("Searched string in first/last name")
                print(controllerRepo.identifyPassengersGivenPlaneGivenStringInPlane(nameNumber,givenString))
            elif command == 21:
                givenFName = input("Searched first name in plane/planes")
                givenLName = input("Searched last name in plane/planes")
                print(controllerRepo.identifyPlanesPassengerGivenNameInPlane(givenFName, givenLName))
            elif command == 22:
                k = int(input("Number of groups of passengers: "))
                try:
                    print(controllerRepo.groupKPassengers(k))
                except ValueError as ve:
                    print(ve)
            elif command == 23:
                k = int(input("Number of groups of planes: "))
                try:
                    print(controllerRepo.groupKPlanes(k))
                except ValueError as ve:
                    print(ve)
            else:
                print("invalid command")
        except ValueError:
            print("invalid type entered")







