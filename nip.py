#cd D:\Diego\Documents\GitHub\Number-Inspection-Program
"""List of things to implement:
Prime check [True]
Square(or cube or whatever) root check [True]
Binary [True]
Hexadecimal [True]
The number in all bases(up to 36) [True]
If it's not prime, check it's factors [True]
Palindromic check [True]
Truncatable prime [True]
Perfect(or triperfect or whatever) number [True]
Factorial [True]

Superpermutation [False] (i don't think i will do this but maybe) 0.5

Fibonacci [True]
Support for the number 0 and negative numbers [True]
Hyperlink to a page in wikipedia explaining the property [True]

Save favorite numbers with the option of a note to explain why [False]
Support for input numbers in any base [False]
13/15.5
Variable maximum number so the max time of an inspection is one second [False]
Roman number [True]
Spanish support [False]

Settings File [True]
Divide the "BASES" view in 3 pages of 12 bases each [True]
Set the names of the bases correctly (1st, 2nd, 3rd, 4th
                                      instead of 1th, 2th, 3th, 4th) [True]

Lucas numbers [False]
^2 instead of ² (optional) [False]
bases for negative numbers [False]
this: https://es.wikipedia.org/wiki/Anexo:Nombres_de_los_n%C3%BAmeros_en_espa%C3%B1ol [False] 0.3
and ^^^^^^^^^^ in english [False] 0.3
^^^^^^^^^^^^^^^in other languages maybe [False] 0.3
if settings.txt doesn't exist, create it [True]
5/11
18/26.5
"""



from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from settingstab import SettingsTab
import properties
import webbrowser
#import time

