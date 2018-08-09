#cd D:\Diego\Documents\GitHub\Number-Inspection-Program
"""List of things to implement:
Prime check [True]
Square(or cube or whatever) root check [True]
Binary [True]
Hexadecimal [True]
Something related to a base that is not base 10 [False]
If it's not prime, check it's factors [False]
Palindromic check [True]
Truncatable prime [False]
Perfect(or triperfect or whatever) number [False]
Factorial [False]
Superpermutation [False] (i don't think i will do this but maybe)
Fibonacci [False]
Support for the number 0 and negative numbers [False]
"""



from tkinter import *
from tkinter import ttk

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.createWidgets()
        self.bind("<Return>", self.doesItHaveRoot)
    def createWidgets(self):
        def placeholder():
            pass
        self.input_Number = StringVar()
        ttk.Entry(self, textvariable=self.input_Number).grid(column=1, row=1)
        ttk.Button(self,
                    command=self.doesItHaveRoot,
                    text="inspect").grid(column=2, row=1)

    def isItPrime(self, event=None):
        primes = [2]
        x = 0
        for num in range(3, int(self.input_Number.get()) + 1): # Tries every number
            while x < len(primes): # Controls index size
                if num % primes[x] == 0: # Sees if it is prime
                    x = 0 # Resets index
                    break # Throws the number away
                else:
                    x += 1 # Tries another number
            else:
                primes.append(num)
                x = 0
        if int(self.input_Number.get()) in primes:
            return True
        else:
            return False
    def doesItHaveRoot(self, event=None):
        input_Number = abs(int(self.input_Number.get()))
        if int(self.input_Number.get()) >= 0:
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
                    result = "{0}th root is {1}".format(degree, (- root))
                    all_Roots.append(result)
                else:
                    result = "{0}th root is {1}".format(degree, root)
                    all_Roots.append(result)
            if negative:
                degree += 2
            else:
                degree += 1
        print(all_Roots)
        return all_Roots
    def convertToBinary(self, event=None):
        input_Number = int(self.input_Number.get())
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
            final_Result[(len(result) - 1) - x] = digit
            x += 1
        return final_Result
    def convertToHexadecimal(self, event=None):
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
        number_InBinary = self.convertToBinary()
        x = 1
        result = []
        final_Result = []
        for digit in number_InBinary:
            hexdigit = number_InBinary[(len(number_InBinary) - x)]
            result.append(str(hexdigit))
            if x % 4 == 0:
                result = invert(result)
                result = "".join(result)
                final_Result.append(hextable[int(result)])
                result = []
            elif x == len(number_InBinary):
                result = invert(result)
                result = "".join(result)
                final_Result.append(hextable[int(result)])
            x +=1
        final_Result = invert(final_Result)
        final_Result = "".join(final_Result)
        print(final_Result)
        return final_Result
    def checkFactors(self, event=None):
        pass
    def isItPalindromic(self, event=None):
        string_Number = str(self.input_Number.get())
        isItReally = True
        for digit in string_Number:
            if digit == string_Number[(len(string_Number) - 1)
                                        - string_Number.index(digit)]:
                pass
            else:
                isItReally = False
                break
        return isItReally
root = Application()
root.mainloop()
