import tkinter as tk
from tkinter import messagebox
from db import create_connection, create_table
from missoes import Missao
from tkcalendar import DateEntry

def add_missao():
    def save_missao():

        missao = Missao(
            None,
            entry_name.get(),
            entry_date.get(),
            entry_destination.get(),
            entry_state.get(),
            entry_crew.get(),
            entry_payload.get(),
            entry_duration.get(),
            float(entry_cost.get()),
            entry_status.get()
        )
        Missao.criar_missao(conn, missao)
        messagebox.showinfo("Sucesso", "Missão adicionada com sucesso.")
        add_window.destroy()
        update_missao_lista()
    
    add_window = tk.Toplevel(root)
    add_window.title("Adicionar Missão")

    tk.Label(add_window, text="Nome:").grid(row=0, column=0)
    entry_name = tk.Entry(add_window)
    entry_name.grid(row=0, column=1)

    tk.Label(add_window, text="Data de Lançamento:").grid(row=1, column=0)
    entry_date = tk.Entry(add_window)
    entry_date.grid(row=1, column=1)

    tk.Label(add_window, text="Destino:").grid(row=2, column=0)
    entry_destination = tk.Entry(add_window)
    entry_destination.grid(row=2, column=1)

    tk.Label(add_window, text="Estado:").grid(row=3, column=0)
    entry_state = tk.Entry(add_window)
    entry_state.grid(row=3, column=1)

    tk.Label(add_window, text="Tripulação:").grid(row=4, column=0)
    entry_crew = tk.Entry(add_window)
    entry_crew.grid(row=4, column=1)

    tk.Label(add_window, text="Carga Útil:").grid(row=5, column=0)
    entry_payload = tk.Entry(add_window)
    entry_payload.grid(row=5, column=1)

    tk.Label(add_window, text="Duração:").grid(row=6, column=0)
    entry_duration = tk.Entry(add_window)
    entry_duration.grid(row=6, column=1)

    tk.Label(add_window, text="Custo:").grid(row=7, column=0)
    entry_cost = tk.Entry(add_window)
    entry_cost.grid(row=7, column=1)

    tk.Label(add_window, text="Status:").grid(row=8, column=0)
    entry_status = tk.Entry(add_window)
    entry_status.grid(row=8, column=1)

    tk.Button(add_window, text="Salvar", command=save_missao).grid(row=9, column=0, columnspan=2)

def atualizar_missao():
    selected_mission = missao_list.get(missao_list.curselection())
    missao_id = int(selected_mission.split(' ')[0])
    mission = Missao.get_missao_by_id(conn, missao_id)
    
    def salvar_atualizacoes():
        missao_atualizada = Missao(
            missao_id,
            entry_name.get(),
            entry_date.get(),
            entry_destination.get(),
            entry_state.get(),
            entry_crew.get(),
            entry_payload.get(),
            entry_duration.get(),
            float(entry_cost.get()),
            entry_status.get()
        )
        Missao.atualizar_missao(conn, missao_atualizada)
        messagebox.showinfo("Sucesso", "Missão atualizada com sucesso!")
        update_window.destroy()
        update_missao_lista()
    
    update_window = tk.Toplevel(root)
    update_window.title("Atualizar Missão")

    labels = ["Nome:", "Data de Lançamento:", "Destino:", "Estado:", "Tripulação:", "Carga Útil:", "Duração:", "Custo:", "Status:"]
    entries = []

    for i, (label, value) in enumerate(zip(labels, mission[1:])):
        tk.Label(update_window, text=label).grid(row=i, column=0)
        entry = tk.Entry(update_window)
        entry.grid(row=i, column=1)
        entry.insert(0, value)
        entries.append(entry)

    entry_name, entry_date, entry_destination, entry_state, entry_crew, entry_payload, entry_duration, entry_cost, entry_status = entries

    tk.Button(update_window, text="Salvar", command=salvar_atualizacoes).grid(row=9, column=0, columnspan=2)

