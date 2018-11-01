def isItPrime(input):
    if input <= 1:
        return False
    for num in range(2, input): # Tries every number
        if input % num == 0:
            return False
    return True

def itsRoots(input):
    input_Number = abs(input)
    if input > 0:
        degree = 2
        negative = False
    elif input == 0:
        all_Roots = []
        return all_Roots
    else:
        degree = 3
        negative = True
    all_Roots = []
    while degree <= (input_Number / 2):
        root = int(round(input_Number ** (1.0 / degree)))
        if root ** degree == input_Number:
            if negative:
                string_Degree = str(degree)
                listed_Degree = list(string_Degree)
                if listed_Degree[len(listed_Degree) - 1] == "1":
                    result = "{0}st root is {1}".format(degree, (- root))
                elif listed_Degree[len(listed_Degree) - 1] == "2":
                    result = "{0}nd root is {1}".format(degree, (- root))
                elif listed_Degree[len(listed_Degree) - 1] == "3":
                    result = "{0}rd root is {1}".format(degree, (- root))
                else:
                    result = "{0}th root is {1}".format(degree, (- root))
                all_Roots.append(result)
            else:
                string_Degree = str(degree)
                listed_Degree = list(string_Degree)
                if listed_Degree[len(listed_Degree) - 1] == "1":
                    result = "{0}st root is {1}".format(degree, root)
                elif listed_Degree[len(listed_Degree) - 1] == "2":
                    result = "{0}nd root is {1}".format(degree, root)
                elif listed_Degree[len(listed_Degree) - 1] == "3":
                    result = "{0}rd root is {1}".format(degree, root)
                else:
                    result = "{0}th root is {1}".format(degree, root)
                all_Roots.append(result)
        if negative:
            degree += 2
        else:
            degree += 1
    return all_Roots

def checkPrimeFactors(input):
    factors = []
    if input == 1:
        factors.append("1")
        return factors
    if input < 0:
        return factors
    for num in range(1, int(input) + 1):
        if input % num == 0 and isItPrime(num):
            factors.append(str(num))
    for num in factors:
        num = int(num)
        input = int(input / num)
    new_Factors = checkPrimeFactors(input)
    for factor in new_Factors:
        factors.append(factor)
    return factors

def isItPalindromic(input):
    string_Number = str(input)
    result = True
    for digit in string_Number:
        if digit == string_Number[(len(string_Number) - 1)
                                    - string_Number.index(digit)]:
            pass
        else:
            result = False
            break
    return result

def isItInFibonacci(input):
    first_Number, second_Number = 0, 1
    count = 1
    while second_Number <= input:
        if second_Number == input:
            return count
        first_Number, second_Number = second_Number, first_Number + second_Number
        count +=1
    return False

def factorial(input):
    if input <= 50000:
        product = 1
        factor = 1
        while factor <= input:
            product = product * factor
            factor += 1
        return product
    else:
        return "number too big"

def truncatablePrime(input):# left-truncatable not right-truncatable
    if input <= 1:
        return False
    listed_Number = list(str(input))
    while True:
        if len(listed_Number) != 1:
            listed_Number = int("".join(listed_Number))
            if isItPrime(listed_Number):
                listed_Number = list(str(listed_Number))
                listed_Number = listed_Number[1:]
            else:
                return False
        else:
            listed_Number = int("".join(listed_Number))
            if isItPrime(listed_Number):
                return True
            else:
                return False

def isItPerfect(input):
    factors = []
    for num in range(1, input + 1):
        if input % num == 0:
            factors.append(num)
    sum = 0
    for index in range(0, len(factors)):
        sum += factors[index]
    if sum == input * 2:
        return "2"
    elif sum == input * 3:
        return "3"
    elif sum == input * 4:
        return "4"
    else:
        return False

def convertToBaseX(input, base): # Max base = 36
    conversion_Table = {0: "0",
                       1: "1",
                       2: "2",
                       3: "3",
                       4: "4",
                       5: "5",
                       6: "6",
                       7: "7",
                       8: "8",
                       9: "9",
                       10: "A",
                       11: "B",
                       12: "C",
                       13: "D",
                       14: "E",
                       15: "F",
                       16: "G",
                       17: "H",
                       18: "I",
                       19: "J",
                       20: "K",
                       21: "L",
                       22: "M",
                       23: "N",
                       24: "O",
                       25: "P",
                       26: "Q",
                       27: "R",
                       28: "S",
                       29: "T",
                       30: "U",
                       31: "V",
                       32: "W",
                       33: "X",
                       34: "Y",
                       35: "Z"
                       }
    input_Number = str(input)[:]
    input_Number = int(input_Number)
    result = []

    while True:
        if input_Number in [-1, 0, 1]:
            result.append(conversion_Table[int(input_Number % base)])
            break
        result.append(conversion_Table[int(input_Number % base)])
        input_Number = int(input_Number / base)
    x = 0
    final_Result = result[:]
    for digit in result:
        final_Result[(len(result) - 1) - x] = str(digit)
        x += 1
    final_Result = "".join(final_Result)
    while True:
        if final_Result[0] == "0":
            final_Result = final_Result[1:]
        else:
            break
    return final_Result

def roman(input):
    input = int(input)
    if input > 388888:
        return "too big"
    conversion_Table = {"1": "I",
        "4": "IV",
        "5": "V",
        "9": "IX",
        "10": "X",
        "40": "XL",
        "50": "L",
        "90": "XC",
        "100": "C",
        "400": "CD",
        "500": "D",
        "900": "CM",
        "1000": "M",
        "4000": "MV\u0305",
        "5000": "V\u0305",
        "9000": "I\u0305X\u0305",
        "10000": "X\u0305",
        "40000": "X\u0305L\u0305",
        "50000": "L\u0305",
        "90000": "X\u0305C\u0305",
        "100000": "C\u0305",
        "400000": "C\u0305D\u0305",
        "500000": "D\u0305",
        "900000": "C\u0305M\u0305",
        "1000000": "M\u0305",
    }
    number = str(input)
    roman_Number = ""
    zeroes = len(number) - 1
    for digit in number:
        if digit in ["2", "3"]:
            quantity = int(digit)
            digit = 1
            new_Digit = (conversion_Table[str(digit) + ("0"*zeroes)]) * quantity
        elif digit in ["6", "7", "8"]:
            quantity = int(digit) - 5
            digit = 1
            new_Digit = conversion_Table["5" + ("0"*zeroes)]\
                         + conversion_Table[str(digit) + ("0"*zeroes)]\
                         * quantity
        elif digit == "0":
            new_Digit = ""
        else:
            new_Digit = conversion_Table[str(digit) + ("0"*zeroes)]
        zeroes -= 1
        roman_Number += new_Digit
    return roman_Number
