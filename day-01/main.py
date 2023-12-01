
numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_first_digit(line):
    string = ''
    for char in range(0, len(line)):
        for number in numbers:
            if number in string:
                return numbers[number]

        if line[char].isdigit():
            return line[char]
        else:
            string += line[char]


def get_last_digit(line):
    string = ''
    for char in range(len(line)-1, -1, -1):
        for number in numbers:
            if number in string:
                return numbers[number]
            
        if line[char].isdigit():
            return line[char]
        else:
            string = line[char] + string
        

def calibration_value(line):
    return int(get_first_digit(line) + get_last_digit(line))


def calibrate(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            total += calibration_value(line)
        return total

if __name__ == "__main__":
    print(calibrate('input.txt'))