def pesquisar_missao_por_data():
    def perform_search():
        data_de_inicio = entry_data_de_inicio.get()
        data_do_fim = entry_data_do_fim.get()
        missoes = Missao.pesquisar_missao_por_data(conn, data_de_inicio, data_do_fim)
        missao_list.delete(0, tk.END)
        for missao in missoes:
            missao_list.insert(tk.END, f"{missao[0]} - {missao[1]} - {missao[2]}")
        search_window.destroy()
    
    search_window = tk.Toplevel(root)
    search_window.title("Pesquisar Missões por Intervalo de Datas")

    tk.Label(search_window, text="Data Inicial:").grid(row=0, column=0)
    entry_data_de_inicio = DateEntry(search_window, date_pattern='dd-mm-yyyy')
    entry_data_de_inicio.grid(row=0, column=1)

    tk.Label(search_window, text="Data Final:").grid(row=1, column=0)
    entry_data_do_fim = DateEntry(search_window, date_pattern='dd-mm-yyyy')
    entry_data_do_fim.grid(row=1, column=1)

    tk.Button(search_window, text="Pesquisar", command=perform_search).grid(row=2, column=0, columnspan=2)
    

def update_missao_lista():
    missoes = Missao.ler_missao(conn)
    missao_list.delete(0, tk.END)
    for missao in missoes:
        missao_list.insert(tk.END, f"{missao[0]} - {missao[1]} - {missao[2]}")

def view_missao_details():
    selected_mission = missao_list.get(missao_list.curselection())
    missao_id = int(selected_mission.split(' ')[0])
    missao = Missao.get_missao_by_id(conn, missao_id)
    details = f"ID: {missao[0]}\nNome: {missao[1]}\nData de Lançamento: {missao[2]}\nDestino: {missao[3]}\nEstado: {missao[4]}\nTripulação: {missao[5]}\nCarga Útil: {missao[6]}\nDuração: {missao[7]}\nCusto: {missao[8]}\nStatus: {missao[9]}"
    messagebox.showinfo("Detalhes da Missão", details)

def delete_missao():
    selected_missao = missao_list.get(missao_list.curselection())
    missao_id = int(selected_missao.split(' ')[0])
    Missao.delete_missao(conn, missao_id)
    messagebox.showinfo("Sucesso", "Missão excluída com sucesso.")
    update_missao_lista()

def trocar_tema():
    global modo_escuro
    modo_escuro = not modo_escuro
    liga_modo_escuro(root)

#Modo escuro:
modo_escuro = False

def liga_modo_escuro(window):
    bg_color = "#333" if modo_escuro else "#fff"
    fg_color = "#fff" if modo_escuro else "#000"
    btn_bg_color = "#555" if modo_escuro else "#f0f0f0"

    window.configure(bg=bg_color)
    for widget in window.winfo_children():
        if isinstance(widget, tk.Toplevel):
            liga_modo_escuro(widget)
        else:
            widget.configure(bg=bg_color, fg=fg_color)
            if isinstance(widget, tk.Button):
                widget.configure(bg=btn_bg_color)



root = tk.Tk()
root.title("Sistema de Gerenciamento de Expedição Espacial")
root.iconbitmap('foguete.ico')

conn = create_connection()
create_table(conn)

missao_list = tk.Listbox(root, width=100, height=20)
missao_list.pack()

tk.Button(root, text="Adicionar Missão", command=add_missao).pack()
tk.Button(root, text="Atualizar Missão", command=atualizar_missao).pack()
tk.Button(root, text="Visualizar Detalhes", command=view_missao_details).pack()
tk.Button(root, text="Excluir Missão", command=delete_missao).pack()
tk.Button(root, text="Pesquisar Missões por Data", command=pesquisar_missao_por_data).pack()
tk.Button(root, text="Modo Escuro", command=trocar_tema).pack()

update_missao_lista()

liga_modo_escuro(root)

root.mainloop()