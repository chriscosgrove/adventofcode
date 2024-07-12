
def calculate(entries: []):
    dictionaryOfNumbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    results = []
    for entry in entries:
        stack = []
        potentialNumber = ""
        reversedPotential = ""
        found = False

        for char in entry:

            if char.isdigit():
                stack.append(char)
                found = True
                break

            potentialNumber = potentialNumber + char

            for key, value in dictionaryOfNumbers.items():
                if key in potentialNumber:
                    stack.append(value)
                    found = True
                    break
            if found:
                break

        found = False
        for char in reversed(entry):
            if char.isdigit():
                stack.append(char)
                found = True
                break

            reversedPotential = char + reversedPotential
            for key, value in dictionaryOfNumbers.items():
                if key in reversedPotential:
                    stack.append(value)
                    found = True
                    break

            if found:
                break

        if len(stack) > 0:
            results.append(int(str(stack[0]) + str(stack[len(stack) - 1])))
            stack.clear()

    return sum(results)

with open('input.txt', 'r') as file:
    entries = file.read().splitlines()

result = calculate(entries)
print(result)

