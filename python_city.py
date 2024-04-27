#Task 1

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

#functions for saving and uploading
def upload_buildings(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, floors = line.strip().split(',')
                build = Building(name, floors)
                builds[name] = build
    except IOError:
        print("An error occurred please try again!")

def save_buildings(filename):
    try:
        with open(filename, "w") as file:                
            for build in builds.values():
                file.write(f"{build.name},{build.floors}\n")
    except IOError:
        print("An error occured, please try agian!")

builds = {} #dictionary with the name being the key
build1 = Building("Apartments", "10")
build2 = Building("Office Building", "4")
build3 = Building("Townhouse", "2")
build4 = Building("Offices", "8")
builds[build1.name] = build1
builds[build2.name] = build2
builds[build3.name] = build3
builds[build4.name] = build4

upload_buildings("exist_builds.txt")
save_buildings("buildings.txt")

upload_buildings("buildings.txt")
for build in builds.values():
    print(f"{build.name} has {build.floors} floors")