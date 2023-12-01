

def get_first_digit(line):
    for char in range(0, len(line)):
        if line[char].isdigit():
            return line[char]


def get_last_digit(line):
    for char in range(len(line)-1, -1, -1):
        if line[char].isdigit():
            return line[char]
        

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