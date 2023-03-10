import sys
sys.path.append('src')
sys.path.append('config')
from app.root.root import Root

rootInstance = Root()
rootInstance.run()