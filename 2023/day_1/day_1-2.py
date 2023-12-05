if __name__ == "__main__":
    string_numbers = {"one" : "1",
                      "two" : "2",
                    "three" : "3",
                     "four" : "4",
                     "five" : "5",
                      "six" : "6",
                    "seven" : "7",
                    "eight" : "8",
                     "nine" : "9"}
    
    f = open("input.txt")
    #f = open("test_input-2.txt")
    Lines = f.readlines()
    calibration_number = []
    for line in Lines:
        line = line.strip()
        numbers_in_line = ""
        strings_to_numbers = ""
        if line in string_numbers:
            print("True")
        tempory_string = ""
        converted_line = ""
        for letter in line:
            tempory_string += letter
            for _ in range(len(tempory_string)):
                try:
                    converted_line += string_numbers[tempory_string[_:]]
                    tempory_string = ""
                except:
                    ValueError
            try:
                int(letter)
                converted_line += letter
                tempory_string = ""
            except:
                ValueError
                 


        for letter in converted_line: 
            try: 
                int(letter)
                numbers_in_line += letter
            
            except:
                ValueError
        calibration_number.append(int(numbers_in_line[0] \
                                    + numbers_in_line[-1]))
    print("Calibration number is ", sum(calibration_number))


