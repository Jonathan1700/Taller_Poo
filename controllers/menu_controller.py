import os
import sys
import runpy
import builtins

from views.consola import (
    # Utilidades
    gotoxy, limpiar_pantalla, ocultar_cursor, mostrar_cursor,
    get_cols, get_filas, w, truncar,
    # Estilo
    RESET, BOLD, TL, TR, BL, BR, H, V, ML, MR,
    # Colores
    C_BORDE_PRIN, C_TITULO_PRIN, C_OPCION_PRIN, C_RESALT_PRIN,
    C_BORDE_SUB, C_TITULO_SUB, C_OPCION_SUB, C_RESALT_SUB,
    C_SEPARADOR, C_SALIR, C_DESC_EJ,
    C_BORDE_COD, C_TITULO_COD, C_NUM_LINEA, C_CODIGO, C_SCROLL_INFO,
    C_ACCION_1, C_ACCION_0,
    C_BORDE_RUN, C_TITULO_RUN, C_ENTER, C_OPCION_PRIN,
)


class Menu:

    def __init__(self, bloques: dict):
        self.bloques = bloques

    # ── Helpers internos de dibujo ────────────────────────────────

    @staticmethod
    def _bh(x, y, ancho, izq, der, color):
        gotoxy(x, y)
        w(f"{color}{izq}{H*(ancho-2)}{der}{RESET}")

    @staticmethod
    def _pw(x_ini, x_fin, y, color):
        gotoxy(x_ini, y); w(f"{color}{V}{RESET}")
        gotoxy(x_fin,  y); w(f"{color}{V}{RESET}")

    @staticmethod
    def _lf(x_ini, interior, y):
        gotoxy(x_ini + 1, y); w(" " * interior)

    @staticmethod
    def _ct(x_ini, interior, y, texto, color=""):
        pad = max(0, (interior - len(texto)) // 2)
        gotoxy(x_ini + 1 + pad, y)
        w(f"{color}{texto}{RESET}")

    # ── Menú principal ────────────────────────────────────────────

    def mostrar_principal(self):
        while True:
            limpiar_pantalla()
            ocultar_cursor()

            c     = get_cols()
            f     = get_filas()
            ancho = max(56, min(72, c - 4))
            inter = ancho - 2
            alto  = len(self.bloques) + 6
            x_ini = max(1, (c - ancho) // 2 + 1)
            x_fin = x_ini + ancho - 1
            y_ini = max(1, (f - alto) // 2)
            cb    = C_BORDE_PRIN
            et    = inter - 22

            self._bh(x_ini, y_ini, ancho, TL, TR, cb)

            y = y_ini + 1
            self._pw(x_ini, x_fin, y, cb)
            self._lf(x_ini, inter, y)
            self._ct(x_ini, inter, y, "✦  MENÚ PRINCIPAL  ✦", BOLD + C_TITULO_PRIN)

            y += 1
            self._bh(x_ini, y, ancho, ML, MR, cb)

            for key, bloque in self.bloques.items():
                y += 1
                self._pw(x_ini, x_fin, y, cb)
                self._lf(x_ini, inter, y)
                nombre = bloque['nombre'][:10]
                tema   = truncar(bloque['tema'], max(8, et))
                linea  = (f"  {C_RESALT_PRIN}[{RESET}{C_OPCION_PRIN}{key:>2}{RESET}"
                          f"{C_RESALT_PRIN}]{RESET}  "
                          f"{C_OPCION_PRIN}{nombre:<10}{RESET}  "
                          f"{C_SEPARADOR}│{RESET}  "
                          f"{C_OPCION_PRIN}{tema}{RESET}")
                gotoxy(x_ini + 1, y); w(linea)

            y += 1; self._bh(x_ini, y, ancho, ML, MR, cb)
            y += 1
            self._pw(x_ini, x_fin, y, cb)
            self._lf(x_ini, inter, y)
            gotoxy(x_ini + 1, y)
            w(f"  {C_RESALT_PRIN}[{RESET}{C_SALIR}S{RESET}"
              f"{C_RESALT_PRIN}]{RESET}  {C_SALIR}Salir del programa{RESET}")

            y += 1; self._bh(x_ini, y, ancho, BL, BR, cb)

            gotoxy(x_ini, y + 2); mostrar_cursor()
            print(f"{C_TITULO_PRIN}  ➤  Elige un bloque: {RESET}", end="", flush=True)
            opcion = input().strip().lower()

            if opcion == 's':
                limpiar_pantalla()
                print(f"\n{C_SALIR}{BOLD}  Saliendo del programa...{RESET}\n")
                break
            elif opcion in self.bloques:
                limpiar_pantalla()
                self.mostrar_submenu(self.bloques[opcion])
            else:
                gotoxy(x_ini, y + 4)
                print(f"{C_SALIR}  Opción no válida.{RESET}", end="", flush=True)
                mostrar_cursor(); input()

    # ── Submenú ───────────────────────────────────────────────────

    def mostrar_submenu(self, bloque: dict):
        nombre_bloque = bloque['nombre']
        tema          = bloque['tema']
        ejercicios    = bloque['ejercicios']

        while True:
            limpiar_pantalla()
            ocultar_cursor()

            c     = get_cols()
            ancho = max(60, min(88, c - 2))
            inter = ancho - 2
            x_ini = max(1, (c - ancho) // 2 + 1)
            x_fin = x_ini + ancho - 1
            cb    = C_BORDE_SUB
            ed    = inter - 26

            y = 2
            self._bh(x_ini, y, ancho, TL, TR, cb)
            y += 1
            self._pw(x_ini, x_fin, y, cb); self._lf(x_ini, inter, y)
            titulo = truncar(f"✦  {nombre_bloque.upper()}  —  {tema.upper()}  ✦", inter - 4)
            self._ct(x_ini, inter, y, titulo, BOLD + C_TITULO_SUB)
            y += 1; self._bh(x_ini, y, ancho, ML, MR, cb)

            opciones_validas = {}
            for i, (nombre_ej, datos) in enumerate(ejercicios.items(), start=1):
                y += 1
                self._pw(x_ini, x_fin, y, cb); self._lf(x_ini, inter, y)
                desc  = truncar(datos['desc'], max(10, ed))
                linea = (f"  {C_RESALT_SUB}[{RESET}{C_OPCION_SUB}{i}{RESET}"
                         f"{C_RESALT_SUB}]{RESET}  "
                         f"{C_OPCION_SUB}{BOLD}{nombre_ej:<14}{RESET}  "
                         f"{C_SEPARADOR}│{RESET}  "
                         f"{C_OPCION_SUB}{desc}{RESET}")
                gotoxy(x_ini + 1, y); w(linea)
                opciones_validas[str(i)] = datos

            y += 1; self._bh(x_ini, y, ancho, ML, MR, cb)
            y += 1
            self._pw(x_ini, x_fin, y, cb); self._lf(x_ini, inter, y)
            gotoxy(x_ini + 1, y)
            w(f"  {C_RESALT_SUB}[{RESET}{C_SALIR}0{RESET}"
              f"{C_RESALT_SUB}]{RESET}  {C_SALIR}Regresar al Menú Principal{RESET}")
            y += 1; self._bh(x_ini, y, ancho, BL, BR, cb)

            gotoxy(x_ini, y + 2); mostrar_cursor()
            print(f"{C_TITULO_SUB}  ➤  Elige un ejercicio: {RESET}", end="", flush=True)
            opcion = input().strip()

            if opcion == '0':
                break
            elif opcion in opciones_validas:
                datos = opciones_validas[opcion]
                if self._mostrar_codigo(datos):
                    self._ejecutar_en_marco(datos['ruta'], datos['desc'])
            else:
                gotoxy(x_ini, y + 4)
                print(f"{C_SALIR}  Opción no válida.{RESET}", end="", flush=True)
                mostrar_cursor(); input()

    # ── Visor de código ───────────────────────────────────────────

    def _mostrar_codigo(self, datos: dict) -> bool:
        ruta = datos['ruta']
        desc = datos['desc']

        if not os.path.exists(ruta):
            limpiar_pantalla()
            print(f"\n{C_SALIR}  ¡Error! No se encontró: {ruta}{RESET}\n")
            mostrar_cursor(); input("  Presiona Enter para continuar...")
            return False

        with open(ruta, "r", encoding="utf-8", errors="replace") as f:
            lineas = f.read().splitlines()

        c         = get_cols()
        f_        = get_filas()
        ancho     = max(60, min(90, c - 2))
        inter     = ancho - 2
        x_ini     = max(1, (c - ancho) // 2 + 1)
        x_fin     = x_ini + ancho - 1
        cod_w     = inter - 6
        CABECERA  = 5
        PIE       = 4
        filas_cod = max(5, f_ - CABECERA - PIE - 2)
        cb        = C_BORDE_COD

        def bh(y, izq, der):
            gotoxy(x_ini, y); w(f"{cb}{izq}{H*(ancho-2)}{der}{RESET}")

        def pared(y):
            gotoxy(x_ini, y); w(f"{cb}{V}{RESET}")
            gotoxy(x_fin,  y); w(f"{cb}{V}{RESET}")

        def lf(y):
            gotoxy(x_ini+1, y); w(" "*inter)

        def ct(y, texto, color=""):
            pad = max(0, (inter - len(texto)) // 2)
            lf(y); gotoxy(x_ini+1+pad, y); w(f"{color}{texto}{RESET}")

        def linea_cod(y, num, texto):
            pared(y); lf(y)
            gotoxy(x_ini+1, y)
            w(f"{C_NUM_LINEA}{num:>3} {RESET}{C_SEPARADOR}│{RESET} "
              f"{C_CODIGO}{truncar(texto, cod_w)}{RESET}")

        total  = len(lineas)
        offset = 0

        while True:
            limpiar_pantalla(); ocultar_cursor()

            y = 1; bh(y, TL, TR)
            y += 1; pared(y)
            ct(y, f"◈  CÓDIGO  —  {os.path.basename(ruta)}  ◈", BOLD + C_TITULO_COD)
            y += 1; bh(y, ML, MR)
            y += 1; pared(y); lf(y)
            gotoxy(x_ini+1, y)
            w(f"{C_DESC_EJ}{truncar('  ' + desc, inter)}{RESET}")
            y += 1; bh(y, ML, MR)

            y_c = y + 1
            for rel in range(filas_cod):
                ya = y_c + rel; idx = offset + rel
                if idx < total:
                    linea_cod(ya, idx+1, lineas[idx])
                else:
                    pared(ya); lf(ya)

            y = y_c + filas_cod; bh(y, ML, MR)
            y += 1; pared(y); lf(y)
            pag_a = offset // filas_cod + 1
            pag_t = max(1, (total + filas_cod - 1) // filas_cod)
            nav   = "  W↑ subir  S↓ bajar  " if total > filas_cod else ""
            gotoxy(x_ini+1, y)
            w(f"{C_SCROLL_INFO}{truncar(f'  Líneas {offset+1}–{min(offset+filas_cod,total)} de {total}  [{pag_a}/{pag_t}]{nav}', inter)}{RESET}")

            y += 1; bh(y, ML, MR)
            y += 1; pared(y); lf(y)
            gotoxy(x_ini+1, y)
            w(f"  {C_BORDE_COD}[{RESET}{C_ACCION_1}1{RESET}{C_BORDE_COD}]{RESET}"
              f"  {C_ACCION_1}{BOLD}Ejecutar{RESET}"
              f"          "
              f"{C_BORDE_COD}[{RESET}{C_ACCION_0}0{RESET}{C_BORDE_COD}]{RESET}"
              f"  {C_ACCION_0}Volver{RESET}")
            y += 1; bh(y, BL, BR)

            gotoxy(x_ini, y+2); mostrar_cursor()
            print(f"{C_TITULO_COD}  ➤  Opción: {RESET}", end="", flush=True)
            tecla = input().strip().lower()

            if tecla in ('1', ''):    return True
            elif tecla in ('0', 'q'): return False
            elif tecla in ('s', 'j'):
                if offset + filas_cod < total: offset += filas_cod
            elif tecla in ('w', 'k'):
                offset = max(0, offset - filas_cod)

    # ── Ejecutar dentro de marco ──────────────────────────────────

    @staticmethod
    def _ejecutar_en_marco(ruta: str, descripcion: str = ""):
        limpiar_pantalla()

        c     = get_cols()
        ancho = min(78, c - 2)
        inter = ancho - 2
        x_ini = max(1, (c - ancho) // 2 + 1)
        x_fin = x_ini + ancho - 1
        cb    = C_BORDE_RUN

        def bh(y, izq, der, color=None):
            clr = color or cb
            gotoxy(x_ini, y)
            w(f"{clr}{izq}{H*(ancho-2)}{der}{RESET}")

        def pared(y, color=None):
            clr = color or cb
            gotoxy(x_ini, y); w(f"{clr}{V}{RESET}")
            gotoxy(x_fin,  y); w(f"{clr}{V}{RESET}")

        def lf(y):
            gotoxy(x_ini+1, y); w(" "*inter)

        def fila_ct(y, texto, color_txt, color_borde=None):
            pared(y, color_borde); lf(y)
            pad = max(0, (inter - len(texto)) // 2)
            gotoxy(x_ini+1+pad, y)
            w(f"{color_txt}{texto}{RESET}")

        def fila_tx(y, texto, color_txt, indent=1):
            pared(y); lf(y)
            trunc = truncar(texto, inter - indent - 1)
            gotoxy(x_ini + indent, y)
            w(f"{color_txt}{trunc}{RESET}")

        def fila_v(y):
            pared(y); lf(y)

        y = 2
        bh(y, TL, TR)
        y += 1; fila_ct(y, "▶  EJECUTANDO EJERCICIO", BOLD + C_TITULO_RUN)
        y += 1; bh(y, ML, MR)
        y += 1; fila_tx(y, f"Archivo : {ruta}", C_OPCION_PRIN)

        label    = "Desc.   : "
        max_body = inter - len(label) - 2
        if len(descripcion) <= max_body:
            y += 1; fila_tx(y, f"{label}{descripcion}", C_DESC_EJ)
        else:
            y += 1; fila_tx(y, f"{label}{descripcion[:max_body]}", C_DESC_EJ)
            y += 1; fila_tx(y, " "*len(label) + truncar(descripcion[max_body:], max_body), C_DESC_EJ)

        y += 1; bh(y, ML, MR)
        y += 1; fila_v(y)
        y_out = y + 1

        mostrar_cursor()

        # ── MONKEY-PATCH ──────────────────────────────────────────
        _orig_print = builtins.print
        _orig_input = builtins.input
        estado = {"fila": y_out, "prompt_pendiente": ""}

        def _dibujar_fila(texto: str, color_txt: str = C_OPCION_PRIN):
            yf = estado["fila"]
            gotoxy(x_ini, yf); w(f"{cb}{V}{RESET}")
            trunc = truncar(texto, inter - 2)
            gotoxy(x_ini + 2, yf); w(f"{color_txt}{trunc}{RESET}")
            relleno = inter - 2 - len(trunc)
            if relleno > 0: w(" " * relleno)
            gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
            estado["fila"] += 1

        def pared_print(*args, **kwargs):
            sep  = kwargs.get("sep", " ")
            end  = kwargs.get("end", "\n")
            file = kwargs.get("file", None)
            if file is sys.stderr:
                sys.stderr.write(sep.join(str(a) for a in args) + (end if end else ""))
                return
            if file not in (None, sys.stdout):
                return
            texto  = sep.join(str(a) for a in args)
            partes = texto.split("\n")
            if end == "" and len(partes) == 1:
                estado["prompt_pendiente"] += partes[0]
                return
            if estado["prompt_pendiente"]:
                partes[0] = estado["prompt_pendiente"] + partes[0]
                estado["prompt_pendiente"] = ""
            for parte in partes:
                _dibujar_fila(parte)

        def pared_input(prompt=""):
            prompt_str = estado["prompt_pendiente"] + str(prompt)
            estado["prompt_pendiente"] = ""
            yf = estado["fila"]
            gotoxy(x_ini, yf); w(f"{cb}{V}{RESET}")
            trunc = truncar(prompt_str, inter - 4)
            gotoxy(x_ini + 2, yf); w(f"{C_DESC_EJ}{trunc}{RESET}")
            col_input = x_ini + 2 + len(trunc)
            relleno = inter - 2 - len(trunc)
            if relleno > 0: w(" " * relleno)
            gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
            gotoxy(col_input, yf)
            val = sys.stdin.readline().rstrip("\n")
            gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
            estado["fila"] += 1
            return val

        builtins.print = pared_print
        builtins.input = pared_input

        try:
            runpy.run_path(os.path.abspath(ruta), run_name="__main__")
        except SystemExit:
            pass
        except Exception as e:
            _dibujar_fila(f"⚠  Error: {e}", C_SALIR)
        finally:
            builtins.print = _orig_print
            builtins.input = _orig_input

        # ── PIE ───────────────────────────────────────────────────
        yp = estado["fila"]
        fila_v(yp);       yp += 1
        bh(yp, ML, MR);   yp += 1
        fila_ct(yp, "✔  Ejercicio finalizado", BOLD + C_TITULO_RUN)
        yp += 1; bh(yp, ML, MR); yp += 1
        ocultar_cursor()
        fila_ct(yp, "Presiona Enter para volver al menú...", C_ENTER)
        yp += 1; bh(yp, BL, BR)

        gotoxy(x_ini + 1, yp + 1); mostrar_cursor()
        sys.stdin.readline()
