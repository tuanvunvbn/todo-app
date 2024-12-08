FREEZING_POINT = 0
BOILING_POINT = 100


def temperature(temper):
    if temper < FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temper < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
