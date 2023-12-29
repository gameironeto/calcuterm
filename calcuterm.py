from tkinter import Tk, ttk, Toplevel, messagebox
import sup_data

main_window = Tk()
main_window.title('calcuterm')
main_window.geometry('820x530')

m_frame = ttk.Frame(main_window)
m_frame.pack()

frame_top_1 = ttk.Frame(m_frame, width=820, height=72)
frame_top_1.pack(side='top')

title_1 = ttk.Label(
    frame_top_1,
    text='CALCULADORA DE CARGA TÉRMICA',
    font=('Arial', 20),
    justify='center'
)
title_1.pack()

frame_middle_title = ttk.Frame(m_frame)
frame_middle_title.pack()

frame_middle_title1 = ttk.Frame(frame_middle_title, width=410, height=78)
frame_middle_title1.grid(column=0, row=0, padx=200)

lb_room = ttk.Label(
    frame_middle_title1,
    text='Cômodo',
    justify='center'
)
lb_room.pack()

frame_middle_title2 = ttk.Frame(frame_middle_title, width=410, height=78)
frame_middle_title2.grid(column=1, row=0, padx=100)

lb_partition = ttk.Label(
    frame_middle_title2,
    text='Divisória'
)
lb_partition.grid(column=0, row=0)

partition_add = ttk.Button(
    frame_middle_title2,
    text='+',
    command=lambda: second_window()
)
partition_add.grid(column=1, row=0)

frame_middle = ttk.Frame(m_frame)
frame_middle.pack()

frame_middle_left = ttk.Frame(frame_middle, width=410, height=234)
frame_middle_left.grid(column=0, row=1)

lb_area = ttk.Label(
    frame_middle_left,
    text='Área (m²)'
)
lb_area.grid(column=0, row=0)

area_input = ttk.Entry(frame_middle_left)
area_input.grid(column=1, row=0)

lb_ppl = ttk.Label(
    frame_middle_left,
    text='Pessoas no recinto (qtd.)',
)
lb_ppl.grid(column=0, row=1)

ppl_input = ttk.Entry(frame_middle_left)
ppl_input.grid(column=1, row=1)

lb_ppltp = ttk.Label(
    frame_middle_left,
    text='Atividade das pessoas'
)
lb_ppltp.grid(column=0, row=2)

pplvl = list(sup_data.dict_ppl_u.keys())

ppltp_cbbx = ttk.Combobox(
    frame_middle_left,
    values=pplvl
)
ppltp_cbbx.grid(column=1, row=2)

lb_equip = ttk.Label(
    frame_middle_left, 
    text='Luzes e Equipamentos (W)'
)
lb_equip.grid(column=0, row=3)

equip_input = ttk.Entry(frame_middle_left)
equip_input.grid(column=1, row=3)

def ppl_eq():
    q = int(ppl_input.get())
    t = ppltp_cbbx.get()
    tv = float(sup_data.dict_ppl_u.get(t))
    Q = q * tv
    return Q

def eqp_eq():
    q = float(equip_input.get())
    Q = round(q * 3.41, 2)
    return Q
    
def button_calculate():
    x = eqp_eq()
    y = ppl_eq()
    Q = x + y
    j = round(sum(ptt_ls) + Q, 2)
    l = 'Carga Total = ' + str(j) + ' BTU/h'
    frame_bottom2 = ttk.Frame(m_frame)
    frame_bottom2.pack(side='bottom')
    calculable = ttk.Label(
        frame_bottom2,
        text=l
    )
    calculable.pack()

frame_middle_right = ttk.Frame(frame_middle, width=410, height=234)
frame_middle_right.grid(column=1, row=1)

ptt_ls = []

def new_button_cmd():
    n_bttn.destroy()
    ptt_ls.pop()
    second_window()

def new_button():
    global n_bttn
    n_bttn = ttk.Button(
        frame_middle_right,
        text=name_input.get(),
        command=lambda: new_button_cmd()
        )
    n_bttn.pack()


frame_bottom1 = ttk.Frame(m_frame)
frame_bottom1.pack(side='bottom')

calculate_bt = ttk.Button(
    frame_bottom1,
    text='CALCULAR',
    command=lambda: button_calculate()
)
calculate_bt.pack()