class Application(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.createInitialWidgets()
        self.createMenu()

    def createInitialWidgets(self):
        def inspect(event=None):
            try:
                self.inspection_Frame.destroy()
            except:
                pass
            self.createInspectionFrame()
        self.input_Number = StringVar()
        self.bind("<Return>", inspect)
        self.main_Frame = ttk.Frame(self)
        self.main_Frame.grid(column=1, row=1)
        self.inspection_Entry = ttk.Entry(self.main_Frame,
                                          textvariable=self.input_Number)
        self.inspection_Entry.grid(column=1, row=1)
        ttk.Button(self.main_Frame,
                    command=inspect,
                    text="inspect").grid(column=2, row=1)
        def calculator():
            def calculatorCE(event=None):
                calculator_Entry.set("")
            def calculatorNumber(number, event=None):
                if operating.get():
                    calculator_Entry.set(number)
                    operating.set(False)
                else:
                    calculator_Entry.set(calculator_Entry.get() + number)
            def calculatorPositiveNegative(event=None):
                try:
                    if int(calculator_Entry.get()) > 0:
                        calculator_Entry.set("-" + calculator_Entry.get())
                    elif int(calculator_Entry.get()) < 0:
                        listed_Entry = list(calculator_Entry.get())
                        listed_Entry.remove("-")
                        string_Entry = "".join(listed_Entry)
                        calculator_Entry.set(string_Entry)
                except:
                    pass
            def calculatorC(event=None):
                self.last_Entry = False
                last_operation.set("")
                operating.set(False)
                calculator_Entry.set("")
                operations.set("")
            def calculatorRemove(event=None):
                try:
                    listed_Entry = list(calculator_Entry.get())
                    listed_Entry[len(listed_Entry) - 1] = ""
                    string_Entry = "".join(listed_Entry)
                    calculator_Entry.set(string_Entry)
                except:
                    pass
            def calculatorSquare(event=None):
                last_operation.set("^2 ")
                operations.set(operations.get()
                                + calculator_Entry.get()
                                +  last_operation.get()
                                )
                try:
                    if len(str(int(calculator_Entry.get()) ** 2)) > 80:
                        calculator_Entry.set("Too big")
                    else:
                        calculator_Entry.set(str(int(calculator_Entry.get()) ** 2))
                except:
                    pass
                list_Operations = list(operations.get())
                while len(list_Operations) > 45:
                    del list_Operations[0]
                list_Operations = "".join(list_Operations)
                operations.set(list_Operations)
                self.last_Entry = calculator_Entry.get()
            def calculatorDivide(event=None):
                self.last_Entry = calculator_Entry.get()
                last_operation.set(" / ")
                operations.set(operations.get() + calculator_Entry.get() +  last_operation.get())
                operating.set(True)
            def calculatorMultiply(event=None):
                self.last_Entry = calculator_Entry.get()
                last_operation.set(" x ")
                operations.set(operations.get() + calculator_Entry.get() +  last_operation.get())
                operating.set(True)
            def calculatorSubstract(event=None):
                self.last_Entry = calculator_Entry.get()
                last_operation.set(" - ")
                operations.set(operations.get() + calculator_Entry.get() +  last_operation.get())
                operating.set(True)
            def calculatorAdd(event=None):
                self.last_Entry = calculator_Entry.get()
                last_operation.set(" + ")
                operations.set(operations.get() + calculator_Entry.get() +  last_operation.get())
                operating.set(True)
            def calculatorEquals(event=None):
                current_Entry = calculator_Entry.get()
                result = ""

                if last_operation.get() == " / ":
                    result = str(int(self.last_Entry) / int(current_Entry))
                elif last_operation.get() == " x ":
                    result = str(int(self.last_Entry) * int(current_Entry))
                elif last_operation.get() == " - ":
                    result = str(int(self.last_Entry) - int(current_Entry))
                elif last_operation.get() == " + ":
                    result = str(int(self.last_Entry) + int(current_Entry))
                else:
                    pass

                last_operation.set(" = ")
                operations.set("")
                calculator_Entry.set(result)
                operating.set(True)
            def exportInput(event=None):
                self.input_Number.set(calculator_Entry.get())

            self.last_Entry = False
            last_operation = StringVar()
            last_operation.set("")
            operating = BooleanVar()
            operating.set(False)
            operations = StringVar()
            calculator_Entry = StringVar()

            calculator_Frame = ttk.Frame(self.main_Frame)
            calculator_Frame.grid(column=1, row=3, columnspan=2)
            calculator_Frame.columnconfigure(1, weight=1)
            calculator_Entry_Frame = ttk.Frame(calculator_Frame)
            calculator_Entry_Frame.grid(column=1, row=2, columnspan=4, sticky="W")
            calculator_Entry_Frame.columnconfigure(1, weight=1)
            calculator_Entry_Frame.columnconfigure(2, weight=1)
            operationsLabel = ttk.Label(calculator_Frame,
                                        textvariable=operations).grid(column=1,
                                                                        row=1,
                                                                        columnspan=4)
            entry_Display = ttk.Entry(calculator_Entry_Frame,
                                        textvariable=calculator_Entry,
                                        width=42
                                        ).grid(column=2, row=2,
                                                columnspan=3,
                                                sticky="W",
                                                pady=(0, 10)
                                                )
            ttk.Button(calculator_Entry_Frame, text="⮤",
                        command=exportInput,
                        width=0
                        ).grid(column=1, row=2,
                                pady=(0, 10),
                                padx=(24, 0),
                                sticky="E"
                                )

            ttk.Button(calculator_Frame, text="CE",
                        command=calculatorCE
                        ).grid(column=1, row=3)
            ttk.Button(calculator_Frame, text="7",
                        command=lambda:calculatorNumber("7")
                        ).grid(column=1, row=4)
            ttk.Button(calculator_Frame, text="4",
                        command=lambda:calculatorNumber("4")
                        ).grid(column=1, row=5)
            ttk.Button(calculator_Frame, text="1",
                        command=lambda:calculatorNumber("1")
                        ).grid(column=1, row=6)
            ttk.Button(calculator_Frame, text="+/-",
                        command=calculatorPositiveNegative
                        ).grid(column=1, row=7)
            ttk.Button(calculator_Frame, text="C",
                        command=calculatorC
                        ).grid(column=2, row=3)
            ttk.Button(calculator_Frame, text="8",
                        command=lambda:calculatorNumber("8")
                        ).grid(column=2, row=4)
            ttk.Button(calculator_Frame, text="5",
                        command=lambda:calculatorNumber("5")
                        ).grid(column=2, row=5)
            ttk.Button(calculator_Frame, text="2",
                        command=lambda:calculatorNumber("2")
                        ).grid(column=2, row=6)
            ttk.Button(calculator_Frame, text="0",
                        command=lambda:calculatorNumber("0")
                        ).grid(column=2, row=7)
            ttk.Button(calculator_Frame, text="<-",
                        command=calculatorRemove
                        ).grid(column=3, row=3)
            ttk.Button(calculator_Frame, text="9",
                        command=lambda:calculatorNumber("9")
                        ).grid(column=3, row=4)
            ttk.Button(calculator_Frame, text="6",
                        command=lambda:calculatorNumber("6")
                        ).grid(column=3, row=5)
            ttk.Button(calculator_Frame, text="3",
                        command=lambda:calculatorNumber("3")
                        ).grid(column=3, row=6)
            ttk.Button(calculator_Frame, text="x²",
                        command=calculatorSquare
                        ).grid(column=3, row=7)
            ttk.Button(calculator_Frame, text="/",
                        command=calculatorDivide
                        ).grid(column=4, row=3)
            ttk.Button(calculator_Frame, text="x",
                        command=calculatorMultiply
                        ).grid(column=4, row=4)
            ttk.Button(calculator_Frame, text="-",
                        command=calculatorSubstract
                        ).grid(column=4, row=5)
            ttk.Button(calculator_Frame, text="+",
                        command=calculatorAdd
                        ).grid(column=4, row=6)
            ttk.Button(calculator_Frame, text="=",
                        command=calculatorEquals
                        ).grid(column=4, row=7)
        calculator()

    def createInspectionFrame(self):
        settings_Tab = SettingsTab(self, display_Window=False)
        settings = settings_Tab.getSettings()
        self.decimal_Mark = settings[0]
        self.thousand_Mark = settings[1]
        self.uppercase_hexadecimal = settings[2]
        self.show_Relevant = settings[3]
        self.show_Prime = settings[4]
        self.show_Roots = settings[5]
        self.show_Factors = settings[6]
        self.show_Palindromic = settings[7]
        self.show_Fibonacci = settings[8]
        self.show_Factorial = settings[9]
        self.selected_Bases = settings[10]
        self.show_Perfects = settings[11]
        self.show_Truncatables = settings[12]
        self.show_Roman = settings[13]

        def display_Bases():
            try:
                self.prime_Frame.grid_forget()
            except:
                pass
            try:
                self.root_Frame.grid_forget()
            except:
                pass
            try:
                self.factor_Frame.grid_forget()
            except:
                pass
            try:
                self.palindromic_Frame.grid_forget()
            except:
                pass
            try:
                self.fibonacci_Frame.grid_forget()
            except:
                pass
            try:
                self.factorial_Frame.grid_forget()
            except:
                pass
            try:
                self.bases_Button.grid_forget()
            except:
                pass
            try:
                self.truncatables_Frame.grid_forget()
            except:
                pass
            try:
                self.perfects_Frame.grid_forget()
            except:
                pass

            self.page_Frame.grid(column=1, row=3)
            self.return_Button.grid(column=1, row=1)
            self.bases_Label.grid(column=1, row=2)
        def display_Normal():
            self.bases_Label.grid_forget()
            self.return_Button.grid_forget()
            try:
                self.page_Frame.grid_forget()
            except:
                pass
            if self.show_Prime:
                self.prime_Frame.grid(column=1, row=2)
            if self.show_Roots:
                self.root_Frame.grid(column=1, row=3)
            if self.show_Factors:
                self.factor_Frame.grid(column=1, row=4)
            if self.show_Palindromic:
                self.palindromic_Frame.grid(column=1, row=5)
            if self.show_Fibonacci:
                self.fibonacci_Frame.grid(column=1, row=6)
            if self.show_Factorial:
                self.factorial_Frame.grid(column=1, row=7)
            if self.show_Truncatables:
                self.truncatables_Frame.grid(column=1, row=8)
            if self.show_Perfects:
                self.perfects_Frame.grid(column=1, row=9)
            self.bases_Button.grid(column=1, row=1)

        self.selected_Number = int(self.input_Number.get())
        self.inspection_Frame = ttk.Frame(self.main_Frame)
        self.inspection_Frame.grid(column=3, row=1, rowspan=10)

        def write_Superscript(num):
            superscript = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
            string = str(num)
            result = []
            for char in string:
                digit = int(char)
                result.append(superscript[digit])
            result = "".join(result)
            return result

        def factors_Format(factors):
            count = {}
            for factor in factors:
                counter = 0
                for num in factors:
                    if factor == num:
                        counter += 1
                count[factor] = counter

            new_Factors = []
            for key in count:
                new_Factors.append("{0}{1}".format(key,
                                                   write_Superscript(count[key])
                                                   )
                                   )
            return "*".join(new_Factors)

        global wiki
        wiki = PhotoImage(file="Wikipedia_logo.gif")

        #current_Time = time.time()
        def hyperlink(url):
            webbrowser.open(url, new=2, autoraise=True)

        if self.show_Prime:
            is_Prime = properties.isItPrime(self.selected_Number)
            if is_Prime:
                prime_Text = "{0} is a prime number".format(self.selected_Number)
            else:
                prime_Text = "{0} is not a prime number".format(self.selected_Number)
            self.prime_Frame = ttk.Frame(self.inspection_Frame)
            self.prime_Frame.grid(column=1, row=2)
            self.prime_Label = ttk.Label(self.prime_Frame, text=prime_Text)
            self.prime_Label.grid(column=1, row=1)
            self.prime_Wiki = Button(self.prime_Frame,
                                     image=wiki,
                                     command=lambda:hyperlink("https://en.wikipedia.org/wiki/Prime_number"))
            self.prime_Wiki.grid(column=2, row=1)
            if self.show_Relevant and not is_Prime:
                self.prime_Frame.grid_forget()
                self.show_Prime = False
            #prime_Time = time.time() - current_Time
            #print("prime time: {0}".format(prime_Time))

        if self.show_Roots:
            #current_Time = time.time()
            has_Roots = True
            if self.selected_Number == 1:
                root_Text = "1's nth root 1"
            elif self.selected_Number == -1:
                root_Text = "-1's every odd root -1"
            else:
                its_Roots = properties.itsRoots(self.selected_Number)
                root_Text = ""
                for root in its_Roots:
                    root_Text = root_Text\
                                + str(self.selected_Number)\
                                + "'s "\
                                + root\
                                + "\n"
                root_List = list(root_Text)
                if len(root_Text) != 0:
                    del root_List[len(root_List) - 1]
                    root_Text = "".join(root_List)
                else:
                    if self.selected_Number != 1 or self.selected_Number != -1:
                        has_Roots = False
                        root_Text = "{0} has no perfect roots"\
                                    .format(self.selected_Number)
            self.root_Frame = ttk.Frame(self.inspection_Frame)
            self.root_Frame.grid(column=1, row=3)
            self.root_Label = ttk.Label(self.root_Frame, text=root_Text)
            self.root_Label.grid(column=1, row=1)
            self.root_Wiki = Button(self.root_Frame,
                                    image=wiki,
                                    command=lambda:hyperlink("https://en.wikipedia.org/wiki/Nth_root"))
            self.root_Wiki.grid(column=2, row=1)
            if self.show_Relevant and not has_Roots:
                self.show_Roots = False
                self.root_Frame.grid_forget()
            #root_Time = time.time() - current_Time
            #print("root time: {0}".format(root_Time))

        if self.show_Factors:
            #current_Time = time.time()
            if self.selected_Number <= 0:
                factors_Text = "{0} = 1*{0}".format(self.selected_Number)
                is_Positive = False
            else:
                is_Positive = True
                factors = properties.checkPrimeFactors(self.selected_Number)
                if is_Prime:
                    factors_Text = "{0} = 1*{0}".format(self.selected_Number)
                else:
                    factors = factors_Format(factors)
                    factors_Text = "{0} = {1}".format(self.selected_Number,
                                                      factors)
            self.factor_Frame = ttk.Frame(self.inspection_Frame)
            self.factor_Frame.grid(column=1, row=4)
            self.factor_Label = ttk.Label(self.factor_Frame, text=factors_Text)
            self.factor_Label.grid(column=1, row=1)
            self.factor_Wiki = Button(self.factor_Frame,
                                      image=wiki,
                                      command=lambda:hyperlink("https://en.wikipedia.org/wiki/Factorization"))
            self.factor_Wiki.grid(column=2, row=1)
            if self.show_Relevant and not is_Positive:
                self.show_Factors = False
                self.factor_Frame.grid_forget()
            #factor_Time = time.time() - current_Time
            #print("factor time: {0}".format(factor_Time))

        if self.show_Palindromic:
            #current_Time = time.time()
            is_Palindromic = properties.isItPalindromic(self.selected_Number)
            if is_Palindromic:
                palindromic_Text = "{0} is a palindromic number"\
                                    .format(self.selected_Number)
            else:
                palindromic_Text = "{0} is not a palindromic number"\
                                    .format(self.selected_Number)
            self.palindromic_Frame = ttk.Frame(self.inspection_Frame)
            self.palindromic_Frame.grid(column=1, row=5)
            self.palindromic_Label = ttk.Label(self.palindromic_Frame,
                                                text=palindromic_Text)
            self.palindromic_Label.grid(column=1, row=1)
            self.palindromic_Wiki = Button(self.palindromic_Frame,
                                           image=wiki,
                                           command=lambda:hyperlink("https://en.wikipedia.org/wiki/Palindromic_number"))
            self.palindromic_Wiki.grid(column=2, row=1)
            if self.show_Relevant and not is_Palindromic:
                self.show_Palindromic = False
                self.palindromic_Frame.grid_forget()
            #palindromic_Time = time.time() - current_Time
            #print("palindromic time: {0}".format(palindromic_Time))

        if self.show_Fibonacci:
            #current_Time = time.time()
            in_Fibonacci = True
            if self.selected_Number <= 0:
                fibonacci_Text = "{0} does not appear in the fibonacci sequence"\
                                .format(self.selected_Number)
                in_Fibonacci = False
            else:
                place_In_Fibonacci_Sequence = properties.isItInFibonacci(self.selected_Number)
                if place_In_Fibonacci_Sequence:
                    string_Place = str(place_In_Fibonacci_Sequence)
                    listed_Place = list(string_Place)
                    if listed_Place[len(listed_Place) - 1] == "1":
                        fibonacci_Text = ("{0} is in the {1}st "
                                          "place in the fibonacci sequence")\
                                          .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)

                    elif listed_Place[len(listed_Place) - 1] == "2":
                        fibonacci_Text = ("{0} is in the {1}nd "
                                          "place in the fibonacci sequence")\
                                          .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)

                    elif listed_Place[len(listed_Place) - 1] == "3":
                        fibonacci_Text = ("{0} is in the {1}rd "
                                          "place in the fibonacci sequence")\
                                          .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)
                    else:
                        fibonacci_Text = ("{0} is in the {1}th "
                                          "place in the fibonacci sequence")\
                                          .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)
                else:
                    fibonacci_Text = ("{0} does not appear in"
                                      "the fibonacci sequence")\
                                      .format(self.selected_Number)
                    in_Fibonacci = False
            self.fibonacci_Frame = ttk.Frame(self.inspection_Frame)
            self.fibonacci_Frame.grid(column=1, row=6)
            self.fibonacci_Label = ttk.Label(self.fibonacci_Frame,
                                            text=fibonacci_Text)
            self.fibonacci_Label.grid(column=1, row=1)
            self.fibonacci_Wiki = Button(self.fibonacci_Frame,
                                         image=wiki,
                                         command=lambda:hyperlink("https://en.wikipedia.org/wiki/Fibonacci_number"))
            self.fibonacci_Wiki.grid(column=2, row=1)
            if self.show_Relevant and not in_Fibonacci:
                self.show_Fibonacci = False
                self.fibonacci_Frame.grid_forget()
            #fibonacci_Time = time.time() - current_Time
            #print("fibonacci time: {0}".format(fibonacci_Time))

        if self.show_Factorial:
            #current_Time = time.time()
            has_Factorial = True
            if self.selected_Number >= 0:
                factorial_Result = properties.factorial(self.selected_Number)
                if factorial_Result != "number too big":
                    if len(str(factorial_Result)) > 10:
                        list_Result = list(str(factorial_Result))
                        exponent = len(list_Result) - 1
                        factorial_Result = list_Result[0]\
                                            + self.decimal_Mark\
                                            + list_Result[1]\
                                            + list_Result[2]\
                                            + "*10^"\
                                            + str(exponent)
                    factorial_Text = "{0}! = {1}".format(self.selected_Number,
                                                            factorial_Result)
                else:
                    factorial_Text = "{0}! is too big"\
                                     .format(self.selected_Number)
            else:
                has_Factorial = False
                factorial_Text = "{0} has no factorial"\
                                 .format(self.selected_Number)
            self.factorial_Frame = ttk.Frame(self.inspection_Frame)
            self.factorial_Frame.grid(column=1, row=7)
            self.factorial_Label = ttk.Label(self.factorial_Frame,
                                             text=factorial_Text)
            self.factorial_Label.grid(column=1, row=1)
            self.factorial_Wiki = Button(self.factorial_Frame,
                                         image=wiki,
                                         command=lambda:hyperlink("https://en.wikipedia.org/wiki/Factorial"))
            self.factorial_Wiki.grid(column=2, row=1)
            if (self.show_Relevant and factorial_Result == "number too big")\
                or (self.show_Relevant and not has_Factorial):
                self.show_Factorial = False
                self.factorial_Frame.grid_forget()
            #factorial_Time = time.time() - current_Time
            #print("factorial time: {0}".format(factorial_Time))
            #print()
            #print()
            #print()

        if self.show_Truncatables:
            truncatables_Text = ""
            is_Truncatable = properties.truncatablePrime(self.selected_Number)
            if is_Truncatable:
                truncatables_Text = "{0} is a left-truncatable prime"\
                                    .format(self.selected_Number)
            else:
                truncatables_Text = "{0} is not a left-truncatable prime"\
                                    .format(self.selected_Number)
            self.truncatables_Frame = ttk.Frame(self.inspection_Frame)
            self.truncatables_Frame.grid(column=1, row=8)
            self.truncatables_Label = ttk.Label(self.truncatables_Frame,
                                                text=truncatables_Text)
            self.truncatables_Label.grid(column=1, row=1)
            self.truncatables_Wiki = Button(self.truncatables_Frame,
                                            image=wiki,
                                            command=lambda:hyperlink("https://en.wikipedia.org/wiki/Truncatable_prime"))
            self.truncatables_Wiki.grid(column=2, row=1)
            if not is_Truncatable and self.show_Relevant:
                self.show_Truncatables = False
                self.truncatables_Frame.grid_forget()

        if self.show_Perfects:
            perfects_Text = ""
            is_Perfect = properties.isItPerfect(self.selected_Number)
            if is_Perfect:
                perfects_Text = "{0} is a {1}-perfect number"\
                                .format(self.selected_Number,
                                        is_Perfect)
            else:
                perfects_Text = "{0} is not a perfect number"\
                                .format(self.selected_Number)
            self.perfects_Frame = ttk.Frame(self.inspection_Frame)
            self.perfects_Frame.grid(column=1, row=9)
            self.perfects_Label = ttk.Label(self.perfects_Frame,
                                            text=perfects_Text)
            self.perfects_Label.grid(column=1, row=1)
            self.perfects_Wiki = Button(self.perfects_Frame,
                                        image=wiki,
                                        command=lambda:hyperlink("https://en.wikipedia.org/wiki/Perfect_number"))
            self.perfects_Wiki.grid(column=2, row=1)
            if not is_Perfect and self.show_Relevant:
                self.show_Perfects = False
                self.perfects_Frame.grid_forget()

        TNR = tkFont.Font(family="Times New Roman", size=9)
        if self.show_Roman: # WIP TODO: add font
            if self.selected_Number == 0:
                roman_Text = "0 has no representation in roman"
                roman_Numeral = ""
                relevant = False
            else:
                relevant = True
                num = abs(self.selected_Number)
                roman_Numeral = properties.roman(num)
                if self.selected_Number < 0:
                    roman_Numeral = "-" + roman_Numeral
                roman_Text = "{0} in roman: ".format(self.selected_Number)
            self.roman_Frame = ttk.Frame(self.inspection_Frame)
            self.roman_Frame.grid(column=1, row=10)
            self.roman_Label = ttk.Label(self.roman_Frame,
                                            text=roman_Text
                                            )
            self.roman_Label.grid(column=1, row=1)
            self.roman_Label_Num = ttk.Label(self.roman_Frame,
                                            text=roman_Numeral,
                                            font=TNR
                                            )
            self.roman_Label_Num.grid(column=2, row=1)
            self.perfects_Wiki = Button(self.roman_Frame,
                                        image=wiki,
                                        command=lambda:hyperlink("https://en.wikipedia.org/wiki/Roman_numerals"))
            self.perfects_Wiki.grid(column=3, row=1)
            if not relevant and self.show_Relevant:
                self.show_Roman = False
                self.roman_Frame.grid_forget()

        self.show_Bases = self.selected_Bases != set({})
        if self.show_Bases:
            bases_Text = StringVar()
            bases_Text1 = ""
            bases_Text2 = ""
            bases_Text3 = ""
            iteration_Count = 0
            for base in self.selected_Bases:
                listed_Base = list(str(base))
                if listed_Base[len(listed_Base) - 1] == "1":
                    sufix = "st"
                elif listed_Base[len(listed_Base) - 1] == "2":
                    sufix = "nd"
                elif listed_Base[len(listed_Base) - 1] == "3":
                    sufix = "rd"
                else:
                    sufix = "th"
                if iteration_Count < 12:
                    bases_Text1 = bases_Text1\
                                 + "{0} in {1}{2} base: ".format(self.selected_Number,
                                                                base, sufix)\
                                 + properties.convertToBaseX(self.selected_Number,
                                                             base)\
                                 + "\n"
                elif iteration_Count < 24:
                    bases_Text2 = bases_Text2\
                                 + "{0} in {1}{2} base: ".format(self.selected_Number,
                                                                base, sufix)\
                                 + properties.convertToBaseX(self.selected_Number,
                                                             base)\
                                 + "\n"
                else:
                    bases_Text3 = bases_Text3\
                                 + "{0} in {1}{2} base: ".format(self.selected_Number,
                                                                base, sufix)\
                                 + properties.convertToBaseX(self.selected_Number,
                                                             base)\
                                 + "\n"
                iteration_Count += 1
            bases_Text.set(bases_Text1)
            self.bases_Label = ttk.Label(self.inspection_Frame,
                                         textvariable=bases_Text)
            def changetoPage1():
                bases_Text.set(bases_Text1)
                self.page1_Button.state(["disabled"])
                self.page2_Button.state(["!disabled"])
                self.page3_Button.state(["!disabled"])
            def changeToPage2():
                self.page1_Button.state(["!disabled"])
                self.page2_Button.state(["disabled"])
                self.page3_Button.state(["!disabled"])
                bases_Text.set(bases_Text2)
            def changeToPage3():
                self.page1_Button.state(["!disabled"])
                self.page2_Button.state(["!disabled"])
                self.page3_Button.state(["disabled"])
                bases_Text.set(bases_Text3)
            self.page_Frame = ttk.Frame(self.inspection_Frame)
            self.page_Frame.grid(column=1, row=3)
            self.page1_Button = ttk.Button(self.page_Frame,
                                      text="1",
                                      command=changetoPage1,
                                      state="disabled",
                                      width=2)
            self.page2_Button = ttk.Button(self.page_Frame,
                                      text="2",
                                      command=changeToPage2,
                                      width=2)
            self.page3_Button = ttk.Button(self.page_Frame,
                                      text="3",
                                      command=changeToPage3,
                                      width=2)
            if bases_Text2:
                self.page1_Button.grid(column=1, row=1)
                self.page2_Button.grid(column=2, row=1)
            if bases_Text3:
                self.page3_Button.grid(column=3, row=1)

            self.bases_Button = ttk.Button(self.inspection_Frame,
                                      text="BASES",
                                      command=display_Bases)
            if (self.show_Prime
                   or self.show_Roots
                   or self.show_Factors
                   or self.show_Palindromic
                   or self.show_Fibonacci
                   or self.show_Factorial
                   or self.show_Truncatables
                   or self.show_Perfects):
                self.page_Frame.grid_forget()
                self.bases_Button.grid(column=1, row=1)
            else:
                self.bases_Label.grid(column=1, row=2)

        if (self.show_Prime
               or self.show_Roots
               or self.show_Factors
               or self.show_Palindromic
               or self.show_Fibonacci
               or self.show_Factorial
               or self.show_Truncatables
               or self.show_Perfects):
            self.return_Button = ttk.Button(self.inspection_Frame,
                                       text="<---",
                                       command=display_Normal)

    def createMenu(self):
        def settingsTab():
            self.main_Frame.grid_forget()
            settings_Tab = SettingsTab(self)
        menu_Bar = Menu(self)
        self.config(menu=menu_Bar)

        self.settings = Menu(menu_Bar, tearoff=0)

        self.settings.add_command(label="Open Settings Window",
                                    command=settingsTab)
        self.settings.add_separator()
        self.settings.add_command(label="Exit", command=self.quit)
        menu_Bar.add_cascade(label="Settings", menu=self.settings)

root = Application()
root.inspection_Entry.focus()
root.mainloop()
