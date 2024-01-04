import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook, Workbook 
from openpyxl.utils import get_column_letter 
from datetime import date, datetime, timedelta 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import calendar 


# funcao salvar valor
def salvar_valor():
    valor_dia = float(entry_valor.get())
    valores.append(valor_dia)
    total_valores = sum(valores)
    entry_valor.delete(0, tk.END)

    label_status.config(text="Valor salvo com Sucesso!", foreground="green")
    label_total.config(text=f"Total economizado: R${total_valores:.2f}")

    # Adicionando valor em uma nova linha na planilha
    linha = len(valores) + 1
    coluna_data = get_column_letter(1)
    coluna_valor = get_column_letter(2)
    sheet.cell(row=linha, column=1, value=date.today().strftime("%d-%m-%y"))
    sheet.cell(row=linha, column=2, value=valor_dia)


janela = tk.Tk()
janela.title("Aplicatico de Poupança")
janela.geometry("700x500")
janela.configure(bg="#252525")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#252525", foreground="#FFFFFF", font=("Arial", 12))
style.configure("TEntry", fieldbackground="#FFFFFF", font=("Arial", 12))
style.configure("TButton", background="#4CAF50", foreground="#FFFFFF", font=("Arial", 12))

label_instrucao = ttk.Label(janela, text="Insira o valor diario")
label_status = ttk.Label(janela, text="", foreground="red")
label_total = ttk.Label(janela, text="100", font=("Arial", 14, "bold"))
entry_valor = ttk.Entry(janela)
button_salvar = ttk.Button(janela, text="Salvar", command=salvar_valor)



#Posicionando os elementos

label_instrucao.pack(pady=5)
entry_valor.pack(pady=5)
button_salvar.pack(pady=10)
label_status.pack()
label_total.pack(pady=10)


# Carregamento da planilha existente ou  criacao de uma nova
try:
    Workbook = load_workbook("valores_diarios.xlsx")
except FileNotFoundError:
    Workbook = Workbook()

# Selecionando a primeira planilha
sheet = Workbook.active

# Verificando se a planilha ja posssui valores salvos
if sheet.max_row == 0:
    sheet.cell(row=1, column=1, value="Data")
    sheet.cell(row=1, column=2, value="Valor diário")

# Obter a lista de valores ja salvo
    
valores = [cell.value for cell in sheet['B'][1:]]

# Exibe o total economizado 
label_total.config(text=f'Total economizado R${sum(valores):.2f}')




janela.mainloop()

# Salve a planilha com os valores atualizados
Workbook.save("valores_diarios.xlsx")