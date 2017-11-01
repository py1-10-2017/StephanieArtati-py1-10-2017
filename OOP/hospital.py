
class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.bed_assigned = []
        for i in range(0,capacity):
            self.bed_assigned.append(0)
        self.name = name
        self.capacity = capacity

    def admit_patient(self, patient):
        if (len(self.patients) >= self.capacity):
            print("Sorry, hospital is full")
        else:
            #find an available bed and assign to patient
            i = 0
            while (self.bed_assigned[i] == 1):
                i += 1
            patient.bed_number = i #assign bed number ot patient
            self.bed_assigned[i] = 1 #mark bed as assigned
            self.patients.append(patient) #admit patient to Hospital
            print("Admission is complete")
        return self

    def discharge_patient(self, patient):
        for i in range(0,len(self.patients)):
            if (patient.id == self.patients[i].id):
                self.patients.pop(i) #remove patient from hospital patient's list
                bed_number = patient.bed_number
                patient.bed_number = None #set bed number to None
                self.bed_assigned[bed_number] = 0 #make bed available again
                break

    def info(self):
        print("Number of patients: " + str(len(self.patients)))


class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def info(self):
        print("Patient name: "+self.name)
        print("Bed number: "+str(self.bed_number))

MyHospital = Hospital("Evergreen",100)
Patient1 = Patient(1, "Stephanie Artati", [])
Patient2 = Patient(2, "Sophia Lie", ["peanut"])
MyHospital.admit_patient(Patient1)
MyHospital.admit_patient(Patient2)
MyHospital.info()
Patient1.info()
Patient2.info()
MyHospital.discharge_patient(Patient1)
Patient3 = Patient(3, "Junaili Lie", [])
MyHospital.admit_patient(Patient3)
MyHospital.info()
Patient3.info()
