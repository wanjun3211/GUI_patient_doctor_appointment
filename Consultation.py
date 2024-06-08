from Doctor import Doctor
from Patient import Patient

class Consultation:
    def __init__(self, date, doctor, patient, reason, fee):
        self.__myCDate = date
        self.__myCDoctor = doctor
        self.__myCPatient = patient
        self.__myCReason = reason
        self.__myFee = fee

    @property
    def date(self):
        return self.__myCDate

    @date.setter
    def date(self, value):
        self.__myCDate = value

    @property
    def doctor(self):
        return self.__myCDoctor

    @doctor.setter
    def doctor(self, value):
        self.__myCDoctor = value

    @property
    def patient(self):
        return self.__myCPatient

    @patient.setter
    def patient(self, value):
        self.__myCPatient = value

    @property
    def reason(self):
        return self.__myCReason

    @reason.setter
    def reason(self, value):
        self.__myCReason = value

    @property
    def fee(self):
        return self.__myFee

    @fee.setter
    def fee(self, value):
        self.__myFee = value

    def __str__(self):
        return f"Consultation Date: {self.date}\nDoctor: {self.doctor.fName} {self.doctor.lName}\nPatient: {self.patient.fName} {self.patient.lName}\nReason: {self.reason}\nFee: ${self.fee:.2f}"
