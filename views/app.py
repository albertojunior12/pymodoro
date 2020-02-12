from tkinter import *
from time import strftime
from views.commons import Color

# funcs


def time():
    str_time = strftime('%M:%S %p')
    label_clock.config(text=str_time)
    label_clock.after(1000, time)


def format_time(minu, sec):
    str_minu = str(minu)
    str_sec = str(sec)
    if minu < 10:
        str_minu = '0{}'.format(str_minu)
    if sec < 10:
        str_sec = '0{}'.format(str_sec)
    return '{}:{}'.format(str_minu, str_sec)


minu = None
sec = None

def initial_state():
    global minu, sec
    minu, sec = None, None
    label_clock.config(text='00:00', fg=Color.success)


def tick():
    global minu
    global sec
    start_button.config(state=DISABLED)
    if sec == None and minu == None:
        minu = 0
        sec = 0
    if sec == 5:
        start_button.config(state=NORMAL)
        label_clock.config(text='Fim do Pomodoro', fg=Color.danger, font=('Arial', 40))
        label_clock.after(2000, initial_state)
    else:
        sec += 1
        if sec == 60:
            minu += 1
            sec = 0
        label_clock.config(text=format_time(minu, sec))
        label_clock.after(1000, tick)


window = Tk()

# window styles
window.title('Pymodoro')
window['bg'] = Color.light
window.resizable(False, False)
window.geometry('700x450+100+100')

# clock container
clock_container = Frame(window, width=500, height=450, background=Color.dark)
clock_container.pack(side=LEFT)
clock_container.pack_propagate(FALSE)

label_clock = Label(
    clock_container,
    text='00:00',
    bg=Color.dark,
    fg=Color.success,
    font=('Arial', 40),
    anchor=CENTER
)

label_clock.pack(side=TOP, padx=10, pady=10)

log_container = Frame(window, width=200, height=450, background=Color.light)
log_container.pack(side=RIGHT)
log_container.pack_propagate(FALSE)

# controls container
controls_container = Frame(clock_container, width=500, height=100, background=Color.dark)
controls_container.pack(side=BOTTOM)
controls_container.pack_propagate(FALSE)

# start button
start_button = Button(
    controls_container,
    width=20,
    height=2,
    bg=Color.warning,
    fg=Color.dark,
    text='Iniciar',
    font=('Arial', 10),
    command=tick,
)
start_button.pack(side=LEFT, padx=10, pady=20)

# pause button
pause_button = Button(
    controls_container,
    width=20,
    height=2,
    bg=Color.primary,
    fg=Color.dark,
    text='Pausar',
    font=('Arial', 10),
)

pause_button.pack(side=RIGHT, padx=10, pady=20)

window.mainloop()
