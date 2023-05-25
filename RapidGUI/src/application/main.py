# Built by Tejas Deolasee

import sys
sys.dont_write_bytecode = True
sys.path.append('RapidGui/src/')
print(sys.path[-1])
from application.apps.pfmApp import PfmApp
from application.apps.calculatorApp import CalculatorApp

#########################################################################################

def mainPfm():
    app = PfmApp()   
    app.run()

#########################################################################################

def mainCalculator():
    app = CalculatorApp()   
    app.run()

#########################################################################################

mainPfm()

#########################################################################################