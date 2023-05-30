import sys
sys.dont_write_bytecode = True
sys.path.append('FleetCore/src')

from fleet.fleetManager import FleetManager

def main():
    fleetInstance = FleetManager()
    fleetInstance.exec()

main()

 