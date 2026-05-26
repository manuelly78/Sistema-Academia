import tkinter as tk
from tkinter import messagebox
try:
    from PIL import Image, ImageTk
except Exception:
    Image = None
    ImageTk = None
import os

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Academia - Sistema de Login")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        # Centralizar janela na tela
        self.center_window()
        
        # Cores
        self.cor_primaria = "#1e3a8a"
        self.cor_secundaria = "#3b82f6"
        self.cor_texto = "#ffffff"
        self.cor_fundo = "#f3f4f6"
        
        # Criar interface
        self.create_ui()
        
    def center_window(self):
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 900
        window_height = 600
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def create_ui(self):
        # Frame principal com dois lados
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Lado esquerdo - Logo e textos
        left_frame = tk.Frame(main_frame, bg=self.cor_primaria)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Adicionar logo
        self.add_logo(left_frame)
        
        # Lado direito - Formulário
        right_frame = tk.Frame(main_frame, bg=self.cor_fundo)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Adicionar formulário
        self.add_form(right_frame)
    
    def add_logo(self, parent):
        # Frame para centralizar o conteúdo no meio
        content_frame = tk.Frame(parent, bg=self.cor_primaria)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame interno para os elementos
        inner_frame = tk.Frame(content_frame, bg=self.cor_primaria)
        inner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Logo padrão em texto
        logo_label = tk.Label(
            inner_frame,
            text="💪",
            font=("Arial", 80),
            bg=self.cor_primaria
        )
        logo_label.pack(pady=(0, 10))
        
        # Texto descritivo
        title_label = tk.Label(
            inner_frame,
            text="ACADEMIA",
            font=("Arial", 28, "bold"),
            fg=self.cor_texto,
            bg=self.cor_primaria
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            inner_frame,
            text="Sistema de Gestão",
            font=("Arial", 14),
            fg="#bfdbfe",
            bg=self.cor_primaria
        )
        subtitle_label.pack()
    
    def add_form(self, parent):
        # Título do formulário
        form_title = tk.Label(
            parent,
            text="Faça Login",
            font=("Arial", 24, "bold"),
            fg=self.cor_primaria,
            bg=self.cor_fundo
        )
        form_title.pack(pady=30)
        
        # Frame para inputs
        input_frame = tk.Frame(parent, bg=self.cor_fundo)
        input_frame.pack(padx=40, pady=10)
        
        # Label e input de email
        email_label = tk.Label(
            input_frame,
            text="Email:",
            font=("Arial", 11),
            fg=self.cor_primaria,
            bg=self.cor_fundo
        )
        email_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.email_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=30,
            relief=tk.FLAT,
            bd=2
        )
        self.email_entry.pack(ipady=8, pady=(0, 20))
        self.email_entry.config(bg="#ffffff", fg="#000000")
        
        # Label e input de senha
        password_label = tk.Label(
            input_frame,
            text="Senha:",
            font=("Arial", 11),
            fg=self.cor_primaria,
            bg=self.cor_fundo
        )
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.password_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=30,
            show="●",
            relief=tk.FLAT,
            bd=2
        )
        self.password_entry.pack(ipady=8, pady=(0, 10))
        self.password_entry.config(bg="#ffffff", fg="#000000")
        
        # Checkbox "Lembrar de mim"
        self.remember_var = tk.BooleanVar()
        remember_check = tk.Checkbutton(
            input_frame,
            text="Lembrar de mim",
            variable=self.remember_var,
            font=("Arial", 10),
            bg=self.cor_fundo,
            fg=self.cor_primaria,
            activebackground=self.cor_fundo,
            activeforeground=self.cor_primaria
        )
        remember_check.pack(anchor=tk.W, pady=(0, 20))
        
        # Botão Login
        login_button = tk.Button(
            input_frame,
            text="ENTRAR",
            font=("Arial", 12, "bold"),
            bg=self.cor_secundaria,
            fg=self.cor_texto,
            width=30,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.login
        )
        login_button.pack(ipady=10, pady=10)
        
        # Botão Cadastro
        register_button = tk.Button(
            input_frame,
            text="CRIAR CONTA",
            font=("Arial", 11),           
            bg=self.cor_fundo,
            fg=self.cor_secundaria,
            width=30,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.register
        )
        register_button.pack(ipady=10)
        
        # Link esqueci senha
        forgot_button = tk.Label(
            input_frame,
            text="Esqueci minha senha",
            font=("Arial", 9),
            fg=self.cor_secundaria,
            bg=self.cor_fundo,
            cursor="hand2"
        )
        forgot_button.pack(pady=15)
        forgot_button.bind("<Button-1>", lambda _: self.forgot_password())
    
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        # Validações simples
        if not email or not password:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
        
        if "@" not in email:
            messagebox.showerror("Erro", "Email inválido!")
            return
        
        # Aqui você conectaria com seu banco de dados
        # Exemplo de validação básica
        if email == "admin@academia.com" and password == "123456":
            messagebox.showinfo("Sucesso", f"Bem-vindo, {email}!")
            # Aqui você abriria a tela principal do sistema
            print("Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")
            self.password_entry.delete(0, tk.END)
    
    def register(self):
        # Abrir janela de cadastro
        register_window = tk.Toplevel(self.root)
        RegisterScreen(register_window)
    
    def forgot_password(self):
        messagebox.showinfo("Recuperar Senha", "Abrir tela de recuperação de senha")
        # Aqui você abriria a janela de recuperação


class RegisterScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro - Sistema Academia")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.center_window()
        
        # Cores
        self.cor_primaria = "#1e3a8a"
        self.cor_secundaria = "#3b82f6"
        self.cor_texto = "#ffffff"
        self.cor_fundo = "#f3f4f6"
        
        self.create_ui()
    
    def center_window(self):
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600
        window_height = 800
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def create_ui(self):
        # Frame principal com scroll
        main_frame = tk.Frame(self.root, bg=self.cor_fundo)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="Criar Sua Conta",
            font=("Arial", 24, "bold"),
            fg=self.cor_primaria,
            bg=self.cor_fundo
        )
        title_label.pack(pady=(0, 20))
        
        # Frame para os campos
        fields_frame = tk.Frame(main_frame, bg=self.cor_fundo)
        fields_frame.pack(fill=tk.BOTH, expand=True)
        
        # Campo Nome
        self.add_field(fields_frame, "Nome Completo:", 0)
        self.nome_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Campo Idade
        self.add_field(fields_frame, "Idade:", 1)
        self.idade_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.idade_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Campo CPF
        self.add_field(fields_frame, "CPF:", 2)
        self.cpf_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.cpf_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Campo Email
        self.add_field(fields_frame, "Email:", 3)
        self.email_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)
        
        # Campo Senha
        self.add_field(fields_frame, "Senha:", 4)
        self.senha_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40, show="●")
        self.senha_entry.grid(row=4, column=1, padx=10, pady=10)
        
        # Campo Confirmar Senha
        self.add_field(fields_frame, "Confirmar Senha:", 5)
        self.confirmar_senha_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40, show="●")
        self.confirmar_senha_entry.grid(row=5, column=1, padx=10, pady=10)
        
        # Campo Local de Moradia
        self.add_field(fields_frame, "Local de Moradia:", 6)
        self.local_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.local_entry.grid(row=6, column=1, padx=10, pady=10)
        
        # Campo Telefone
        self.add_field(fields_frame, "Telefone:", 7)
        self.telefone_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.telefone_entry.grid(row=7, column=1, padx=10, pady=10)
        
        # Campo Cidade
        self.add_field(fields_frame, "Cidade:", 8)
        self.cidade_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.cidade_entry.grid(row=8, column=1, padx=10, pady=10)
        
        # Campo Estado
        self.add_field(fields_frame, "Estado:", 9)
        self.estado_entry = tk.Entry(fields_frame, font=("Arial", 11), width=40)
        self.estado_entry.grid(row=9, column=1, padx=10, pady=10)
        
        # Campo Gênero
        self.add_field(fields_frame, "Gênero:", 10)
        self.genero_var = tk.StringVar(value="")
        genero_frame = tk.Frame(fields_frame, bg=self.cor_fundo)
        genero_frame.grid(row=10, column=1, padx=10, pady=10, sticky=tk.W)
        
        tk.Radiobutton(genero_frame, text="Masculino", variable=self.genero_var, value="Masculino", bg=self.cor_fundo, font=("Arial", 10)).pack(anchor=tk.W)
        tk.Radiobutton(genero_frame, text="Feminino", variable=self.genero_var, value="Feminino", bg=self.cor_fundo, font=("Arial", 10)).pack(anchor=tk.W)
        tk.Radiobutton(genero_frame, text="Outro", variable=self.genero_var, value="Outro", bg=self.cor_fundo, font=("Arial", 10)).pack(anchor=tk.W)
        
        # Frame para botões
        button_frame = tk.Frame(main_frame, bg=self.cor_fundo)
        button_frame.pack(pady=20)
        
        # Botão Cadastrar
        cadastrar_button = tk.Button(
            button_frame,
            text="CADASTRAR",
            font=("Arial", 12, "bold"),
            bg=self.cor_secundaria,
            fg=self.cor_texto,
            width=20,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.cadastrar
        )
        cadastrar_button.pack(side=tk.LEFT, padx=5)
        
        # Botão Cancelar
        cancelar_button = tk.Button(
            button_frame,
            text="CANCELAR",
            font=("Arial", 12),
            bg="#e5e7eb",
            fg=self.cor_primaria,
            width=20,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.root.destroy
        )
        cancelar_button.pack(side=tk.LEFT, padx=5)
    
    def add_field(self, parent, label_text, row):
        label = tk.Label(
            parent,
            text=label_text,
            font=("Arial", 10),
            fg=self.cor_primaria,
            bg=self.cor_fundo
        )
        label.grid(row=row, column=0, sticky=tk.W, padx=10, pady=10)
    
    def cadastrar(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        cpf = self.cpf_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        confirmar_senha = self.confirmar_senha_entry.get()
        local = self.local_entry.get()
        telefone = self.telefone_entry.get()
        cidade = self.cidade_entry.get()
        estado = self.estado_entry.get()
        genero = self.genero_var.get()
        
        # Validações
        if not all([nome, idade, cpf, email, senha, confirmar_senha, local, telefone, cidade, estado, genero]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
        
        if "@" not in email:
            messagebox.showerror("Erro", "Email inválido!")
            return
        
        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return
        
        if len(senha) < 6:
            messagebox.showerror("Erro", "A senha deve ter no mínimo 6 caracteres!")
            return
        
        if len(cpf) < 11:
            messagebox.showerror("Erro", "CPF inválido!")
            return
        
        try:
            idade = int(idade)
            if idade < 13:
                messagebox.showerror("Erro", "Você deve ter no mínimo 13 anos!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número!")
            return
        
        # Aqui você salvaria os dados no banco de dados
        messagebox.showinfo("Sucesso", f"Cadastro realizado com sucesso!\nBem-vindo, {nome}!")
        self.root.destroy()


def main():
    root = tk.Tk()
    LoginScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
