
def tolerance_mapping(tolerance):
    tolerance_mapping = {
        "Brown": "0.01",
        "Red": "0.02",
        "Green": "0.005",
        "Blue": "0.0025",
        "Violet": "0.001",
        "Gray": "0.0005",
        "Gold" : "0.05",
        "Silver" : "0.1"
    }

    output = tolerance_mapping.get(tolerance, "!") + " "
    return output

def tolerance4_mapping(tolerance):
    tolerance4_mapping = {
        "Brown": "0.01",
        "Red": "0.02",
        "Green": "0.005",
        "Blue": "0.0025",
        "Violet": "0.001",
        "Gray": "0.0005",
        "Gold" : "0.05",
        "Silver" : "0.1",
        "Black": "0.02",
        "Orange": "0.02",
        "Yellow" : "0.02",
        "White" : "0.02"
    }

    output4 = tolerance4_mapping.get(tolerance, "!") + " "
    return output4


def reverse_tolerance_mapping(tolerance):
   mapping_tolerance = {
        "0.01": "Brown",
        "0.02": "Red",
        "0.005": "Green",
        "0.0025": "Blue",
        "0.001": "Violet",
        "0.0005": "Gray",
        "0.05": "Gold",
        "0.1": "Silver"

    }

   value = mapping_tolerance.get(tolerance, "!") + " "
   return value