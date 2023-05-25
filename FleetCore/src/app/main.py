import sys
sys.dont_write_bytecode = True
sys.path.append('FleetCore/')

from FleetCore.src.fleet.fleetManager import FleetManager

def main():
    fleetInstance = FleetManager()

main()

