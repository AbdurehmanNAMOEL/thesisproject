
def Temperature_mapping(tolerance):
    mapping_Temperature = {
        "100": "Brown",
        "50": "Red",
        "15": "Orange",
        "25": "Yellow",
        "10": "Blue",
        "5": "Violet",

    }

    value = mapping_Temperature.get(tolerance, "!") + " "
    return value