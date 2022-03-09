# Alarm clock with GUI

# import modules
import tkinter as tk
import datetime
import time
import winsound
import os

# main function
def Alarm(set_date, set_time):
    current_time = datetime.datetime.now()
    date = current_time.strftime("%Y-%m-%d")
    now = current_time.strftime("%H:%M:%S")

    if date <= set_date and now < set_time:
        print("The set date-time: ", set_date, set_time)
        print("Current date-time: ", date, now)
        window.after(1000, Alarm, set_date, set_time)
    else:
        lbl_msg = tk.Label(master=window, text="Wake up!", font=font_wakeup, bg=bg_main_3)
        lbl_msg.grid(row=3, column=0, columnspan=4, pady=10)
        window.update()
        current_path = os.path.dirname(__file__)
        sound_path = os.path.join(current_path, 'alarm.wav')
        winsound.PlaySound(sound_path, winsound.SND_FILENAME)
        print("Wake up!")
        time.sleep(5)
        winsound.PlaySound(None, winsound.SND_PURGE)
        window.destroy()

# trigger function
def Trigger():
    set_date = f"{yr.get()}-{mth.get()}-{day.get()}"
    set_time = f"{hr.get()}:{min.get()}:{sec.get()}"
    Alarm(set_date, set_time)

# stop sound function
def Stop():
    winsound.PlaySound(None, winsound.SND_FILENAME)
    window.destroy()
    print("Stop!")



# font
font_main_12 = ("Helvetica", 12)
font_main_10 = ("Helvetica", 10)
font_wakeup = ("Helvetica", 14, "bold")

# background
bg_main_1 = "#396EB0"
bg_main_2 = "#DADDFC"
bg_main_3 = "#FC997C"

# window
window = tk.Tk()
window.title("Alarm Clock")
window.geometry("330x180")
window.resizable(width=False, height=False)
window.config(bg=bg_main_1)

# label
lbl_date = tk.Label(master=window, text="Date", font=font_main_12, bg=bg_main_1)
lbl_time = tk.Label(master=window, text="Time", font=font_main_12, bg=bg_main_1)
lbl_date.grid(row=0, column=0, sticky="e", padx=18, pady=10)
lbl_time.grid(row=1, column=0, sticky="e", padx=18)


# variables
yr = tk.StringVar()
mth = tk.StringVar()
day = tk.StringVar()
hr = tk.StringVar()
min = tk.StringVar()
sec = tk.StringVar()


# default date and time
default_time = datetime.datetime.now()
yr.set(default_time.strftime("%Y"))
mth.set(default_time.strftime("%m"))
day.set(default_time.strftime("%d"))
hr.set(default_time.strftime("%H"))
min.set(default_time.strftime("%M"))
sec.set(default_time.strftime("%S"))

# entry
ent_yr = tk.Entry(master=window, textvariable=yr, width=10, font=font_main_10)
ent_mth = tk.Entry(master=window, textvariable=mth, width=10, font=font_main_10)
ent_day = tk.Entry(master=window, textvariable=day, width=10, font=font_main_10)
ent_hr = tk.Entry(master=window, textvariable=hr, width=10, font=font_main_10)
ent_min = tk.Entry(master=window, textvariable=min, width=10, font=font_main_10)
ent_sec = tk.Entry(master=window, textvariable=sec, width=10, font=font_main_10)
ent_yr.grid(row=0, column=1)
ent_mth.grid(row=0, column=2, padx=5)
ent_day.grid(row=0, column=3)
ent_hr.grid(row=1, column=1)
ent_min.grid(row=1, column=2, padx=5)
ent_sec.grid(row=1, column=3)

# button
btn_set_alarm = tk.Button(master=window, text="Set Alarm", command=Trigger, font=font_main_10, bg=bg_main_2)
btn_stop_alarm = tk.Button(master=window, text="Stop Alarm", command=Stop, font=font_main_10, bg=bg_main_2)
btn_set_alarm.grid(row=2, column=1, pady=10)
btn_stop_alarm.grid(row=2, column=2, pady=10)

window.mainloop()