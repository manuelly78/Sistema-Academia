import sys
import traceback

try:
    import tkinter as tk
except Exception as e:
    print(f"tkinter import failed: {e}")
    sys.exit(1)

try:
    # Carrega o arquivo main.py
    with open(r"c:\Users\diliu\OneDrive\Área de Trabalho\Codigos.python\main.py", "r", encoding="utf-8") as f:
        code = f.read()
    # Executa o código em um namespace separado
    ns = {}
    exec(code, ns)
    print("Script carregado com sucesso")

    # Inicializa a tela sem mostrar
    root = tk.Tk()
    root.withdraw()
    LoginScreen = ns.get('LoginScreen')
    if LoginScreen is None:
        print('LoginScreen não encontrado no script')
        sys.exit(1)
    app = LoginScreen(root)
    print('LoginScreen inicializado com sucesso')
    root.destroy()

except Exception:
    traceback.print_exc()
    sys.exit(1)
