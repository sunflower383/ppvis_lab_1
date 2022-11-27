import os
from models.Garden import Garden
from models.Plot import Plot
from models.Weather import Rain, Sun, Drought
from models.Plant import Vegetable, Tree
from models.Pests import Pests

class GardenSimulator:
    def __init__(self, garden):
        self.garden = garden
        self.weather = None

    def set_weather(self, weather):
        os.system('cls||clear')

        if weather == "1":
            self.weather = Rain()
            print("Weather is Rain \n")
        elif weather == "2":
            self.weather = Sun()
            print("Weather is Sun \n")
        elif weather == "3":
            print("Weather is Drought \n")
            self.weather = Drought()

    def simulate(self):
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    continue
                plant.grow()
                if self.weather.name == "Rain":
                    plant.growth += self.weather.growth_rate
                elif self.weather.name == "Sun":
                    plant.growth += self.weather.growth_rate
                elif self.weather.name == "Drought":
                    plant.growth += self.weather.growth_rate

                if plant.is_grown():
                    print(f'{plant} is grown')

        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    continue
                if plant.is_grown():
                    print(f'{plant} is harvested')
                    plant.growth = 0
                    plant.harvested = True
                    if isinstance(plant, Vegetable):
                        plot.add_plant(plant.seed)
                    elif isinstance(plant, Tree):
                        plot.add_plant(plant.seed)

        os.system('cls||clear')
        print(f"Simulation of garden {self.garden.get_garden_name()}\n")
        print(f"To check result with print garden\n")

    def print_garden(self):
        for plot in self.garden.get_plots():
            print(plot)
            for plant in plot.get_plants():
                print(plant, plant.growth)
            print()

    def harvest(self):
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    plot.add_plant(plant.seed)
                    plant.seed = None

    def get_plot_by_name(self, name):
        return self.garden.get_plot_by_name(name)

    def get_plant_by_name(self, name):
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.name == name:
                    return plant
        return None