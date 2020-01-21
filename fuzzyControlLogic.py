# --------------------------------------------------
# Handles all the logic a fuzzy controller needs
# --------------------------------------------------


def fuzzyEquals(lingTerm, fuzzySet):
    true_terms = [k for k, v in fuzzySet.items() if v >= 0.5]
    if lingTerm in true_terms:
        return True
    else:
        return False



