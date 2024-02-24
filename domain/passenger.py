class Passenger:
    def __init__(self, firstName, lastName, passportNumber):
        """
        Create a passenger object with first name, last name and passport number
        :param firstName:
        :type firstName: str
        :param lastName:
        :type lastName: str
        :param passportNumber:
        :type passportNumber: str
        """
        self.__firstName = firstName
        self.__lastName = lastName
        self.__passportNumber = passportNumber

        # getter functions for the properties
        # the name of the function becomes the name of the property

    @property
    def firstName(self):
        """
        Get the first name of the passenger
        :return:
        :rtype: str
        """
        return self.__firstName

    @property
    def lastName(self):
        """
        Get the last name of the passenger
        :return:
        :rtype: str
        """
        return self.__lastName

    @property
    def passportNumber(self):
        """
        Get the passport number of the passenger
        :return:
        :rtype: str
        """
        return self.__passportNumber


    @firstName.setter
    def firstName(self, newFirstName):
        """
        Set the first name of the passenger
        :return:
        :rtype: str
        """
        self.__firstName = newFirstName

    @lastName.setter
    def lastName(self, newLastName):
        """
        Set the last name of the passenger
        :return:
        :rtype: str
        """
        self.__lastName = newLastName

    @passportNumber.setter
    def passportNumber(self, newPassportNumber):
        """
        Set the passport number of the passenger
        :return:
        :rtype: str
        """
        self.__passportNumber = newPassportNumber


    def __str__(self):
        """
        Return the string representation of the passenger.
        :return:
        :rtype:
        """

        return f"Passenger({self.__firstName} {self.__lastName}, {self.__passportNumber})"

    def __repr__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Check if two passenger objects are equal by comparing their properties
        :param other:
        :type other: Passenger
        :return:
        :rtype: bool
        """
        return self.__firstName == other.__firstName and self.__lastName == other.__lastName and self.__passportNumber == other.__passportNumber



