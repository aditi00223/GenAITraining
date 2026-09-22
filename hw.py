class Hospital:

    class Patient:
        def __init__(self, patient_id, name, disease, age, room_no):
            self.patient_id = patient_id
            self.name = name
            self.disease = disease
            self.age = age
            self.room_no = room_no

        def details(self):
            print("Patient ID :", self.patient_id)
            print("Name :", self.name)
            print("Disease :", self.disease)
            print("Age :", self.age)
            print("Room No :", self.room_no)


    def __init__(self):
        self.patients = []


    def register_patient(self):
        patient_id = int(input("Enter Patient ID : "))
        name = input("Enter Patient Name : ")
        disease = input("Enter Disease : ")
        age = int(input("Enter Age : "))
        room_no = int(input("Enter Room No : "))

        p = self.Patient(patient_id, name, disease, age, room_no)
        self.patients.append(p)

        print("Patient Added Successfully")


    def show_patients(self):
        if len(self.patients) == 0:
            print("No Patient Added Yet")

        else:
            for i in self.patients:
                i.details()


    def search_patient(self):
        patient_id = int(input("Enter Patient ID to Search : "))

        found = False

        for i in self.patients:
            if i.patient_id == patient_id:
                i.details()
                found = True

        if found == False:
            print("No Patient Found")


    def update_patient(self):
        patient_id = int(input("Enter Patient ID to Update : "))

        found = False

        for i in self.patients:
            if i.patient_id == patient_id:
                found = True

                i.room_no = int(input("Enter New Room No : "))

                print("Room No Updated Successfully")

        if found == False:
            print("No Patient Found")


    def delete_patient(self):
        patient_id = int(input("Enter Patient ID to Delete : "))

        found = False

        for i in self.patients:
            if i.patient_id == patient_id:
                found = True

                self.patients.remove(i)

                print("Patient Deleted Successfully")
                break

        if found == False:
            print("No Patient Found")


hospital = Hospital()


while True:

    print("\n===== HOSPITAL PATIENT MANAGEMENT SYSTEM =====")
    print("1. Register Patient")
    print("2. Show All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        hospital.register_patient()

    elif choice == 2:
        hospital.show_patients()

    elif choice == 3:
        hospital.search_patient()

    elif choice == 4:
        hospital.update_patient()

    elif choice == 5:
        hospital.delete_patient()

    elif choice == 6:
        print("Thank you for using Hospital Patient Management System")
        break

    else:
        print("Invalid Choice")