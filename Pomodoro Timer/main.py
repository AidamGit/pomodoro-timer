from tkinter import *
from playsound import playsound

STATUS_COLOR = "#9bdeac"
BACKGROUND_COLOR = "#f7f5dd"
FONT = "Courier"
pomodoros_completed = 0


def start_program():

    # ---------------------------- BUTTON CLICKS ------------------------------- #


    def start_pause():
        if start_pause_button["text"] == "Start":
            start_pause_button["text"] = "Pause"
        else:
            start_pause_button["text"] = "Start"


    def restart():
        global pomodoros_completed
        pomodoros_completed = 0
        window.destroy()
        start_program()


    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def countdown(time_left):

        global pomodoros_completed
        minute = time_left//60
        second = time_left % 60
        time_left -= 1 if start_pause_button["text"] == "Pause" else False

        canvas.itemconfig(timer_display, text=f"{minute}:{second:02d}")

        if time_left > -2:
            window.after(1000, countdown, time_left)

        elif pomodoros_completed < 4:

            if status["text"] == "Work":

                status["text"] = "Rest"
                canvas.itemconfig(timer_display, text=f"10:00")

                pomodoro_status_list = list(pomodoro_status["text"])
                pomodoro_status_list[pomodoros_completed*2] = "☑"
                pomodoro_status["text"] = "".join(pomodoro_status_list)
                pomodoros_completed += 1
                window.update()

                if pomodoros_completed < 4:
                    playsound("sound.wav")
                    countdown(300)
                else:
                    status.place(x=100, y=-70)
                    status["text"] = "Finish"
                    canvas.itemconfig(timer_display, text=f"00:00")
                    window.update()
                    playsound("sound.wav")
                    return

            elif status["text"] == "Rest":
                status["text"] = "Work"
                canvas.itemconfig(timer_display, text=f"30:00")
                window.update()
                playsound("sound.wav")
                countdown(1800)


    # ---------------------------- UI SETUP ------------------------------- #

    # window/display
    window = Tk()
    window.title("Pomodoro Timer")
    window.minsize(height=500, width=600)
    window.config(padx=100, pady=150)
    window["bg"] = BACKGROUND_COLOR

    # image and timer display
    canvas = Canvas(height=224, width=200, bg=BACKGROUND_COLOR, highlightthickness=0)

    image = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=image)

    timer_display = canvas.create_text(102, 130, text="30:00", fill="white", font=(FONT, 25, "bold"))

    canvas.pack()

    # status
    status = Label(text="Work", font=(FONT, 40, "bold"), bg=BACKGROUND_COLOR, fg=STATUS_COLOR)
    status.place(x=130, y=-70)

    # buttons
    start_pause_button = Button(text="Start", font=("calibri", 10, "bold"), command=start_pause)
    start_pause_button.place(x=65, y=215)

    reset_button = Button(text="Restart", font=("calibri", 10, "bold"), command=restart)
    reset_button.place(x=290, y=213)

    # pomodoros completed
    pomodoro_status = Label(text="☐ ☐ ☐ ☐", font=(FONT, 15, "bold"), bg=BACKGROUND_COLOR, fg="green")
    pomodoro_status.place(x=135, y=230)

    countdown(1800)
    window.eval('tk::PlaceWindow . center')
    window.mainloop()

start_program()
