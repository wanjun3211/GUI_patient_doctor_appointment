from Doctor import Doctor

class Patient:
    __nextID = 1000

    def __init__(self, fName, lName):
        self.__myDoctor = None
        self.__myPatientFName = fName
        self.__myPatientLName = lName
        self.__myPatientID = Patient.__nextID
        Patient.__nextID += 1

    def __str__(self):
        return f"Patient: {self.__myPatientFName} {self.__myPatientLName}, ID: {self.__myPatientID}"

    @property
    def doctor(self):
        return self.__myDoctor

    @doctor.setter
    def doctor(self, newDoctor):
        self.__myDoctor = newDoctor

    @property
    def fName(self):
        return self.__myPatientFName

    @fName.setter
    def fName(self, value):
        self.__myPatientFName = value

    @property
    def lName(self):
        return self.__myPatientLName

    @lName.setter
    def lName(self, value):
        self.__myPatientLName = value

    @property
    def patientID(self):
        return self.__myPatientID

    @patientID.setter
    def patientID(self, value):
        print("Warning: Changing doctor ID directly is not allowed.")

    @staticmethod
    def resetIDCounter():
        Patient.__nextID = 1000



