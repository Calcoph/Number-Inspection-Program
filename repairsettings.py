def isaValidSet(input_Set):
    new_Set = set({})
    listed_Value = list(input_Set)
    if listed_Value[0] != "{" or listed_Value[len(listed_Value) - 1] != "}":
        return False
    digit_Storage = ""
    for item in listed_Value:
        if item.isdigit():
            digit_Storage = digit_Storage + item
        elif item == ","or item == "}":
            new_Set.add(int(digit_Storage))
            digit_Storage = ""
            input_Set = new_Set
            for item in input_Set:
                if item >= 37 or item <= 1:
                    return False
        elif item in [" ", "{"]:
            pass
        else:
            return False
        return True
def getVariableName(line):
    listed_Line = list(line)
    newstring = ""
    for character in listed_Line:
        if character != " ":
            newstring += character
        else:
            return newstring
    return newstring
def getRestOfLine(line):
    listed_Line = list(line)
    newstring = ""
    second_Blank = False
    iterating_Over_Rest_Of_The_Line = False
    for character in listed_Line:
        if iterating_Over_Rest_Of_The_Line:
            newstring += character
        elif character == " ":
            if second_Blank:
                iterating_Over_Rest_Of_The_Line = True
            second_Blank = True
    return newstring[:-1]# The slicing is to remove \n
def diagnoseSettings(template, line_Count, listed_New_File):
    with open("settings.txt") as settings:
        for line in settings:
            variable_Name = getVariableName(line)
            rest_Of_The_Line = getRestOfLine(line)
            if line_Count == 1:
                expected_Variable_Name = "decimal_Mark"
                possible_Values = ["','", "'.'"]
                default_Value = "','"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 2:
                expected_Variable_Name = "thousand_Mark"
                possible_Values = ["','", "'.'"]
                default_Value = "'.'"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 3:
                expected_Variable_Name = "uppercase_hexadecimal"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 4:
                expected_Variable_Name = "decimal_Separator"
                possible_Values = ["1", "2"]
                default_Value = "1"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 5:
                expected_Variable_Name = "show_Relevant"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 6:
                expected_Variable_Name = "show_Prime"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 7:
                expected_Variable_Name = "show_Roots"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 8:
                expected_Variable_Name = "show_Binary"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 9:
                expected_Variable_Name = "show_Hexadecimal"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 10:
                expected_Variable_Name = "show_Factors"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 11:
                expected_Variable_Name = "show_Palindromic"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 12:
                expected_Variable_Name = "show_Fibonacci"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 13:
                expected_Variable_Name = "show_Factorial"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 14:
                expected_Variable_Name = "selected_Bases"
                default_Value = "{2, 8, 10, 16}"
                if (expected_Variable_Name == variable_Name)\
                    and isaValidSet(rest_Of_The_Line):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 15:
                expected_Variable_Name = "show_All_Bases"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 16:
                expected_Variable_Name = "show_Base_2"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 17:
                expected_Variable_Name = "show_Base_3"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 18:
                expected_Variable_Name = "show_Base_4"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 19:
                expected_Variable_Name = "show_Base_5"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 20:
                expected_Variable_Name = "show_Base_6"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 21:
                expected_Variable_Name = "show_Base_7"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 22:
                expected_Variable_Name = "show_Base_8"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 23:
                expected_Variable_Name = "show_Base_9"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 24:
                expected_Variable_Name = "show_Base_10"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 25:
                expected_Variable_Name = "show_Base_11"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 26:
                expected_Variable_Name = "show_Base_12"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 27:
                expected_Variable_Name = "show_Base_13"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 28:
                expected_Variable_Name = "show_Base_14"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 29:
                expected_Variable_Name = "show_Base_15"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 30:
                expected_Variable_Name = "show_Base_16"
                possible_Values = ["True", "False"]
                default_Value = "True"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 31:
                expected_Variable_Name = "show_Base_17"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 32:
                expected_Variable_Name = "show_Base_18"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 33:
                expected_Variable_Name = "show_Base_19"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 34:
                expected_Variable_Name = "show_Base_20"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 35:
                expected_Variable_Name = "show_Base_21"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 36:
                expected_Variable_Name = "show_Base_22"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 37:
                expected_Variable_Name = "show_Base_23"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 38:
                expected_Variable_Name = "show_Base_24"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 39:
                expected_Variable_Name = "show_Base_25"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 40:
                expected_Variable_Name = "show_Base_26"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 41:
                expected_Variable_Name = "show_Base_27"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 42:
                expected_Variable_Name = "show_Base_28"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 43:
                expected_Variable_Name = "show_Base_29"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 44:
                expected_Variable_Name = "show_Base_30"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 45:
                expected_Variable_Name = "show_Base_31"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 46:
                expected_Variable_Name = "show_Base_32"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 47:
                expected_Variable_Name = "show_Base_33"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 48:
                expected_Variable_Name = "show_Base_34"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 49:
                expected_Variable_Name = "show_Base_35"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                        listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            elif line_Count == 50:
                expected_Variable_Name = "show_Base_36"
                possible_Values = ["True", "False"]
                default_Value = "False"
                if (expected_Variable_Name == variable_Name)\
                    and (rest_Of_The_Line in possible_Values):
                    listed_New_File.append(line)
                else:
                    listed_New_File.append(template[line_Count - 1])
            line_Count += 1
        return line_Count, listed_New_File
