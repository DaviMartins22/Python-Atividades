import tkinter as tk
from tkinter import ttk, messagebox

def verificar_cadeia():
    cadeia = entrada.get().strip()

    # Validação
    for c in cadeia:
        if c not in ['0', '1']:
            resultado.set("⚠ Cadeia inválida! Use apenas 0 e 1.")
            label_resultado.config(foreground="#ff4d4d")
            return

    estado = False

    # Processamento
    for simbolo in cadeia:
        if simbolo == '1':
            estado = True
        else:
            estado = False

    # Resultado final
    if estado:
        resultado.set("✔ Estado final: q1\nCadeia ACEITA")
        label_resultado.config(foreground="#00cc66")
    else:
        resultado.set("✖ Estado final: q0\nCadeia REJEITADA")
        label_resultado.config(foreground="#ff3333")


# ================= JANELA =================
janela = tk.Tk()
janela.title("🔍 Verificador de Cadeia")
janela.geometry("420x280")
janela.configure(bg="#1e1e2f")  # fundo escuro moderno
janela.resizable(False, False)

# ================= ESTILO =================
style = ttk.Style()
style.theme_use("default")

style.configure("TButton",
                font=("Segoe UI", 10, "bold"),
                padding=6)

# ================= TÍTULO =================
titulo = tk.Label(
    janela,
    text="Verificador de Cadeia",
    font=("Segoe UI", 18, "bold"),
    fg="#ffffff",
    bg="#1e1e2f"
)
titulo.pack(pady=(15, 5))

subtitulo = tk.Label(
    janela,
    text="Digite apenas 0 e 1",
    font=("Segoe UI", 10),
    fg="#bbbbbb",
    bg="#1e1e2f"
)
subtitulo.pack(pady=(0, 15))

# ================= INPUT =================
frame_input = tk.Frame(janela, bg="#1e1e2f")
frame_input.pack(pady=5)

entrada = tk.Entry(
    frame_input,
    font=("Consolas", 14),
    justify="center",
    bd=0,
    bg="#2a2a40",
    fg="#ffffff",
    insertbackground="white",
    width=20
)
entrada.pack(ipady=6, padx=10)

# ================= BOTÃO =================
botao = tk.Button(
    janela,
    text="Verificar Cadeia",
    command=verificar_cadeia,
    font=("Segoe UI", 11, "bold"),
    bg="#4da6ff",
    fg="white",
    activebackground="#3399ff",
    activeforeground="white",
    relief="flat",
    padx=10,
    pady=5
)
botao.pack(pady=15)

# ================= RESULTADO =================
resultado = tk.StringVar()

label_resultado = tk.Label(
    janela,
    textvariable=resultado,
    font=("Segoe UI", 12, "bold"),
    bg="#1e1e2f",
    wraplength=350,
    justify="center"
)
label_resultado.pack(pady=10)

# ================= RODAR =================
janela.mainloop()