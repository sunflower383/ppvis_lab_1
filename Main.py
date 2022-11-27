from Gui import Gui
from Controller import GardenSimulatorApp
class Main():
    print("Welcome to the Garden Simulator! \n")
    app = GardenSimulatorApp()
    gui = Gui(app)
    gui.run()
if __name__ == "__main__":
    Main()