from tkinter import Tk, ttk, Toplevel, mainloop
from cs50 import SQL


######################################################
# CHANGE WINDOW FUNCTION
def second_page():
    
    second_window = ttk.Frame(main_frame)
    second_window.pack()
    
    frame_top_1 = ttk.Frame(second_window)
    frame_top_1.pack(side='top')
    title_1 = ttk.Label(
        frame_top_1,
        text='THERMAL LOAD CALCULATOR',
        font=('Arial', 20)
    )
    title_1.pack(
        padx=201,
        pady=46
    )
    
    frame_middle_1 = ttk.Frame(second_window)
    frame_middle_1.pack()
    lb_room = ttk.Label(
        frame_middle_1,
        text='Room'
    )
    lb_room.pack()
    
    frame_middle_2 = ttk.Frame(second_window)
    frame_middle_2.pack()
    lb_area = ttk.Label(
        frame_middle_2,
        text='Area (m²)'
    )
    lb_area.grid(column=0, row=0)
    area_input = ttk.Entry(frame_middle_2)
    area_input.grid(column=1, row=0)
    lb_height = ttk.Label(
        frame_middle_2,
        text='Ceiling height (m)'
    )
    lb_height.grid(column=0, row=1)
    height_input = ttk.Entry(frame_middle_2)
    height_input.grid(column=1, row=1)
    
    
    
    
    


def combobox_selector():
    sl = br_state_cb.get()
    print(sl)
    
#######################################################
# BUTTON PAGE 1
def button_action(page):
    combobox_selector()
    first_window.destroy()
    page()
    
    
######################################################
# OPENING WINDOW
window = Tk()
window.geometry("820x530")

main_frame = ttk.Frame(window)
main_frame.pack()

first_window = ttk.Frame(main_frame)
first_window.pack()

######################################################
# SET TOP APP FRAME
frame_top = ttk.Frame(first_window)
frame_top.pack(side='top')

title = ttk.Label(
    frame_top,
    text='THERMAL LOAD CALCULATOR',
    font=('Arial', 20)
)
title.pack(
    padx=201,
    pady=46
)

####################################################
# SET MIDDLE APP FRAME
frame_middle = ttk.Frame(first_window)
frame_middle.pack()

db_cities = SQL("sqlite:///cities.db")
city_st = db_cities.execute("SELECT cidades FROM cities")

br_state_lb = ttk.Label(
    frame_middle,
    text='City(State)',
    font=('Arial', 16)
)
br_state_lb.grid(
    column=0,
    row=0
)

br_state_cb = ttk.Combobox(
    frame_middle,
    values=city_st
)
br_state_cb.grid(
    column=1,
    row=0
)

##########################################
# SET BOTTOM APP FRAME
frame_bottom = ttk.Frame(first_window)
frame_bottom.pack()

######################################################
# OPEN PRINCIPAL WINDOW FUNCTION
start_bt = ttk.Button(
    frame_bottom,
    text='Start',
    command=lambda: button_action(second_page)
)
start_bt.pack()

mainloop()
