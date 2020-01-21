def fuzzify (lingVar, input):  # Example: fuzzify (temperatureInCelsius, 20)
    fuzzySet = dict()
    for key, value in lingVar.items():
        minima = value[0]
        median = value[1]
        maxima = value[2]
        if minima == None: # All Values <= Median = 1
            if input < maxima and input > median:
                fuzzySet[key] = 2 - input/median
            elif input >= maxima :
                fuzzySet[key] = 0
            else:
                fuzzySet[key] = 1

        elif maxima == None: # All Values >= Median = 1
            if input > minima and input < median:
                fuzzySet[key] = 2 - input/median
            elif input <= minima :
                fuzzySet[key] = 0
            else:
                fuzzySet[key] = 1

        elif minima == None and maxima == None: # Singleton
            if(input == value):
                fuzzySet[key] = 1
            else:
                fuzzySet[key] = 0

        else: # Normal Triangular Relation
            if input < minima or input > maxima:
                fuzzySet[key] = 0
            elif input >= median:
                fuzzySet[key] = 1 - (input - median) / (maxima - minima)
            else:
                fuzzySet[key] = 1 + (input - median) / (maxima - minima)

    return fuzzySet
