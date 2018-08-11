#cd D:\Diego\Documents\GitHub\Number-Inspection-Program
"""List of things to implement:
Prime check [True]
Square(or cube or whatever) root check [True]
Binary [True]
Hexadecimal [True]
The number in all bases(the limit is an input ofc) [False]
If it's not prime, check it's factors [True]
Palindromic check [True]
Truncatable prime [False]
Perfect(or triperfect or whatever) number [False]
Factorial [False]
Superpermutation [False] (i don't think i will do this but maybe)
Fibonacci [True]
Support for the number 0 and negative numbers [False]
Hyperlink to a page in wikipedia explaining the property [False]
Save favorite numbers with the option of a note to explain why [False]
"""



from tkinter import *
from tkinter import ttk

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.createInitialWidgets()
    def createInitialWidgets(self):
        def inspect(event=None):
            try:
                slaves = self.inspectionFrame.destroy()
                for slave in slaves:
                    slave.grid_forget()
            except:
                pass
            self.createInspectionFrame()
        self.input_Number = StringVar()
        self.bind("<Return>", inspect)
        ttk.Entry(self, textvariable=self.input_Number).grid(column=10, row=10)
        ttk.Button(self,
                    command=inspect,
                    text="inspect").grid(column=20, row=10)
    def createInspectionFrame(self):
        self.selected_Number = int(self.input_Number.get())
        self.inspectionFrame = ttk.Frame(self)
        self.inspectionFrame.grid(column=30, row=10)

        is_It_Prime = self.isItPrime()
        if is_It_Prime:
            prime_Text = "{0} is a prime number".format(self.selected_Number)
        else:
            prime_Text = "{0} is not a prime number".format(self.selected_Number)
        self.prime_Label = ttk.Label(self.inspectionFrame, text=prime_Text)
        self.prime_Label.grid(column=1, row=1)

        its_Roots = self.itsRoots()
        root_Text = ""
        for root in its_Roots:
            root_Text = root_Text + str(self.selected_Number) + "'s " + root + "\n"
        root_List = list(root_Text)
        if len(root_Text) != 0:
            del root_List[len(root_List) - 1]
            root_Text = "".join(root_List)
        else:
            root_Text = "{0} has no perfect roots".format(self.selected_Number)
        self.root_Label = ttk.Label(self.inspectionFrame, text=root_Text)
        self.root_Label.grid(column=1, row=2)

        number_In_Binary = self.convertToBinary()
        binary_Text = "{0} in binary: {1}".format(self.selected_Number, number_In_Binary)
        self.binary_Label = ttk.Label(self.inspectionFrame, text=binary_Text)
        self.binary_Label.grid(column=1, row=3)

        number_In_Hexadecimal = self.convertToHexadecimal()
        hexadecimal_Text = "{0} in hexadecimal: {1}".format(self.selected_Number, number_In_Hexadecimal)
        self.hexadecimal_Label = ttk.Label(self.inspectionFrame, text=hexadecimal_Text)
        self.hexadecimal_Label.grid(column=1, row=4)

        factors = self.checkFactors()
        if is_It_Prime:
            factors_Text = "{0} = 1*{0}".format(self.selected_Number)
        else:
            factors = "*".join(factors)
            factors_Text = "{0} = {1}".format(self.selected_Number, factors)
        self.factor_Label = ttk.Label(self.inspectionFrame, text=factors_Text)
        self.factor_Label.grid(column=1, row=5)

        it_Is_Palindromic = self.isItPalindromic()
        if it_Is_Palindromic:
            palindromic_Text = "{0} is a palindromic number".format(self.selected_Number)
        else:
            palindromic_Text = "{0} is not a palindromic number".format(self.selected_Number)
        self.palindromic_Label = ttk.Label(self.inspectionFrame, text=palindromic_Text)
        self.palindromic_Label.grid(column=1, row=6)

        place_In_Fibonacci_Sequence = self.isItInFibonacci()
        if place_In_Fibonacci_Sequence:
            string_Place = str(place_In_Fibonacci_Sequence)
            listed_Place = list(string_Place)
            if listed_Place[len(listed_Place) - 1] == "1":
                fibonacci_Text = "{0} is in the {1}st place in the fibonacci sequence".format(self.selected_Number, place_In_Fibonacci_Sequence)
            if listed_Place[len(listed_Place) - 1] == "2":
                fibonacci_Text = "{0} is in the {1}nd place in the fibonacci sequence".format(self.selected_Number, place_In_Fibonacci_Sequence)
            if listed_Place[len(listed_Place) - 1] == "3":
                fibonacci_Text = "{0} is in the {1}rd place in the fibonacci sequence".format(self.selected_Number, place_In_Fibonacci_Sequence)
            else:
                fibonacci_Text = "{0} is in the {1}th place in the fibonacci sequence".format(self.selected_Number, place_In_Fibonacci_Sequence)
        else:
            fibonacci_Text = "{0} does not appear in the fibonacci sequence".format(self.selected_Number)
        self.fibonacci_Label = ttk.Label(self.inspectionFrame, text=fibonacci_Text)
        self.fibonacci_Label.grid(column=1, row=7)

    def isItPrime(self):
        primes = [2]
        x = 0
        for num in range(3, self.selected_Number + 1): # Tries every number
            while x < len(primes): # Controls index size
                if num % primes[x] == 0: # Sees if it is prime
                    x = 0 # Resets index
                    break # Throws the number away
                else:
                    x += 1 # Tries another number
            else:
                primes.append(num)
                x = 0
        if self.selected_Number in primes:
            return True
        else:
            return False
    def itsRoots(self):
        input_Number = abs(self.selected_Number)
        if self.selected_Number >= 0:
            degree = 2
            negative = False
        else:
            degree = 3
            negative = True
        all_Roots = []
        while degree < input_Number:
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
    def convertToBinary(self):
        input_Number = str(self.selected_Number)[:]
        input_Number = int(input_Number)
        result = []

        while True:
            if input_Number == 1:
                result.append(int(input_Number % 2))
                break
            result.append(int(input_Number % 2))
            input_Number = int(input_Number / 2)

        x = 0
        final_Result = result[:]
        for digit in result:
            final_Result[(len(result) - 1) - x] = str(digit)
            x += 1
        final_Result = "".join(final_Result)
        final_Result = int(final_Result)
        return final_Result
    def convertToHexadecimal(self):
        def invert(list):
            x = 1
            result = list[:]
            for item in list:
                result[len(list) - x] = item
                x +=1
            return result
        hextable = {0: "0",
            1: "1",
            10: "2",
            11: "3",
            100: "4",
            101: "5",
            110: "6",
            111: "7",
            1000: "8",
            1001: "9",
            1010: "a",
            1011: "b",
            1100: "c",
            1101: "d",
            1110: "e",
            1111: "f"
            }
        number_In_Binary = list(str(self.convertToBinary()))
        x = 1
        result = []
        final_Result = []
        for digit in number_In_Binary:
            hexdigit = number_In_Binary[(len(number_In_Binary) - x)]
            result.append(str(hexdigit))
            if x % 4 == 0:
                result = invert(result)
                result = "".join(result)
                final_Result.append(hextable[int(result)])
                result = []
            elif x == len(number_In_Binary):
                result = invert(result)
                result = "".join(result)
                final_Result.append(hextable[int(result)])
            x +=1
        final_Result = invert(final_Result)
        final_Result = "".join(final_Result)
        return final_Result
    def checkFactors(self):
        primes = [2]
        x = 0
        for num in range(3, self.selected_Number + 1): # Tries every number
            while x < len(primes): # Controls index size
                if num % primes[x] == 0: # Sees if it is prime
                    x = 0 # Resets index
                    break # Throws the number away
                else:
                    x += 1 # Tries another number
            else:
                primes.append(num)
                x = 0
        selected_Number = str(self.selected_Number)[:]
        selected_Number = int(selected_Number)
        factors = []
        still_Going_On = True
        while still_Going_On:
            for prime in primes:
                if selected_Number == 1:
                    still_Going_On = False
                    break
                if selected_Number % prime == 0:
                    factors.append(str(prime))
                    selected_Number = selected_Number / prime
                    break
        return factors
    def isItPalindromic(self):
        string_Number = str(self.selected_Number)
        result = True
        for digit in string_Number:
            if digit == string_Number[(len(string_Number) - 1)
                                        - string_Number.index(digit)]:
                pass
            else:
                result = False
                break
        return result
    def isItInFibonacci(self):
        first_Number, second_Number = 0, 1
        count = 1
        while second_Number <= self.selected_Number:
            if second_Number == self.selected_Number:
                return count
            first_Number, second_Number = second_Number, first_Number + second_Number
            count +=1
        return False

root = Application()
root.mainloop()
