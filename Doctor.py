class Doctor:
    __nextID = 1000

    def __init__(self, fName, lName, spec):
        self.__myDoctorFName = fName
        self.__myDoctorLName = lName
        self.__myDoctorLID = Doctor.__nextID
        self.__myDoctorSpec = spec
        Doctor.__nextID += 1

    def __str__(self):
        return f"Doctor: {self.__myDoctorFName} {self.__myDoctorLName}, ID: {self.__myDoctorLID}, Specialization: {self.__myDoctorSpec}"

    
    @property
    def fName(self):
        return self.__myDoctorFName

    @fName.setter
    def fName(self, value):
        self.__myDoctorFName = value

    @property
    def lName(self):
        return self.__myDoctorLName

    @lName.setter
    def lName(self, value):
        self.__myDoctorLName = value

    @property
    def spec(self):
        return self.__myDoctorSpec

    @spec.setter
    def spec(self, value):
        self.__myDoctorSpec = value

    @property
    def doctorID(self):
        return self.__myDoctorLID

    @doctorID.setter
    def doctorID(self, value):
        print("Warning: Changing doctor ID directly is not allowed.")

    @staticmethod
    def resetIDCounter():
        Doctor.__nextID = 1000



   
        


    

