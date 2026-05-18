import os
import sys
import shutil

# ─────────────────────────────────────────────
#   UTILIDADES DE CONSOLA
# ─────────────────────────────────────────────

def gotoxy(x, y):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ocultar_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def mostrar_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def get_cols():
    return shutil.get_terminal_size((80, 24)).columns

def get_filas():
    return shutil.get_terminal_size((80, 24)).lines

def w(texto):
    """Escribe directo a stdout sin pasar por builtins.print."""
    sys.stdout.write(texto)
    sys.stdout.flush()

def wln(texto=""):
    sys.stdout.write(texto + "\n")
    sys.stdout.flush()

def truncar(texto: str, max_len: int) -> str:
    if len(texto) <= max_len:
        return texto
    return texto[:max_len - 1] + "…"

# ─────────────────────────────────────────────
#   CONSTANTES DE ESTILO
# ─────────────────────────────────────────────

RESET = "\033[0m"
BOLD  = "\033[1m"

TL = "╔"; TR = "╗"; BL = "╚"; BR = "╝"
H  = "═"; V  = "║"; ML = "╠"; MR = "╣"

# ── Paleta de colores ─────────────────────────
C_BORDE_PRIN  = rgb(0, 200, 255)
C_TITULO_PRIN = rgb(255, 220, 0)
C_OPCION_PRIN = rgb(200, 255, 200)
C_RESALT_PRIN = rgb(255, 120, 0)
C_BORDE_SUB   = rgb(180, 0, 255)
C_TITULO_SUB  = rgb(0, 255, 180)
C_OPCION_SUB  = rgb(230, 230, 255)
C_RESALT_SUB  = rgb(255, 80, 80)
C_SEPARADOR   = rgb(80, 80, 120)
C_SALIR       = rgb(255, 80, 80)
C_DESC_EJ     = rgb(180, 220, 255)
C_BORDE_COD   = rgb(255, 165, 0)
C_TITULO_COD  = rgb(255, 220, 0)
C_NUM_LINEA   = rgb(100, 100, 140)
C_CODIGO      = rgb(220, 255, 180)
C_SCROLL_INFO = rgb(160, 160, 160)
C_ACCION_1    = rgb(0, 255, 180)
C_ACCION_0    = rgb(255, 80, 80)
C_BORDE_RUN   = rgb(0, 220, 120)
C_TITULO_RUN  = rgb(255, 255, 255)
C_ENTER       = rgb(255, 220, 0)

# ─────────────────────────────────────────────
#   HELPERS DE DIBUJO
#   (todos usan w/gotoxy, nunca builtins.print)
# ─────────────────────────────────────────────

def dibujar_borde_h(x, y, ancho, izq, der, color):
    gotoxy(x, y)
    w(f"{color}{izq}{H*(ancho-2)}{der}{RESET}")

def dibujar_paredes(x_ini, x_fin, y, color):
    gotoxy(x_ini, y); w(f"{color}{V}{RESET}")
    gotoxy(x_fin,  y); w(f"{color}{V}{RESET}")

def limpiar_fila(x_ini, interior, y):
    gotoxy(x_ini + 1, y)
    w(" " * interior)

def dibujar_fila_texto(x_ini, interior, y, texto, color_txt, indent=1):
    trunc = truncar(texto, interior - indent - 1)
    gotoxy(x_ini + indent, y)
    w(f"{color_txt}{trunc}{RESET}")

def dibujar_fila_centrada(x_ini, interior, y, texto, color_txt):
    texto_trunc = truncar(texto, interior - 2)
    pad = max(0, (interior - len(texto_trunc)) // 2)
    gotoxy(x_ini + 1 + pad, y)
    w(f"{color_txt}{texto_trunc}{RESET}")
