import os

from core import main

instance = main.Rose(home=os.path.dirname(__file__))
instance.start()
