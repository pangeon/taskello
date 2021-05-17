from utils import path_finder as path
from data import _variables as app

def welcome():
    print("--- {}, ver {} ---".format(app.name, app.version))

if __name__ == "__main__":
    welcome()
