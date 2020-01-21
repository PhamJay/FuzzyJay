import matplotlib.pyplot as plt  # chart library
import pprint as pp# Pretty Print Dictionaries
from defuzzify import defuzzifySet
from fuzzify import fuzzify

# --------------------------------------------------
# A small program to fuzzify a set of input values, transforming them into membership relations.
# Additionally, a defuzzified Value will be returned by default.
# The current variables relate to "Temperature" and "Humidity" respectively, and are defined below.
# However, the program could theoretically be applied to any linguistic variables where the input values are
# doubles/floats, and the membership relations are all triangular or "edge"-cases.
# --------------------------------------------------

#region LinguisticVariables

# The schema for defining Linguistic terms in the context of a linguistic variable is as follows:
# 'Linguistic Term' : [Minima, Median, Maxima]
# If Minima is None, the Minima approaches negative infinity. If Maxima is None, it approaches infinity.
# If both are none, the relation is defined as a Singleton

# Note: Technically, the terms of the linguistic variables "TemperatureInCelsius" and "HumidityInPercent" should
# be dependant on the current value of the other. However, accounting for this would break the scope of this exercise.
# Example: The most comfortable humidity at -10C and +45C is vastly different.


temperatureInCelsius =  { # Values are based on personal experience, from an Austrian perspective.
    "cold": [None, 5, 10],
    "cool": [5, 12.5, 20],
    "nice": [12.5, 20, 27.5],
    "warm": [20, 27.5, 35],
    "hot": [27.5, 35, None]
}

humidityInPercent = { # Source: https://www.howtohome.com/appliances/humidifier/what-is-a-good-humidity-comfort-level/
    "dry": [None, 30, 35],
    "nice": [30, 45, 50],
    "humid": [45, 50, None]
}

window = {
    "closed": [None, 0, None],
    "open": [None, 1, None]
}

radiator = {
    "off": [None, 0, None],
    "1": [None, 1, None],
    "2": [None, 2, None],
    "3": [None, 3, None],
    "4": [None, 4, None],
    "5": [None, 5, None],
}

#endregion



def printFuzzified(lingVar, input, defuzzify = True): # Prints the fuzzified values in the console and to a Barchart
    fuzzySet = fuzzify(lingVar, input)

    plt.bar(range(len(fuzzySet)), list(fuzzySet.values()), align='center')
    plt.xticks(range(len(fuzzySet)), list(fuzzySet.keys()))

    plt.show()

    print("\n ------------------------")
    print("Linguistic Terms:")
    pp.pprint(lingVar)
    print ("\n Crisp Input: ",input)
    print("\n Fuzzy Set:")
    pp.pprint(fuzzySet)

    if defuzzify:
        print("\n Defuzzified Value: ", defuzzifySet(lingVar, fuzzySet))



#region test

printFuzzified(temperatureInCelsius, 22)
printFuzzified(temperatureInCelsius, -12)
printFuzzified(temperatureInCelsius, 42)
printFuzzified(humidityInPercent, 45)
printFuzzified(humidityInPercent, 33)
printFuzzified(humidityInPercent, 60)

#endregion