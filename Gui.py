import os
class Gui:
    def __init__(self, app):
        self.app = app

    def run(self):
        while True:
            print("1. Create plot")
            print("2. Create plant")
            print("3. Set weather")
            print("4. Simulate")
            print("5. Print garden")
            print("6. Get plant")
            print("7. Get plot")
            print("0. Exit \n")
            command = input("Enter command: ")
            print("\n")

            if command == '1':
                self.app.create_plot()
            elif command == '2':
                print("1. Tree,    2. Vegetable \n")
                plant_type = input("Enter choice: ")
                name = input("Enter name: ")
                growth_rate = float(input("Enter growth rate: "))
                growth_time = int(input("Enter growth time: "))
                harvest_time = int(input("Enter harvest time: "))
                seed_rate = float(input("Enter seed rate: "))

                if plant_type == '1':
                    dig_time = int(input("Enter dig time: "))
                    self.app.create_plant(plant_type, name, growth_rate, growth_time,
                                          harvest_time, seed_rate, dig_time)
                elif plant_type == '2':
                    treat_time = int(input("Enter treat time: "))
                    self.app.create_plant(plant_type, name, growth_rate, growth_time,
                                          harvest_time, seed_rate, treat_time)

                os.system('cls||clear')
                print("Plant created \n")
            elif command == '3':
                print("1. Rain")
                print("2. Sun")
                print("3. Drought")
                choice = input("Enter your choice: ")
                self.app.set_weather(choice)
            elif command == '4':
                self.app.simulate()
            elif command == '5':
                self.app.print_garden()
            elif command == '6':
                self.app.get_plant()
            elif command == '7':
                self.app.get_plot()
            elif command == '0':
                break
