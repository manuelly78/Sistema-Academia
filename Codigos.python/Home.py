import customtkinter as ctk
from PIL import Image

# ── Configuração visual global
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── Paleta de cores
COR_FUNDO       = "#0F1117"
COR_SIDEBAR     = "#161B27"
COR_SIDEBAR_BTN = "#1E2535"
COR_ATIVO       = "#2563EB"
COR_HOVER       = "#1D4ED8"
COR_TEXTO       = "#E2E8F0"
COR_TEXTO_SUB   = "#64748B"
COR_BORDA       = "#2D3748"


# ════════════════════════════════════════════════════════════════════════════
#  FRAMES DE CONTEÚDO
#  Cada classe representa uma tela do sistema.
#  Adicione seus widgets dentro do __init__ de cada uma.
# ════════════════════════════════════════════════════════════════════════════

class FrameDashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO, corner_radius=0)
        # Carrega a imagem
        self.imagem = ctk.CTkImage(
        light_image=Image.open("Codigos.python/Imagens/sof.jpg"),
        dark_image=Image.open("Codigos.python/Imagens/sof.jpg"),
        size=(700, 500)
)
         # Exibe a imagem
        self.label_imagem = ctk.CTkLabel(
            self,
            image=self.imagem,
            text=""
        )
        self.label_imagem.place(relx=0.5, rely=0.5, anchor="center")
      


class FrameAlunos(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO, corner_radius=0)
        # ── código do frame Alunos ─────────────────────────────────────────


class FrameFinanceiro(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO, corner_radius=0)
        # ── código do frame Financeiro ─────────────────────────────────────


class FrameModalidades(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO, corner_radius=0)
        # ── código do frame Modalidades ────────────────────────────────────


class FrameConfiguracoes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO, corner_radius=0)
        # ── código do frame Configurações ──────────────────────────────────


# ════════════════════════════════════════════════════════════════════════════
#  JANELA PRINCIPAL
# ════════════════════════════════════════════════════════════════════════════

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Academia")
        self.configure(fg_color=COR_FUNDO)

        # ── Centraliza na tela ─────────────────────────────────────────────
        largura, altura = 1200, 720
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - largura)  // 2
        y = (self.winfo_screenheight() - altura) // 2
        self.geometry(f"{largura}x{altura}+{x}+{y}")
        self.minsize(900, 600)
        self.resizable(True, True)

        self._frame_atual = None
        self._botoes: dict[str, ctk.CTkButton] = {}

        self._construir_layout()
        self._abrir_frame("Dashboard")  # tela inicial

    def _construir_layout(self):
        # ── Sidebar ────────────────────────────────────────────────────────
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0,
                                    fg_color=COR_SIDEBAR)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo
        logo = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo.pack(fill="x", padx=20, pady=(24, 20))
        ctk.CTkLabel(logo, text="🏋", font=("Segoe UI", 30)).pack(side="left")
        ctk.CTkLabel(logo, text="AcademiaApp",
                     font=("Segoe UI", 16, "bold"),
                     text_color=COR_TEXTO).pack(side="left", padx=8)

        ctk.CTkFrame(self.sidebar, height=1,
                     fg_color=COR_BORDA).pack(fill="x", padx=16, pady=(0, 16))

        # Botões de navegação — adicione/remova opções aqui
        menu = [
            ("Dashboard",    "📊"),
            ("Alunos",       "👥"),
            ("Financeiro",   "💰"),
            ("Modalidades",  "🏋"),
            ("Configuracoes","⚙"),
        ]
        for nome, icone in menu:
            label = "Configurações" if nome == "Configuracoes" else nome
            btn = ctk.CTkButton(
                self.sidebar,
                text=f" {icone}  {label}",
                anchor="w",
                height=44,
                corner_radius=8,
                fg_color="transparent",
                hover_color=COR_SIDEBAR_BTN,
                text_color=COR_TEXTO_SUB,
                font=("Segoe UI", 14),
                command=lambda n=nome: self._abrir_frame(n),
            )
            btn.pack(fill="x", padx=12, pady=3)
            self._botoes[nome] = btn

        # Rodapé sidebar
        ctk.CTkFrame(self.sidebar, height=1,
                     fg_color=COR_BORDA).pack(fill="x", padx=16, side="bottom", pady=16)
        ctk.CTkLabel(self.sidebar, text="v1.0.0",
                     font=("Segoe UI", 11),
                     text_color=COR_TEXTO_SUB).pack(side="bottom", pady=(0, 8))

        # ── Área de conteúdo ───────────────────────────────────────────────
        self.area_conteudo = ctk.CTkFrame(self, corner_radius=0, fg_color=COR_FUNDO)
        self.area_conteudo.pack(side="left", fill="both", expand=True)

    def _abrir_frame(self, nome: str):
        mapa = {
            "Dashboard":    FrameDashboard,
            "Alunos":       FrameAlunos,
            "Financeiro":   FrameFinanceiro,
            "Modalidades":  FrameModalidades,
            "Configuracoes":FrameConfiguracoes,
        }

        # Destaca botão ativo
        for n, btn in self._botoes.items():
            btn.configure(
                fg_color=COR_ATIVO if n == nome else "transparent",
                text_color=COR_TEXTO if n == nome else COR_TEXTO_SUB,
            )

        # Destroi frame anterior e carrega o novo
        if self._frame_atual:
            self._frame_atual.destroy()

        cls = mapa.get(nome, FrameDashboard)
        self._frame_atual = cls(self.area_conteudo)
        self._frame_atual.pack(fill="both", expand=True)


# ── Entry point
if __name__ == "__main__":
    app = App()
    app.mainloop()