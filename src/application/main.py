# Built by Tejas Deolasee

import sys
sys.path.append('src/')
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