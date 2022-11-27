from GardenSimulator import *


class GardenSimulatorApp:
    def __init__(self):
        self.garden = self.set_garden()
        self.simulator = GardenSimulator(self.garden)
        self.weather = None

    def set_garden(self):
        print('Create garden')
        name = input('Enter name: ')
        size = int(input('Enter size: '))
        area = int(input('Enter area: '))
        os.system('cls||clear')
        print(f"Welcome to the {name}! \n")
        return Garden(name, size, area)

    def create_plot(self):
        name = input("Enter plot name: ")
        plot = Plot(name)
        self.garden.add_plot(plot)

    def create_plant(self, choice, name, growth_rate, growth_time,
                     harvest_time, seed_rate, dig_time=0, treat_time=0):

        if choice == '1':
            plant = Tree(name, growth_rate, growth_time,
                         harvest_time, seed_rate, dig_time)
        elif choice == '2':
            plant = Vegetable(name, growth_rate, growth_time,
                              harvest_time, seed_rate, treat_time)

        plot_name = input("Enter plot name: ")
        plot = self.simulator.get_plot_by_name(plot_name)

        if plant and plot:
            plot.add_plant(plant)
            os.system('cls||clear')
            print("Plant added to plot \n")

    def set_weather(self, weather):
        self.simulator.set_weather(weather)

    def simulate(self):
        self.simulator.simulate()

    def print_garden(self):
        self.simulator.print_garden()

    def get_plant(self):
        name = input("Enter plant name: ")
        plant = self.simulator.get_plant_by_name(name)
        print(plant)

    def get_plot(self):
        name = input("Enter plot name: ")
        plot = self.simulator.get_plot_by_name(name)
        print(plot)





