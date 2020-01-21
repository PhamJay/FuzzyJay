def defuzzifySet(lingVar, fuzzySet):
    medians = dict()  # Since the way we have defined the terms already includes the median, calculation is unnecessary
    sumOfFuzzySet = 0
    for key, value in fuzzySet.items():
        medians[key] = lingVar[key][1]
        sumOfFuzzySet += value
    crispValue = 0

    for key, value in medians.items():
        crispValue += value * fuzzySet[key]

    crispValue = crispValue / sumOfFuzzySet

    return crispValue
