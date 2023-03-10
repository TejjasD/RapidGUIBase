# Built by Tejas Deolasee

import sys
sys.path.append('src')
sys.path.append('config')
from app.root.root import Root

#########################################################################################

def main():
    rootInstance = Root()   
    rootInstance.run()

#########################################################################################

main()

#########################################################################################