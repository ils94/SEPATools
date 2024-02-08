def mostrarDuplicados():
    pass


def find_duplicates(numbers):
    duplicates = {}
    result_string = ""
    for number in numbers:
        if number in duplicates:
            duplicates[number] += 1
        else:
            duplicates[number] = 1

    for number, count in duplicates.items():
        if count > 1:
            result_string += f"{number}: {count}x\n"

    return result_string.strip()
