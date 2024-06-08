"""!@brief example Python program with Doxygen style comments"""

##
# @mainpage Clinic Application Project
# 
# @section description_main Description 
# An example Python program demonstrating how to use Doxygen style comments for
# generating source code documentation in HTML
#
# @section notes_main Notes
# Add special notes here
# Imports 

from Doctor import Doctor 
from Patient import Patient
from Consultation import Consultation


class ClinicController:
    def __init__(self, clinicName):
        self.clinicName = clinicName
        self.doctorList = []
        self.patientList = []
        self.consulationList = []

    def addDoctor(self, fName, lName, spec):
        aDoctor = Doctor(fName, lName, spec)
        self.doctorList.append(aDoctor)

    def addPatient(self, fName, lName):
        aPatient = Patient(fName, lName)
        self.patientList.append(aPatient)

    def assignDoctorTOpatient(self, aPatient, aDoctor):
        aPatient.doctor = aDoctor
        return ("assign docotor:"+str(aPatient.doctor.doctorID)+" "+aPatient.doctor.fName+" "+aPatient.doctor.lName+' '+"to"+" "+str(aPatient.patientID)
        +" "+aPatient.fName+" "+aPatient.lName)


    def addConsulation(self, date, doctor, patient, reason, fee):
            aconsulation = Consultation(date, doctor, patient, reason, fee)
            self.consulationList.append(aconsulation)
            return f"Consultation Date: {aconsulation.date}\nDoctor: {aconsulation.doctor.fName} {aconsulation.doctor.lName}\nPatient: {aconsulation.patient.fName} {aconsulation.patient.lName}\nReason: {aconsulation.reason}\nFee: ${aconsulation.fee:.2f}"

