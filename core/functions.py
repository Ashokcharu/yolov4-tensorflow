import os
def read_clases(classes):
    names = {}
    with open(classes, "r") as file:
        for id, name in enumerate(file):
            print(name.strip('/'))