#############################################################################################################
#############################################################################################################
####       SECOND WINDOW (UNFORTUNATELLY I COUDN'T PUT THE SECOND WINDOW IN ANOTHER .PY ARCHIVE)         ####
#############################################################################################################
#############################################################################################################




def second_window():
    scnd_window = Toplevel(main_window)
    scnd_window.title('Nova Divisória')
    
    main_frame = ttk.Frame(scnd_window)
    main_frame.pack()

    top_frame = ttk.Frame(main_frame)
    top_frame.pack(side='top')

    title_lbl = ttk.Label(
        top_frame,
        text='Nova Divisória'
    )
    title_lbl.pack()

    mid_frame = ttk.Frame(main_frame)
    mid_frame.pack()

    pttype_label = ttk.Label(
        mid_frame,
        text='Tipo'
    )
    pttype_label.grid(column=0, row=0)

    type_selection = ttk.Combobox(
        mid_frame,
        values=sup_data.list_partition
    )
    type_selection.grid(column=1, row=0)

    material_label = ttk.Label(
        mid_frame,
        text='Material da Divisória'
    )
    material_label.grid(column=0, row=1)
    
    dict_ext_list = list(sup_data.dict_uext_partition.keys())

    material_selection = ttk.Combobox(
        mid_frame,
        values=dict_ext_list
    )
    material_selection.grid(column=1, row=1)

    name_label = ttk.Label(
        mid_frame,
        text='Nome da Divisória'
    )
    name_label.grid(column=0, row=2)

    global name_input
    name_input = ttk.Entry(mid_frame)
    name_input.grid(column=1, row=2)

    area_label = ttk.Label(
        mid_frame,
        text='Área da Divisória (m²)'
    )
    area_label.grid(column=0, row=3)

    area_input = ttk.Entry(mid_frame)
    area_input.grid(column=1, row=3)

    orientation_label = ttk.Label(
        mid_frame,
        text='Orientação Geográfica'
    )
    orientation_label.grid(column=0, row=4)

    orientation_list = list(sup_data.dict_orientation.keys())

    orientation_cbbx = ttk.Combobox(
        mid_frame,
        values=orientation_list
    )
    orientation_cbbx.grid(column=1, row=4)

    bottom_frame = ttk.Frame(main_frame)
    bottom_frame.pack(side='bottom')

    def conduction():
        x = material_selection.get()
        U = float(sup_data.dict_uext_partition.get(x))
        A = float(area_input.get())
        if type_selection.get() == sup_data.list_partition[0]:
            D = 9.4
        elif type_selection.get() == sup_data.list_partition[1]:
            D = 5.5
        else:
            messagebox.showinfo(message='Preencha todos os campos!')
        Q = round(U * A * D * 3.96567, 2)
        return Q

    def insolation_reflect():
        lista = ['janelas de vidros comuns (simples)', 'janelas de vidros duplos', 'janelas de vidros triplos']
        if material_selection.get() in lista:
            x = orientation_cbbx.get()
            q = int(sup_data.dict_orientation.get(x))
            Q = round(q * 3.96567, 2)
        else:
            Q = 0
        return Q

    def insolation_absorb():
        x = material_selection.get()
        U = float(sup_data.dict_uext_partition.get(x))
        A = float(area_input.get())
        if type_selection.get() == sup_data.list_partition[0]:
            dt = 9.4
        elif type_selection.get() == sup_data.list_partition[1]:
            dt = 5.5
        else:
            messagebox.showinfo(message='Preencha todos os campos!')
        y = orientation_cbbx.get()
        lista_1 = ['E', 'NE', 'SE', 'O', 'SO', 'NO']
        if y in lista_1:
            dt_ins = 11.1
        elif y == 'N':
            dt_ins = 5.5
        else:
            dt_ins = 0
        Q = round(A * U * (dt + dt_ins) * 3.96567, 2)
        return Q

    def button_action():
        global o
        x = conduction()
        y = insolation_reflect()
        z = insolation_absorb()
        o = round(x + y + z, 2)
        ptt_ls.append(o)
        new_button()
        scnd_window.destroy()

    wd_destroyer_bttn = ttk.Button(
        bottom_frame,
        text='CONFIRMAR',
        command=lambda: button_action()
    )
    wd_destroyer_bttn.pack()

    scnd_window.mainloop()
    
lambda: new_button()
main_window.mainloop()