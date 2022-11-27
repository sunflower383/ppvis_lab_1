import os
# Сущности - Грядка
class Garden:
    def __init__(self, name, size, area):
        self.name = name
        self.size = size
        self.area = area
        self.plots = []

    def __str__(self):
        return f'Garden {self.name} has size {self.size} and area {self.area}'

    def __repr__(self):
        return f'Garden {self.name} has size {self.size} and area {self.area}'

    def add_plot(self, plot):
        if len(self.plots)+self.size >= self.area:
            os.system('cls||clear')
            print('Not enough space in garden \n')
            return
        self.plots.append(plot)
        os.system('cls||clear')
        print("Plot created! \n")

    def get_plots(self):
        return self.plots

    def get_plot_by_name(self, name):
        for plot in self.plots:
            if plot.name == name:
                return plot
        print('Plot with name ' + name + ' not found')
        return None

    def remove_plot_by_name(self, name):
        for i in range(len(self.plots)):
            if self.plots[i].name == name:
                del self.plots[i]
                return
        raise Exception('Plot with name ' + name + ' not found')

    def get_plots_count(self):
        return len(self.plots)

    def get_garden_name(self):
        return self.name

    def water(self, plant):
        plant.watered = True

    def weed(self, plant):
        plant.weeded = True