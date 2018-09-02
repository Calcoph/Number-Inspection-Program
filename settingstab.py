from tkinter import *
from tkinter import ttk
import repairsettings

class SettingsTab:
    def __init__(self, parent):
        self.createSettingsVariables()
        self.settingsWindow(parent)
    def setSettingsValues(self, variable_Name, value_Type):
        with open("settings.txt") as settings:
            for line in settings:
                reading_Variable_Name = repairsettings.getVariableName(line)
                if reading_Variable_Name == variable_Name:
                    value = repairsettings.getRestOfLine(line)
        if value_Type == "string":
            value = list(value)
            value = value[1:-1]
            value = "".join(value)
        elif value_Type == "boolean":
            if value == "True":
                value = True
            elif value == "False":
                value = False
        elif value_Type == "int":
            value = int(value)
        elif value_Type == "set":# WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP
            new_Set = set({})
            listed_Value = list(value)
            digit_Storage = ""
            for item in listed_Value:
                if item.isdigit():
                    digit_Storage = digit_Storage + item
                elif item == "," or item == "}":
                    new_Set.add(int(digit_Storage))
                    digit_Storage = ""
            value = new_Set
        return value
    def createSettingsVariables(self):
        repairsettings.repairSettings()
        self.decimal_Mark = self.setSettingsValues("decimal_Mark", "string")
        self.thousand_Mark = self.setSettingsValues("thousand_Mark", "string")
        self.uppercase_hexadecimal = BooleanVar()
        self.uppercase_hexadecimal.set(self.setSettingsValues("uppercase_hexadecimal",
                                                              "boolean"))
        self.decimal_Separator = IntVar()
        self.decimal_Separator.set(self.setSettingsValues("decimal_Separator",
                                                          "int"))

        self.show_Relevant = BooleanVar()
        self.show_Relevant.set(self.setSettingsValues("show_Relevant",
                                                      "boolean"))
        self.show_Prime = BooleanVar()
        self.show_Prime.set(self.setSettingsValues("show_Prime",
                                                   "boolean"))
        self.show_Roots = BooleanVar()
        self.show_Roots.set(self.setSettingsValues("show_Roots",
                                                   "boolean"))
        self.show_Binary = BooleanVar()
        self.show_Binary.set(self.setSettingsValues("show_Binary",
                                                    "boolean"))
        self.show_Hexadecimal = BooleanVar()
        self.show_Hexadecimal.set(self.setSettingsValues("show_Hexadecimal",
                                                         "boolean"))
        self.show_Factors = BooleanVar()
        self.show_Factors.set(self.setSettingsValues("show_Factors",
                                                     "boolean"))
        self.show_Palindromic = BooleanVar()
        self.show_Palindromic.set(self.setSettingsValues("show_Palindromic",
                                                         "boolean"))
        self.show_Fibonacci = BooleanVar()
        self.show_Fibonacci.set(self.setSettingsValues("show_Fibonacci",
                                                       "boolean"))
        self.show_Factorial = BooleanVar()
        self.show_Factorial.set(self.setSettingsValues("show_Factorial",
                                                       "boolean"))

        self.selected_Bases = self.setSettingsValues("selected_Bases", "set")
        self.show_All_Bases = BooleanVar()
        self.show_All_Bases.set(self.setSettingsValues("show_All_Bases",
                                                       "boolean"))
        self.show_Base_2 = BooleanVar()
        self.show_Base_2.set(self.setSettingsValues("show_Base_2",
                                                    "boolean"))
        self.show_Base_3 = BooleanVar()
        self.show_Base_3.set(self.setSettingsValues("show_Base_3",
                                                    "boolean"))
        self.show_Base_4 = BooleanVar()
        self.show_Base_4.set(self.setSettingsValues("show_Base_4",
                                                    "boolean"))
        self.show_Base_5 = BooleanVar()
        self.show_Base_5.set(self.setSettingsValues("show_Base_5",
                                                    "boolean"))
        self.show_Base_6 = BooleanVar()
        self.show_Base_6.set(self.setSettingsValues("show_Base_6",
                                                    "boolean"))
        self.show_Base_7 = BooleanVar()
        self.show_Base_7.set(self.setSettingsValues("show_Base_7",
                                                    "boolean"))
        self.show_Base_8 = BooleanVar()
        self.show_Base_8.set(self.setSettingsValues("show_Base_8",
                                                    "boolean"))
        self.show_Base_9 = BooleanVar()
        self.show_Base_9.set(self.setSettingsValues("show_Base_9",
                                                    "boolean"))
        self.show_Base_10 = BooleanVar()
        self.show_Base_10.set(self.setSettingsValues("show_Base_10",
                                                    "boolean"))
        self.show_Base_11 = BooleanVar()
        self.show_Base_11.set(self.setSettingsValues("show_Base_11",
                                                    "boolean"))
        self.show_Base_12 = BooleanVar()
        self.show_Base_12.set(self.setSettingsValues("show_Base_12",
                                                    "boolean"))
        self.show_Base_13 = BooleanVar()
        self.show_Base_13.set(self.setSettingsValues("show_Base_13",
                                                    "boolean"))
        self.show_Base_14 = BooleanVar()
        self.show_Base_14.set(self.setSettingsValues("show_Base_14",
                                                    "boolean"))
        self.show_Base_15 = BooleanVar()
        self.show_Base_15.set(self.setSettingsValues("show_Base_15",
                                                    "boolean"))
        self.show_Base_16 = BooleanVar()
        self.show_Base_16.set(self.setSettingsValues("show_Base_16",
                                                    "boolean"))
        self.show_Base_17 = BooleanVar()
        self.show_Base_17.set(self.setSettingsValues("show_Base_17",
                                                    "boolean"))
        self.show_Base_18 = BooleanVar()
        self.show_Base_18.set(self.setSettingsValues("show_Base_18",
                                                    "boolean"))
        self.show_Base_19 = BooleanVar()
        self.show_Base_19.set(self.setSettingsValues("show_Base_19",
                                                    "boolean"))
        self.show_Base_20 = BooleanVar()
        self.show_Base_20.set(self.setSettingsValues("show_Base_20",
                                                    "boolean"))
        self.show_Base_21 = BooleanVar()
        self.show_Base_21.set(self.setSettingsValues("show_Base_21",
                                                    "boolean"))
        self.show_Base_22 = BooleanVar()
        self.show_Base_22.set(self.setSettingsValues("show_Base_22",
                                                    "boolean"))
        self.show_Base_23 = BooleanVar()
        self.show_Base_23.set(self.setSettingsValues("show_Base_23",
                                                    "boolean"))
        self.show_Base_24 = BooleanVar()
        self.show_Base_24.set(self.setSettingsValues("show_Base_24",
                                                    "boolean"))
        self.show_Base_25 = BooleanVar()
        self.show_Base_25.set(self.setSettingsValues("show_Base_25",
                                                    "boolean"))
        self.show_Base_26 = BooleanVar()
        self.show_Base_26.set(self.setSettingsValues("show_Base_26",
                                                    "boolean"))
        self.show_Base_27 = BooleanVar()
        self.show_Base_27.set(self.setSettingsValues("show_Base_27",
                                                    "boolean"))
        self.show_Base_28 = BooleanVar()
        self.show_Base_28.set(self.setSettingsValues("show_Base_28",
                                                    "boolean"))
        self.show_Base_29 = BooleanVar()
        self.show_Base_29.set(self.setSettingsValues("show_Base_29",
                                                    "boolean"))
        self.show_Base_30 = BooleanVar()
        self.show_Base_30.set(self.setSettingsValues("show_Base_30",
                                                    "boolean"))
        self.show_Base_31 = BooleanVar()
        self.show_Base_31.set(self.setSettingsValues("show_Base_31",
                                                    "boolean"))
        self.show_Base_32 = BooleanVar()
        self.show_Base_32.set(self.setSettingsValues("show_Base_32",
                                                    "boolean"))
        self.show_Base_33 = BooleanVar()
        self.show_Base_33.set(self.setSettingsValues("show_Base_33",
                                                    "boolean"))
        self.show_Base_34 = BooleanVar()
        self.show_Base_34.set(self.setSettingsValues("show_Base_34",
                                                    "boolean"))
        self.show_Base_35 = BooleanVar()
        self.show_Base_35.set(self.setSettingsValues("show_Base_35",
                                                    "boolean"))
        self.show_Base_36 = BooleanVar()
        self.show_Base_36.set(self.setSettingsValues("show_Base_36",
                                                    "boolean"))
    def updateSettings(self):
        with open("settings.txt", "w") as settings:
            settings.write("decimal_Mark = {0}\n".format("'" + self.decimal_Mark + "'"))
            settings.write("thousand_Mark = {0}\n".format("'" + self.thousand_Mark + "'"))
            settings.write("uppercase_hexadecimal = {0}\n".format(self.uppercase_hexadecimal.get()))
            settings.write("decimal_Separator = {0}\n".format(self.decimal_Separator.get()))

            settings.write("show_Relevant = {0}\n".format(self.show_Relevant.get()))
            settings.write("show_Prime = {0}\n".format(self.show_Prime.get()))
            settings.write("show_Roots = {0}\n".format(self.show_Roots.get()))
            settings.write("show_Binary = {0}\n".format(self.show_Binary.get()))
            settings.write("show_Hexadecimal = {0}\n".format(self.show_Hexadecimal.get()))
            settings.write("show_Factors = {0}\n".format(self.show_Factors.get()))
            settings.write("show_Palindromic = {0}\n".format(self.show_Palindromic.get()))
            settings.write("show_Fibonacci = {0}\n".format(self.show_Fibonacci.get()))
            settings.write("show_Factorial = {0}\n".format(self.show_Factorial.get()))

            settings.write("selected_Bases = {0}\n".format(self.selected_Bases))
            settings.write("show_All_Bases = {0}\n".format(self.show_All_Bases.get()))
            settings.write("show_Base_2 = {0}\n".format(self.show_Base_2.get()))
            settings.write("show_Base_3 = {0}\n".format(self.show_Base_3.get()))
            settings.write("show_Base_4 = {0}\n".format(self.show_Base_4.get()))
            settings.write("show_Base_5 = {0}\n".format(self.show_Base_5.get()))
            settings.write("show_Base_6 = {0}\n".format(self.show_Base_6.get()))
            settings.write("show_Base_7 = {0}\n".format(self.show_Base_7.get()))
            settings.write("show_Base_8 = {0}\n".format(self.show_Base_8.get()))
            settings.write("show_Base_9 = {0}\n".format(self.show_Base_9.get()))
            settings.write("show_Base_10 = {0}\n".format(self.show_Base_10.get()))
            settings.write("show_Base_11 = {0}\n".format(self.show_Base_11.get()))
            settings.write("show_Base_12 = {0}\n".format(self.show_Base_12.get()))
            settings.write("show_Base_13 = {0}\n".format(self.show_Base_13.get()))
            settings.write("show_Base_14 = {0}\n".format(self.show_Base_14.get()))
            settings.write("show_Base_15 = {0}\n".format(self.show_Base_15.get()))
            settings.write("show_Base_16 = {0}\n".format(self.show_Base_16.get()))
            settings.write("show_Base_17 = {0}\n".format(self.show_Base_17.get()))
            settings.write("show_Base_18 = {0}\n".format(self.show_Base_18.get()))
            settings.write("show_Base_19 = {0}\n".format(self.show_Base_19.get()))
            settings.write("show_Base_20 = {0}\n".format(self.show_Base_20.get()))
            settings.write("show_Base_21 = {0}\n".format(self.show_Base_21.get()))
            settings.write("show_Base_22 = {0}\n".format(self.show_Base_22.get()))
            settings.write("show_Base_23 = {0}\n".format(self.show_Base_23.get()))
            settings.write("show_Base_24 = {0}\n".format(self.show_Base_24.get()))
            settings.write("show_Base_25 = {0}\n".format(self.show_Base_25.get()))
            settings.write("show_Base_26 = {0}\n".format(self.show_Base_26.get()))
            settings.write("show_Base_27 = {0}\n".format(self.show_Base_27.get()))
            settings.write("show_Base_28 = {0}\n".format(self.show_Base_28.get()))
            settings.write("show_Base_29 = {0}\n".format(self.show_Base_29.get()))
            settings.write("show_Base_30 = {0}\n".format(self.show_Base_30.get()))
            settings.write("show_Base_31 = {0}\n".format(self.show_Base_31.get()))
            settings.write("show_Base_32 = {0}\n".format(self.show_Base_32.get()))
            settings.write("show_Base_33 = {0}\n".format(self.show_Base_33.get()))
            settings.write("show_Base_34 = {0}\n".format(self.show_Base_34.get()))
            settings.write("show_Base_35 = {0}\n".format(self.show_Base_35.get()))
            settings.write("show_Base_36 = {0}\n".format(self.show_Base_36.get()))
    def settingsWindow(self, parent):
        def goBack():
            self.updateSettings()
            self.settings_Window_Frame.grid_forget()
            self.cosmetic_Preferences_Frame.grid_forget()
            self.base_Settings_Frame.grid_forget()
            parent.main_Frame.grid(column=1, row=1)
        self.settings_Window_Frame = ttk.Frame(parent)
        self.settings_Window_Frame.grid(column=1, row=1)
        ttk.Button(self.settings_Window_Frame, text="<--", command=goBack, width=0)\
                    .grid(column=1, row=1, sticky=(NW))
        ttk.Button(self.settings_Window_Frame, text="Save",
                   command=self.updateSettings, width=0)\
                    .grid(column=2, row=1, sticky=(NW))

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
                                                    padding="0 15 0 0")
        self.cosmetic_Preferences_Frame.grid(column=1, row=7)

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

        self.base_Settings_Frame = ttk.Frame(parent, padding="15 0 0 0")
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