def repairSettings():
    template = ["decimal_Mark = ','\n",
        "thousand_Mark = '.'\n",
        "uppercase_hexadecimal = False\n",
        "decimal_Separator = 1\n",
        "show_Relevant = True\n",
        "show_Prime = True\n",
        "show_Roots = True\n",
        "show_Binary = True\n",
        "show_Hexadecimal = True\n",
        "show_Factors = True\n",
        "show_Palindromic = True\n",
        "show_Fibonacci = True\n",
        "show_Factorial = True\n",
        "selected_Bases = {2, 8, 10, 16}\n",
        "show_All_Bases = False\n",
        "show_Base_2 = True\n",
        "show_Base_3 = False\n",
        "show_Base_4 = False\n",
        "show_Base_5 = False\n",
        "show_Base_6 = False\n",
        "show_Base_7 = False\n",
        "show_Base_8 = True\n",
        "show_Base_9 = False\n",
        "show_Base_10 = True\n",
        "show_Base_11 = False\n",
        "show_Base_12 = False\n",
        "show_Base_13 = False\n",
        "show_Base_14 = False\n",
        "show_Base_15 = False\n",
        "show_Base_16 = True\n",
        "show_Base_17 = False\n",
        "show_Base_18 = False\n",
        "show_Base_19 = False\n",
        "show_Base_20 = False\n",
        "show_Base_21 = False\n",
        "show_Base_22 = False\n",
        "show_Base_23 = False\n",
        "show_Base_24 = False\n",
        "show_Base_25 = False\n",
        "show_Base_26 = False\n",
        "show_Base_27 = False\n",
        "show_Base_28 = False\n",
        "show_Base_29 = False\n",
        "show_Base_30 = False\n",
        "show_Base_31 = False\n",
        "show_Base_32 = False\n",
        "show_Base_33 = False\n",
        "show_Base_34 = False\n",
        "show_Base_35 = False\n",
        "show_Base_36 = False\n"]
    is_Damaged = True
    is_Empty = False
    with open("settings.txt") as settings:
        string_Template = "".join(template)
        if settings.read() == string_Template:
            is_Damaged = False
        if settings.read() == " ":
            is_Empty = True
    if is_Empty:
        with open("settings.txt", "w") as settings:
            for line in template:
                listed_Line = list(line)
                listed_line = listed_Line[:-1]
                line = "".join(listed_Line)
                settings.write(line)
    elif is_Damaged:
        line_Count = 1
        listed_New_File = []
        while True:
            if line_Count <= 50:
                line_Count, listed_New_File = diagnoseSettings(template,
                                                               line_Count,
                                                               listed_New_File)
            else:
                break
        new_File = "".join(listed_New_File)
        with open("settings.txt", "w") as settings:
            for line in new_File:
                listed_Line = list(line)
                listed_line = listed_Line[:-1]
                line = "".join(listed_Line)
                settings.write(line)
