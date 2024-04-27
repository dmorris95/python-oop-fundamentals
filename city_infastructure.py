#Task 1

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print("The owner has been updated")
    

vehicle1 = Vehicle("12345", "Camry", "Joe Smith")
vehicle2 = Vehicle("65432", "F-150", "Richard Johns")
vehicle3 = Vehicle("32412", "Elantra", "George Jennies")

print(vehicle1.registration_number, vehicle1.type, vehicle1.owner)
print(vehicle2.registration_number, vehicle2.type, vehicle2.owner)
print(vehicle3.registration_number, vehicle3.type, vehicle3.owner)

vehicle2.update_owner("Richie Stevens")
print("Updated Vehicle:", vehicle2.registration_number, vehicle2.type, vehicle2.owner)


#Task 2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []

    def add_participant(self, *participant):
        #adds participants to the participant dictionary
        for p in participant:
            self.participants.append(p)

    def get_participant_count(self):
        print(f"Number of particpants: {len(self.participants)}")
        print(f"The participants for the {self.name} are: ")
        for p in self.participants:
            print(p)

first_event = Event("Parade", "12-04-2025")
second_event = Event("Concert", "08-09-2024")

first_event.add_participant("John", "Steve", "Rich", "Drew")
first_event.get_participant_count()

 
