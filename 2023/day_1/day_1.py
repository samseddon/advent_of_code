import numpy as np

if __name__ == "__main__":
    f = open("input.txt")
    Lines = f.readlines()
    calibration_number = []
    for line in Lines:
        line = line.strip()
        numbers_in_line = []
        for letter in line:
            
            try: 
                int(letter)
                numbers_in_line += letter
            
            except:
                ValueError
        calibration_number.append(int(numbers_in_line[0] \
                                    + numbers_in_line[-1]))
        print(numbers_in_line, calibration_number)
    print("Calibration number is ", sum(calibration_number))


