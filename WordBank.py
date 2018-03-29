import pickle
import sys
import random

places = {1 : "The North Pole", 2 : "Hollywood", 3 : "Swimming Pool"}
def save(dict):
    with open("places.pkl", "wb") as file:
        pickle.dump(dict, file, pickle.HIGHEST_PROTOCOL)
save(places)

def load(name):
    with open(name + ".pkl", "rb") as file:
        return pickle.load(file)
print(load("places"))