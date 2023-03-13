import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#FFE2E2"
WHITE = "#FFFFFF" #warna latar belakang tombol digit
LIGHT_BLUE = "#FFE2E2" #code warna btn sama dengan 
LIGHT_GRAY = "#FFFFFF"
LABEL_COLOR = "#DB7093"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667") #menentukan lebar dan tinggi frame kalkulator
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = "" # menyimpan ekspresi saat ini yang sedang ditampilkan pada layar kalkulator.
        self.display_frame = self.create_display_frame() #untuk menampilkan layar kalkulator.

        self.total_label, self.label = self.create_display_labels()

        self.digits = { #memetakan angka-angka ke posisi baris dan kolom pada grid layar kalkulator.
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} #memetakan operator matematika ke simbol yang akan ditampilkan pada tombol operator.
        self.buttons_frame = self.create_buttons_frame() #pemanggilan dari code def create_digit_buttons(self):untuk menampilkan tombol-tombol digit di kalkulator.

        self.buttons_frame.rowconfigure(0, weight=1) # kode yang mengatur konfigurasi baris pertama dari frame tombol
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons() #fungsi yang digunakan untuk membuat tombol-tombol angka pada kalkulator.
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()# untuk mengikat tombol-tombol pada keyboard dengan fungsi-fungsi yang sesuai pada kalkulator.

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate()) #untuk menghitung hasil dari ekspresi aritmatika yang telah dimasukkan 
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self): #function ini akan digunakan untuk membuat beberapa tombol khusus
        self.create_clear_button() #membuat tombol "Clear"
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_backspace_button() # membuat tombol "Backspace" 
    #label
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                            fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both') # kode untuk membuat label untuk menampilkan hasil total ekspresi aritmatika yang telah dimasukkan 

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                        fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    #bingkai untuk tampilan
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    #membuat tombol digit angkanya, setiap digit dan nilai grid akan di buat tombol
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                            borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW) #menempatkan tombol" dalam kotak agar menempel di setiap sisi. 

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
        
    #membuat tombol operator
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                        borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                        borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                        borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # fungsi backspace
    def backspace(self):
        if len(self.current_expression) > 0:
            self.current_expression = self.current_expression[:-1]
            self.update_label()

    def create_backspace_button(self):
        button = tk.Button(self.buttons_frame, text="\u232B", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                        borderwidth=0, command=self.backspace)
        button.grid(row=0, column=3, sticky=tk.NSEW)
# ---------------------

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                        borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()