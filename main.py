from tkinter import *

root = Tk()
root['bg'] = "black"
root.geometry('315x280+800+400')
root.title("Calculator")
root.resizable(False, False)


def add_digit(digit):
    value = get_num.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    get_num.delete(0, END)
    get_num.insert(0, value + digit)


def add_operation(operation):
    value = get_num.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        get_result()
        value = get_num.get()
    get_num.delete(0, END)
    get_num.insert(END, value + operation)


def get_result():
    value = get_num.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    get_num.delete(0, END)
    try:
        get_num.insert(END, eval(value))
    except NameError:
        pass


def clear():
    get_num.delete(0, END)
    get_num.insert(0, '0')


def make_digit_button(digit):
    return Button(root, text=digit, font=("Arial", 20), fg='blue', bd=5,
                  command=lambda: add_digit(digit), padx=10, pady=5)


def make_operation_button(operation):
    return Button(root, text=operation, font=("Arial", 20), fg='red', bd=5,
                  command=lambda: add_operation(operation), padx=10, pady=5)


def delete(text):
    return Button(root, text=text, font=("Arial", 20), bd=5,
                  command=clear, padx=10, pady=5)


def make_equal_button(equal):
    return Button(root, text=equal, font=("Arial", 20), fg='red', bd=5,
                  command=lambda: get_result(), padx=10, pady=5)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        get_result()


root.bind('<Key>', press_key)

get_num = Entry(root, justify=RIGHT, font=("Arial", 20))
get_num.insert(0, '0')
get_num.grid(row=0, columnspan=5, stick='wens', pady=2, padx=2)


make_digit_button('7').grid(row=1, column=0, stick='wens', pady=2, padx=2)
make_digit_button('8').grid(row=1, column=1, stick='wens', pady=2, padx=2)
make_digit_button('9').grid(row=1, column=2, stick='wens', pady=2, padx=2)
make_digit_button('4').grid(row=2, column=0, stick='wens', pady=1, padx=2)
make_digit_button('5').grid(row=2, column=1, stick='wens', pady=2, padx=2)
make_digit_button('6').grid(row=2, column=2, stick='wens', pady=2, padx=2)
make_digit_button('1').grid(row=3, column=0, stick='wens', pady=2, padx=2)
make_digit_button('2').grid(row=3, column=1, stick='wens', pady=2, padx=2)
make_digit_button('3').grid(row=3, column=2, stick='wens', pady=2, padx=2)
make_digit_button('0').grid(row=4, columnspan=3, stick='wens', padx=2, pady=2)

make_operation_button('+').grid(row=4, column=3, stick='wens', padx=2, pady=2)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=2, pady=2)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=2, pady=2)
make_operation_button('/').grid(row=1, column=3, stick='wens', padx=2, pady=2)

delete('del').grid(row=1, column=4, stick='wens', padx=2, pady=2)

make_equal_button('=').grid(row=2, column=4, rowspan=3, stick='wens', padx=2, pady=2)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)

root.mainloop()
