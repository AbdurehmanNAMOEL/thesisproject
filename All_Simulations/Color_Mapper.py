
def color_mapper(total):
    color_mapping = {
        "Black": "0",
        "Brown": "1",
        "Red": "2",
        "Orange": "3",
        "Yellow": "4",
        "Green": "5",
        "Blue": "6",
        "Violet": "7",
        "Gray": "8",
        "White": "9"
    }

    output = color_mapping.get(total, "!") + " "
    return output


def reverse_color(total):
    reverse = {
        "0": "Black",
        "1": "Brown",
        "2": "Red",
        "3": "Orange",
        "4": "Yellow",
        "5": "Green",
        "6": "Blue",
        "7": "Violet",
        "8": "Gray",
        "9": "White"
    }

    output =reverse.get(total, "!") + " "
    return output