# this function is used in GUI def assign_doctor() in order to find the doctor object by user selction in the doctor list 
    def searchDoctor_for_assign(self, input):
        for doctor in self.doctorList:
            if doctor.fName == input or doctor.lName == input or doctor.spec == input or doctor.doctorID == input:
                    return doctor
             


    def searchDoctor(self, input_str):
        matching_doctors = []

        try:
            input_num = int(input_str)  # Convert input to integer if possible
        except ValueError:
            input_num = None

        for doctor in self.doctorList:
            if (
                doctor.fName.lower() == input_str.lower() or
                doctor.lName.lower() == input_str.lower() or
                doctor.spec.lower() == input_str.lower() or
                doctor.doctorID == input_num
            ):
                matching_doctors.append(doctor)

        if not matching_doctors:
            return "No matched doctor. Please pay attention to your input. You should provide a doctor's first name, last name, specialization, or an ID number."

        result = ""
        for doctor in matching_doctors:
            info1 = f"Doctor: {doctor.fName} {doctor.lName}, ID: {doctor.doctorID}, Specialization: {doctor.spec}\n"
            info2 = "Patient list:\n"
            info3 = ''
            info4 = "Consultations:\n"
            info5 = ''
            patient_list = []

            for consultation in self.consulationList:
                if consultation.doctor == doctor:
                    info5 += f"{consultation.date} Patient ID: {consultation.patient.patientID}, Patient: {consultation.patient.fName} {consultation.patient.lName}, Reason: {consultation.reason} Fee: ${consultation.fee:.2f}\n"
                    patient_list.append(consultation.patient)
            if info5:
                # remove repeated patient and show the same patient only once
                patient_list = list(dict.fromkeys(patient_list))
                for patient in patient_list:
                    info3 += f"{patient.fName} {patient.lName}\n"
                result += info1+'\n'+info2+info3+'\n'+info4+info5
            else:
                result += info1 + "\n" + "Currently there are no consultations for this doctor"

        return result




    def showDoctorDetails(self, doctorID):
            doctor = self.searchDoctor_for_assign(doctorID)
            info1 = f"Doctor: {doctor.fName} {doctor.lName}, ID: {doctor.doctorID}, Specialization: {doctor.spec}\n"
            info2 = "Patient list:\n"
            info3 = ''
            info4 = "Consultations:\n"
            info5 = ''
            patient_list = []
            for consultation in self.consulationList:
                if consultation.doctor == doctor:
                    info5 += f"{consultation.date} Patient ID: {consultation.patient.patientID}, Patient: {consultation.patient.fName} {consultation.patient.lName}, Reason: {consultation.reason} Fee: ${consultation.fee:.2f}\n"
                    patient_list.append(consultation.patient)
            if info5 == '':
                return info1+'\n'+'currently there is no consulation'
            else:
                # remove repeated patient and show the same patient only once
                patient_list = list(dict.fromkeys(patient_list))
                for patient in patient_list:
                    info3 += f"{patient.fName} {patient.lName}\n"
                return info1+'\n'+info2+info3+'\n'+info4+info5

   
    def search_Patient(self, input_str):
        try:
            input_num = int(input_str)  # Convert input to integer if possible
        except ValueError:
            input_num = None

        matching_patients = []

        for patient in self.patientList:
            if (
                patient.fName.lower() == input_str.lower() or
                patient.lName.lower() == input_str.lower() or
                patient.patientID == input_num
            ):
                matching_patients.append(patient)

        if not matching_patients:
            return "No matched patient. Please pay attention to your input. You should provide a patient's first name, last name, or ID number."

        result = ""
        for patient in matching_patients:
            info1 = f"Patient: {patient.fName} {patient.lName}, ID: {patient.patientID}\n"
            info2 = "Doctor list:\n"
            info3 = ''
            info4 = "Consultations:\n"
            info5 = ''
            doctor_list = []
            total_fee = 0

            for consultation in self.consulationList:
                if consultation.patient == patient:
                    info5 += f"Doctor: {consultation.doctor.fName} {consultation.doctor.lName} Date:{consultation.date} Reason: {consultation.reason} Fee: ${consultation.fee:.2f}\n"
                    total_fee += consultation.fee
                    doctor_list.append(consultation.doctor)

            if info5:
                # remove repeated docotr and show the same doctor only once
                doctor_list = list(dict.fromkeys(doctor_list))
                for doctor in doctor_list:
                    info3 += f"{doctor.fName} {doctor.lName}\n"
                result = info1+'\n'+info2+info3+'\n'+'\n'+info4+info5+'\n'+f"Total Fee for Consultations: ${total_fee:.2f}"
            else:
                result += info1 + "\n" + "Currently there are no consultations for this patient"

        return result



    def searchPatient_for_assign(self, input):
        for patient in self.patientList:
            if patient.fName == input or patient.lName == input or patient.patientID == input:
                return patient
        return 0

   

    def showPatientDetails(self, patientID):
        patient = self.searchPatient_for_assign(patientID)
        info1 = f"Patient: {patient.fName} {patient.lName}, ID: {patient.patientID}\n"
        info2 = "Doctor list:\n"
        info3 = ''
        info4 = "Consultations:\n"
        info5 = ''
        doctor_list=[]
        total_fee = 0
        for consultation in self.consulationList:
            if consultation.patient == patient:
                info5 += f"Doctor: {consultation.doctor.fName} {consultation.doctor.lName} Date:{consultation.date} Reason: {consultation.reason} Fee: ${consultation.fee:.2f}\n"
                total_fee += consultation.fee
                doctor_list.append(consultation.doctor)
        if info5 == '':
            return info1+'\n'+'currently there is no consulation'
        else:
            # remove repeated docotr and show the same doctor only once
            doctor_list = list(dict.fromkeys(doctor_list))
            for doctor in doctor_list:
                info3 += f"{doctor.fName} {doctor.lName}\n"
            return info1+'\n'+info2+info3+'\n'+'\n'+info4+info5+'\n'+f"Total Fee for Consultations: ${total_fee:.2f}"


 



    def showAllConsultations(self):
        info = 'consulation report for ABC clinic\n'
        total_fee = 0
        for consultation in self.consulationList:
            info += f"\n{consultation.date} Reason: {consultation.reason} Fee: ${consultation.fee:.2f}"
            total_fee += consultation.fee
        if total_fee == 0:
            return info + '\nCurrently there is no consulation'+'\n'+f"\nTotal Fees: ${total_fee:.2f}"
        else:
            return info + '\n'+f"\nTotal Fees: ${total_fee:.2f}"


        


    def showAllDoctors(self):
        for doctor in self.doctorList:
            print(doctor)                     


    def showAllPatients(self):
        for patient in self.patientList:
            print(patient)

    
   
