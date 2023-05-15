# Built by Tejas Deolasee

import sys
sys.path.append('src/')
from app.pfmApp import PfmApp
from app.calculatorApp import CalculatorApp

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