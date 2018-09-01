#cd D:\Diego\Documents\GitHub\Number-Inspection-Program
"""List of things to implement:
Prime check [True]
Square(or cube or whatever) root check [True]
Binary [True]
Hexadecimal [True]

The number in all bases(up to 36) [False]

If it's not prime, check it's factors [True]
Palindromic check [True]

Truncatable prime [False]
Perfect(or triperfect or whatever) number [False]

Factorial [True]

Superpermutation [False] (i don't think i will do this but maybe)

Fibonacci [True]
Support for the number 0 and negative numbers [True]

Hyperlink to a page in wikipedia explaining the property [False]
Save favorite numbers with the option of a note to explain why [False]
Support for numbers in any base [False]
Sexagesimal [False]
Duodecimal [False]
Vigesimal [False]
9/18.5
Variable maximum number [False]
Roman number [False]
Spanish support [False]
"""



from tkinter import *
from tkinter import ttk
import time

class Application(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.createSettingsVariables()
        self.createInitialWidgets()
        self.createMenu()

    def createSettingsVariables(self):
        self.decimal_Mark = ","
        self.thousand_Mark = "."
        self.uppercase_hexadecimal = BooleanVar()
        self.uppercase_hexadecimal.set(False)
        self.decimal_Separator = IntVar()
        self.decimal_Separator.set(1)

        self.show_Relevant = BooleanVar()
        self.show_Relevant.set(True)
        self.show_Prime = BooleanVar()
        self.show_Prime.set(True)
        self.show_Roots = BooleanVar()
        self.show_Roots.set(True)
        self.show_Binary = BooleanVar()
        self.show_Binary.set(True)
        self.show_Hexadecimal = BooleanVar()
        self.show_Hexadecimal.set(True)
        self.show_Factors = BooleanVar()
        self.show_Factors.set(True)
        self.show_Palindromic = BooleanVar()
        self.show_Palindromic.set(True)
        self.show_Fibonacci = BooleanVar()
        self.show_Fibonacci.set(True)
        self.show_Factorial = BooleanVar()
        self.show_Factorial.set(True)

        self.selected_Bases = {2, 8, 10, 16}
        self.show_All_Bases = BooleanVar()
        self.show_All_Bases.set(False)
        self.show_Base_2 = BooleanVar()
        self.show_Base_2.set(True)
        self.show_Base_3 = BooleanVar()
        self.show_Base_3.set(False)
        self.show_Base_4 = BooleanVar()
        self.show_Base_4.set(False)
        self.show_Base_5 = BooleanVar()
        self.show_Base_5.set(False)
        self.show_Base_6 = BooleanVar()
        self.show_Base_6.set(False)
        self.show_Base_7 = BooleanVar()
        self.show_Base_7.set(False)
        self.show_Base_8 = BooleanVar()
        self.show_Base_8.set(True)
        self.show_Base_9 = BooleanVar()
        self.show_Base_9.set(False)
        self.show_Base_10 = BooleanVar()
        self.show_Base_10.set(True)
        self.show_Base_11 = BooleanVar()
        self.show_Base_11.set(False)
        self.show_Base_12 = BooleanVar()
        self.show_Base_12.set(False)
        self.show_Base_13 = BooleanVar()
        self.show_Base_13.set(False)
        self.show_Base_14 = BooleanVar()
        self.show_Base_14.set(False)
        self.show_Base_15 = BooleanVar()
        self.show_Base_15.set(False)
        self.show_Base_16 = BooleanVar()
        self.show_Base_16.set(True)
        self.show_Base_17 = BooleanVar()
        self.show_Base_17.set(False)
        self.show_Base_18 = BooleanVar()
        self.show_Base_18.set(False)
        self.show_Base_19 = BooleanVar()
        self.show_Base_19.set(False)
        self.show_Base_20 = BooleanVar()
        self.show_Base_20.set(False)
        self.show_Base_21 = BooleanVar()
        self.show_Base_21.set(False)
        self.show_Base_22 = BooleanVar()
        self.show_Base_22.set(False)
        self.show_Base_23 = BooleanVar()
        self.show_Base_23.set(False)
        self.show_Base_24 = BooleanVar()
        self.show_Base_24.set(False)
        self.show_Base_25 = BooleanVar()
        self.show_Base_25.set(False)
        self.show_Base_26 = BooleanVar()
        self.show_Base_26.set(False)
        self.show_Base_27 = BooleanVar()
        self.show_Base_27.set(False)
        self.show_Base_28 = BooleanVar()
        self.show_Base_28.set(False)
        self.show_Base_29 = BooleanVar()
        self.show_Base_29.set(False)
        self.show_Base_30 = BooleanVar()
        self.show_Base_30.set(False)
        self.show_Base_31 = BooleanVar()
        self.show_Base_31.set(False)
        self.show_Base_32 = BooleanVar()
        self.show_Base_32.set(False)
        self.show_Base_33 = BooleanVar()
        self.show_Base_33.set(False)
        self.show_Base_34 = BooleanVar()
        self.show_Base_34.set(False)
        self.show_Base_35 = BooleanVar()
        self.show_Base_35.set(False)
        self.show_Base_36 = BooleanVar()
        self.show_Base_36.set(False)

    def createInitialWidgets(self):
        def inspect(event=None):
            try:
                slaves = self.inspection_Frame.destroy()
                for slave in slaves:
                    slave.grid_forget()
            except:
                pass
            self.createInspectionFrame()
        self.input_Number = StringVar()
        self.bind("<Return>", inspect)
        self.main_Frame = ttk.Frame(self)
        self.main_Frame.grid(column=1, row=1)
        ttk.Entry(self.main_Frame, textvariable=self.input_Number)\
                .grid(column=1, row=1)
        ttk.Button(self.main_Frame,
                    command=inspect,
                    text="inspect").grid(column=2, row=1)

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
        ttk.Button(calculator_Frame, text="x^2",
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

    def createInspectionFrame(self):
        self.selected_Number = int(self.input_Number.get())
        self.inspection_Frame = ttk.Frame(self.main_Frame)
        self.inspection_Frame.grid(column=3, row=1, rowspan=3)

        #current_Time = time.time()
        if self.show_Prime.get():
            if self.selected_Number <= 0:
                is_Prime = False
                prime_Text = "{0} is not a prime number".format(self.selected_Number)
            else:
                is_Prime = self.isItPrime(self.selected_Number)
                if is_Prime:
                    prime_Text = "{0} is a prime number".format(self.selected_Number)
                else:
                    if self.show_Relevant:
                        prime_Text =""
                    else:
                        prime_Text = "{0} is not a prime number"\
                                    .format(self.selected_Number)
            self.prime_Label = ttk.Label(self.inspection_Frame, text=prime_Text)
            self.prime_Label.grid(column=1, row=1)
            if self.show_Relevant and not is_Prime:
                self.prime_Label.grid_forget()
            #prime_Time = time.time() - current_Time
            #print("prime time: {0}".format(prime_Time))

        if self.show_Roots.get():
            #current_Time = time.time()
            has_Roots = True
            if self.selected_Number == 1:
                root_Text = "1's nth root 1"
            elif self.selected_Number == -1:
                root_Text = "-1's every odd root -1"
            else:
                its_Roots = self.itsRoots()
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
            self.root_Label = ttk.Label(self.inspection_Frame, text=root_Text)
            self.root_Label.grid(column=1, row=2)
            if self.show_Relevant and not has_Roots:
                self.root_Label.grid_forget()
            #root_Time = time.time() - current_Time
            #print("root time: {0}".format(root_Time))

        if self.show_Binary.get():
            #current_Time = time.time()
            if self.selected_Number == 0:
                binary_Text = "0 in binary: 0"
            else:
                number_In_Binary = self.convertToBinary()
                if self.selected_Number < 0:
                    binary_Text = "{0} in binary: -{1}".format(self.selected_Number,
                                                                number_In_Binary)
                elif self.selected_Number == 0:
                    binary_Text = "0 in binary: 0"
                else:
                    binary_Text = "{0} in binary: {1}".format(self.selected_Number,
                                                                number_In_Binary)
            self.binary_Label = ttk.Label(self.inspection_Frame, text=binary_Text)
            self.binary_Label.grid(column=1, row=3)
            #binary_Time = time.time() - current_Time
            #print("binary time: {0}".format(binary_Time))

        if self.show_Hexadecimal.get():
            #current_Time = time.time()
            if self.selected_Number == 0:
                hexadecimal_Text = "0 in hexadecimal: 0"
            else:
                number_In_Hexadecimal = self.convertToHexadecimal()
                if self.selected_Number < 0:
                    hexadecimal_Text = "{0} in hexadecimal: -{1}"\
                                        .format(self.selected_Number,
                                                number_In_Hexadecimal)
                else:
                    hexadecimal_Text = "{0} in hexadecimal: {1}"\
                                        .format(self.selected_Number,
                                                number_In_Hexadecimal)
            self.hexadecimal_Label = ttk.Label(self.inspection_Frame,
                                                text=hexadecimal_Text)
            self.hexadecimal_Label.grid(column=1, row=4)
            #hexadecimal_Time = time.time() - current_Time
            #print("hexadecimal time: {0}".format(hexadecimal_Time))

        if self.show_Factors.get():
            #current_Time = time.time()
            if self.selected_Number == 0:
                factors_Text = "{0} = 1*{0}".format(self.selected_Number)
            else:
                factors = self.checkFactors()
                if is_Prime:
                    factors_Text = "{0} = 1*{0}".format(self.selected_Number)
                else:
                    factors = "*".join(factors)
                    if self.selected_Number < 1: # !!!!!!!!!! WIP !!!!!!!!!!!!
                        factors_Text = "{0} = -1*{1}".format(self.selected_Number,
                                                                factors)
                    else:
                        factors_Text = "{0} = {1}".format(self.selected_Number,
                                                            factors)
            self.factor_Label = ttk.Label(self.inspection_Frame, text=factors_Text)
            self.factor_Label.grid(column=1, row=5)
            #factor_Time = time.time() - current_Time
            #print("factor time: {0}".format(factor_Time))

        if self.show_Palindromic.get():
            #current_Time = time.time()
            is_Palindromic = self.isItPalindromic()
            if is_Palindromic:
                palindromic_Text = "{0} is a palindromic number"\
                                    .format(self.selected_Number)
            else:
                palindromic_Text = "{0} is not a palindromic number"\
                                    .format(self.selected_Number)
            self.palindromic_Label = ttk.Label(self.inspection_Frame,
                                                text=palindromic_Text)
            self.palindromic_Label.grid(column=1, row=6)
            if self.show_Relevant and not is_Palindromic:
                self.palindromic_Label.grid_forget()
            #palindromic_Time = time.time() - current_Time
            #print("palindromic time: {0}".format(palindromic_Time))

        if self.show_Fibonacci.get():
            #current_Time = time.time()
            in_Fibonacci = True
            if self.selected_Number <= 0:
                fibonacci_Text = "{0} does not appear in the fibonacci sequence"\
                                .format(self.selected_Number)
                in_Fibonacci = False
            else:
                place_In_Fibonacci_Sequence = self.isItInFibonacci()
                if place_In_Fibonacci_Sequence:
                    string_Place = str(place_In_Fibonacci_Sequence)
                    listed_Place = list(string_Place)
                    if listed_Place[len(listed_Place) - 1] == "1":
                        fibonacci_Text = "{0} is in the {1}st place in thefibonacci sequence"\
                                        .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)
                    elif listed_Place[len(listed_Place) - 1] == "2":
                        fibonacci_Text = "{0} is in the {1}nd place in the fibonacci sequence"\
                                        .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)
                    elif listed_Place[len(listed_Place) - 1] == "3":
                        fibonacci_Text = "{0} is in the {1}rd place in the fibonacci sequence"\
                                        .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)
                    else:
                        fibonacci_Text = "{0} is in the {1}th place in the fibonacci sequence"\
                                        .format(self.selected_Number,
                                                place_In_Fibonacci_Sequence)
                else:
                    fibonacci_Text = "{0} does not appear in the fibonacci sequence"\
                                    .format(self.selected_Number)
                    in_Fibonacci = False
            self.fibonacci_Label = ttk.Label(self.inspection_Frame,
                                            text=fibonacci_Text)
            self.fibonacci_Label.grid(column=1, row=7)
            if self.show_Relevant and not in_Fibonacci:
                self.fibonacci_Label.grid_forget()
            #fibonacci_Time = time.time() - current_Time
            #print("fibonacci time: {0}".format(fibonacci_Time))

        if self.show_Factorial.get():
            #current_Time = time.time()
            has_Factorial = True
            if self.selected_Number >= 0:
                factorial_Result = self.factorial()
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
                    factorial_Text = "{0}! is too big".format(self.selected_Number)
            else:
                has_Factorial = False
                factorial_Text = "{0} has no factorial".format(self.selected_Number)
            self.factorial_Label = ttk.Label(self.inspection_Frame,
                                                text=factorial_Text)
            self.factorial_Label.grid(column=1, row=8)
            if self.show_Relevant and not has_Factorial:
                self.factorial_Label.grid_forget()
            #factorial_Time = time.time() - current_Time
            #print("factorial time: {0}".format(factorial_Time))
            #print()
            #print()
            #print()

    def createMenu(self):
        menu_Bar = Menu(self)
        self.config(menu=menu_Bar)

        self.settings = Menu(menu_Bar, tearoff=0)

        self.settings.add_command(label="Open Settings Window",
                                    command=self.settingsWindow)
        self.settings.add_separator()
        self.settings.add_command(label="Exit", command=self.quit)
        menu_Bar.add_cascade(label="Settings", menu=self.settings)

    def settingsWindow(self):
        def goBack():
            self.settings_Window_Frame.grid_forget()
            self.createInitialWidgets()
        self.main_Frame.grid_forget()
        self.settings_Window_Frame = ttk.Frame(self)
        self.settings_Window_Frame.grid(column=1, row=1)
        ttk.Button(self.settings_Window_Frame, text="<--", command=goBack, width=0)\
                    .grid(column=1, row=1, sticky=(NW))

        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show only relevant information",
                        variable=self.show_Relevant,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=1, row=2, columnspan=2)
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show if the number is prime",
                        variable=self.show_Prime,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=1, row=3, sticky="W")
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show the number's roots",
                        variable=self.show_Roots,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=1, row=4, sticky="W")
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show the number in binary",
                        variable=self.show_Binary,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=1, row=5, sticky="W")
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show the number in hexadecimal",
                        variable=self.show_Hexadecimal,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=1, row=6, sticky="W")
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show the number's factors",
                        variable=self.show_Factors,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=2, row=3, sticky="W")
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show if the number is palindromic",
                        variable=self.show_Palindromic,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=2, row=4, sticky="W")
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show the number in the Fibonacci sequence",
                        variable=self.show_Fibonacci,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=2, row=5, sticky="W")
        ttk.Checkbutton(self.settings_Window_Frame,
                        text="Show the factorial of the number",
                        variable=self.show_Factorial,
                        onvalue=True,
                        offvalue=False
                        ).grid(column=2, row=6, sticky="W")

        def updateDecimalSeparator():
            if self.decimal_Separator.get() == 1:
                self.decimal_Mark = ","
                self.thousand_Mark = "."
            elif self.decimal_Separator.get() == 2:
                self.decimal_Mark = "."
                self.thousand_Mark = ","
        self.cosmetic_Preferences_Frame = ttk.Frame(self.settings_Window_Frame,
                                                    padding="0 15 0 0"
                                                    ).grid(column=1,
                                                           row=7)

        ttk.Label(self.cosmetic_Preferences_Frame,
                  text="Show numbers the following way:").grid(column=1, row=7)
        ttk.Radiobutton(self.cosmetic_Preferences_Frame, text="10000/3 = 3.333,33",
                        variable=self.decimal_Separator,
                        value=1,
                        command=updateDecimalSeparator
                        ).grid(column=1, row=8)
        ttk.Radiobutton(self.cosmetic_Preferences_Frame, text="10000/3 = 3,333.33",
                        variable=self.decimal_Separator,
                        value=2,
                        command=updateDecimalSeparator
                        ).grid(column=1, row=9)

        ttk.Label(self.cosmetic_Preferences_Frame,
                  text="Show numbers in base 10+ the following way:"
                  ).grid(column=2, row=7)
        ttk.Radiobutton(self.cosmetic_Preferences_Frame, text="A78FC0",
                        variable=self.uppercase_hexadecimal,
                        value=True).grid(column=2, row=8)
        ttk.Radiobutton(self.cosmetic_Preferences_Frame, text="a78fc0",
                        variable=self.uppercase_hexadecimal,
                        value=False).grid(column=2, row=9)

        self.base_Settings_Frame = ttk.Frame(self, padding="15 0 0 0")
        self.base_Settings_Frame.grid(column=2, row=1)
        self.base_Settings_Frame.columnconfigure(1, weight=1)
        self.base_Settings_Frame.columnconfigure(2, weight=1)
        self.base_Settings_Frame.columnconfigure(3, weight=1)
        self.base_Settings_Frame.columnconfigure(4, weight=1)
        self.base_Settings_Frame.columnconfigure(5, weight=1)
        self.base_Settings_Frame.columnconfigure(6, weight=1)
        ttk.Label(self.base_Settings_Frame, text="Display the number in the following bases:").grid(column=1, row=1, columnspan=6)
        def updateBases(base, boolean):
            if boolean == True:
                self.selected_Bases.add(base)
            elif boolean == False:
                self.selected_Bases.discard(base)
            if len(self.selected_Bases) == 35:
                self.show_All_Bases.set(True)
            else:
                self.show_All_Bases.set(False)
        def selectAll():
            checkbox_State = self.show_All_Bases.get()
            for base in range(37):
                if base > 1:
                    updateBases(base, checkbox_State)
            self.show_Base_2.set(self.show_All_Bases.get())
            self.show_Base_3.set(self.show_All_Bases.get())
            self.show_Base_4.set(self.show_All_Bases.get())
            self.show_Base_5.set(self.show_All_Bases.get())
            self.show_Base_6.set(self.show_All_Bases.get())
            self.show_Base_7.set(self.show_All_Bases.get())
            self.show_Base_8.set(self.show_All_Bases.get())
            self.show_Base_9.set(self.show_All_Bases.get())
            self.show_Base_10.set(self.show_All_Bases.get())
            self.show_Base_11.set(self.show_All_Bases.get())
            self.show_Base_12.set(self.show_All_Bases.get())
            self.show_Base_13.set(self.show_All_Bases.get())
            self.show_Base_14.set(self.show_All_Bases.get())
            self.show_Base_15.set(self.show_All_Bases.get())
            self.show_Base_16.set(self.show_All_Bases.get())
            self.show_Base_17.set(self.show_All_Bases.get())
            self.show_Base_18.set(self.show_All_Bases.get())
            self.show_Base_19.set(self.show_All_Bases.get())
            self.show_Base_20.set(self.show_All_Bases.get())
            self.show_Base_21.set(self.show_All_Bases.get())
            self.show_Base_22.set(self.show_All_Bases.get())
            self.show_Base_23.set(self.show_All_Bases.get())
            self.show_Base_24.set(self.show_All_Bases.get())
            self.show_Base_25.set(self.show_All_Bases.get())
            self.show_Base_26.set(self.show_All_Bases.get())
            self.show_Base_27.set(self.show_All_Bases.get())
            self.show_Base_28.set(self.show_All_Bases.get())
            self.show_Base_29.set(self.show_All_Bases.get())
            self.show_Base_30.set(self.show_All_Bases.get())
            self.show_Base_31.set(self.show_All_Bases.get())
            self.show_Base_32.set(self.show_All_Bases.get())
            self.show_Base_33.set(self.show_All_Bases.get())
            self.show_Base_34.set(self.show_All_Bases.get())
            self.show_Base_35.set(self.show_All_Bases.get())
            self.show_Base_36.set(self.show_All_Bases.get())
        ttk.Checkbutton(self.base_Settings_Frame, text="All",
                        variable=self.show_All_Bases,
                        onvalue=True,
                        offvalue=False,
                        command=selectAll
                        ).grid(column=1,
                               row=2,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="2",
                        variable=self.show_Base_2,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(2, self.show_Base_2.get())
                        ).grid(column=2,
                               row=2,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="3",
                        variable=self.show_Base_3,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(3, self.show_Base_3.get())
                        ).grid(column=3,
                               row=2,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="4",
                        variable=self.show_Base_4,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(4, self.show_Base_4.get())
                        ).grid(column=4,
                               row=2,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="5",
                        variable=self.show_Base_5,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(5, self.show_Base_5.get())
                        ).grid(column=5,
                               row=2,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="6",
                        variable=self.show_Base_6,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(6, self.show_Base_6.get())
                        ).grid(column=6,
                               row=2,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="7",
                        variable=self.show_Base_7,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(7, self.show_Base_7.get())
                        ).grid(column=1,
                               row=3,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="8",
                        variable=self.show_Base_8,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(8, self.show_Base_8.get())
                        ).grid(column=2,
                               row=3,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="9",
                        variable=self.show_Base_9,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(9, self.show_Base_9.get())
                        ).grid(column=3,
                               row=3,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="10",
                        variable=self.show_Base_10,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(10, self.show_Base_10.get())
                        ).grid(column=4,
                               row=3,
                               sticky=W)

        ttk.Checkbutton(self.base_Settings_Frame, text="11",
                        variable=self.show_Base_11,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(11, self.show_Base_11.get())
                        ).grid(column=5,
                               row=3,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="12",
                        variable=self.show_Base_12,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(12, self.show_Base_12.get())
                        ).grid(column=6,
                               row=3,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="13",
                        variable=self.show_Base_13,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(13, self.show_Base_13.get())
                        ).grid(column=1,
                               row=4,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="14",
                        variable=self.show_Base_14,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(14, self.show_Base_14.get())
                        ).grid(column=2,
                               row=4,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="15",
                        variable=self.show_Base_15,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(15, self.show_Base_15.get())
                        ).grid(column=3,
                               row=4,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="16",
                        variable=self.show_Base_16,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(16, self.show_Base_16.get())
                        ).grid(column=4,
                               row=4,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="17",
                        variable=self.show_Base_17,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(17, self.show_Base_17.get())
                        ).grid(column=5,
                               row=4,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="18",
                        variable=self.show_Base_18,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(18, self.show_Base_18.get())
                        ).grid(column=6,
                               row=4,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="19",
                        variable=self.show_Base_19,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(19, self.show_Base_19.get())
                        ).grid(column=1,
                               row=5,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="20",
                        variable=self.show_Base_20,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(20, self.show_Base_20.get())
                        ).grid(column=2,
                               row=5,
                               sticky=W)

        ttk.Checkbutton(self.base_Settings_Frame, text="21",
                        variable=self.show_Base_21,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(21, self.show_Base_21.get())
                        ).grid(column=3,
                               row=5,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="22",
                        variable=self.show_Base_22,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(22, self.show_Base_22.get())
                        ).grid(column=4,
                               row=5,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="23",
                        variable=self.show_Base_23,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(23, self.show_Base_23.get())
                        ).grid(column=5,
                               row=5,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="24",
                        variable=self.show_Base_24,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(24, self.show_Base_24.get())
                        ).grid(column=6,
                               row=5,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="25",
                        variable=self.show_Base_25,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(25, self.show_Base_25.get())
                        ).grid(column=1,
                               row=6,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="26",
                        variable=self.show_Base_26,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(26, self.show_Base_26.get())
                        ).grid(column=2,
                               row=6,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="27",
                        variable=self.show_Base_27,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(27, self.show_Base_27.get())
                        ).grid(column=3,
                               row=6,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="28",
                        variable=self.show_Base_28,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(28, self.show_Base_28.get())
                        ).grid(column=4,
                               row=6,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="29",
                        variable=self.show_Base_29,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(29, self.show_Base_29.get())
                        ).grid(column=5,
                               row=6,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="30",
                        variable=self.show_Base_30,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(30, self.show_Base_30.get())
                        ).grid(column=6,
                               row=6,
                               sticky=W)

        ttk.Checkbutton(self.base_Settings_Frame, text="31",
                        variable=self.show_Base_31,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(31, self.show_Base_31.get())
                        ).grid(column=1,
                               row=7,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="32",
                        variable=self.show_Base_32,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(32, self.show_Base_32.get())
                        ).grid(column=2,
                               row=7,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="33",
                        variable=self.show_Base_33,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(33, self.show_Base_33.get())
                        ).grid(column=3,
                               row=7,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="34",
                        variable=self.show_Base_34,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(34, self.show_Base_34.get())
                        ).grid(column=4,
                               row=7,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="35",
                        variable=self.show_Base_35,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(35, self.show_Base_35.get())
                        ).grid(column=5,
                               row=7,
                               sticky=W)
        ttk.Checkbutton(self.base_Settings_Frame, text="36",
                        variable=self.show_Base_36,
                        onvalue=True,
                        offvalue=False,
                        command=lambda:updateBases(36, self.show_Base_36.get())
                        ).grid(column=6,
                               row=7,
                               sticky=W)

    def isItPrime(self, input):
        for num in range(2, input): # Tries every number
            if input % num == 0:
                return False
        return True

    def itsRoots(self):
        input_Number = abs(self.selected_Number)
        if self.selected_Number > 0:
            degree = 2
            negative = False
        elif self.selected_Number == 0:
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

    def convertToBinary(self):
        input_Number = str(self.selected_Number)[:]
        input_Number = int(input_Number)
        result = []

        while True:
            if input_Number == 1 or input_Number == -1:
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
                if self.uppercase_hexadecimal.get():
                    final_Result.append(hextable[int(result)].upper())
                else:
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
        absolute_Number = abs(self.selected_Number)
        if absolute_Number == 1:
            factors = ["1"]
            return factors
        factors = []
        for num in range(1, int(self.selected_Number / 2)):
            if self.selected_Number % num == 0 and self.isItPrime(num):
                factors.append(str(num))
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

    def factorial(self):
        if self.selected_Number <= 50000:
            product = 1
            factor = 1
            while factor <= self.selected_Number:
                product = product * factor
                factor += 1
            return product
        else:
            return "number too big"

    def convertToBaseX(self, base): # Max base = 36
        conversionTable = {0: "0",
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
        input_Number = str(self.selected_Number)[:]
        input_Number = int(input_Number)
        result = []

        while True:
            if input_Number in [-1, 0, 1]:
                result.append(int(input_Number % base))
                break
            result.append(int(input_Number % base))
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

root = Application()
root.mainloop()
