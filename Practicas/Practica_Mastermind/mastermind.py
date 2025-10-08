
#!/usr/bin/env python3
# mastermind.py
# Juego Mastermind (colores) - requiere `emoji` (se intenta importar, si no está, se usa un fallback)
# Uso: python mastermind.py

import random
try:
    import emoji
    def e(alias): 
        # usa emoji.emojize para permitir alias como ":red_circle:"
        return emoji.emojize(alias, language='alias')
except Exception:
    # fallback simple con caracteres emoji literales si la librería no está instalada
    def e(alias):
        fallback = {
            ":red_circle:":"🔴", ":blue_circle:":"🔵", ":green_circle:":"🟢",
            ":yellow_circle:":"🟡", ":purple_circle:":"🟣", ":orange_circle:":"🟠",
            ":white_large_square:":"⬜", ":black_large_square:":"⬛"
        }
        return fallback.get(alias, alias)

# Paleta de colores: 6 colores. Puedes cambiar el número y los emojis.
PALETTE = {
    "R": (e(":red_circle:"), "red"),
    "B": (e(":blue_circle:"), "blue"),
    "G": (e(":green_circle:"), "green"),
    "Y": (e(":yellow_circle:"), "yellow"),
    "P": (e(":purple_circle:"), "purple"),
    "O": (e(":orange_circle:"), "orange"),
}

CODE_LENGTH = 4
MAX_ATTEMPTS = 10

def generate_secret():
    keys = list(PALETTE.keys())
    return [random.choice(keys) for _ in range(CODE_LENGTH)]

def score_guess(secret, guess):
    # devuelve (black, white)
    # black = color correcto en posición correcta
    # white = color correcto en posición incorrecta (sin contar los ya 'black' ni duplicados)
    black = 0
    white = 0
    secret_remaining = []
    guess_remaining = []
    # primeros pases: contar blacks
    for s,g in zip(secret, guess):
        if s == g:
            black += 1
        else:
            secret_remaining.append(s)
            guess_remaining.append(g)
    # contar whites: por frecuencia
    from collections import Counter
    sec_count = Counter(secret_remaining)
    for g in guess_remaining:
        if sec_count.get(g,0) > 0:
            white += 1
            sec_count[g] -= 1
    return black, white

def format_code(code):
    # convierte lista de letras en emojis separados
    return " ".join(PALETTE[c][0] for c in code)

def print_welcome():
    print("=== Mastermind (colores) ===")
    print(f"Adivina la secuencia secreta de {CODE_LENGTH} colores.")
    print(f"Tienes {MAX_ATTEMPTS} intentos.")
    print("Paleta (usa las letras para introducir tu jugada):")
    for k,(emoji_char,name) in PALETTE.items():
        print(f"  {k} -> {emoji_char} ({name})")
    print("Ejemplo de jugada: RGBY (sin espacios).")

def parse_input(s):
    s = s.strip().upper().replace(" ", "")
    if len(s) != CODE_LENGTH:
        return None
    for ch in s:
        if ch not in PALETTE:
            return None
    return list(s)

def main():
    secret = generate_secret()
    # DEBUG: descomenta la siguiente línea para ver el secreto al iniciar (útil para pruebas)
    # print("DEBUG secret:", secret)
    attempts = 0
    print_welcome()
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        while True:
            guess_raw = input(f"Intento {attempts}/{MAX_ATTEMPTS} > ")
            guess = parse_input(guess_raw)
            if guess is None:
                print(f"Entrada inválida. Introduce {CODE_LENGTH} letras válidas (p.ej. RGBY).")
                continue
            break
        black, white = score_guess(secret, guess)
        print(f"Tú: {format_code(guess)}   ->  Comprobación: {e(':black_large_square:')}*{black}  {e(':white_large_square:')}*{white}")
        if black == CODE_LENGTH:
            print("¡Felicidades! Has acertado la combinación secreta.")
            print("Combinación:", format_code(secret))
            return
    print("Se acabaron los intentos. Has perdido.")
    print("La combinación secreta era:", format_code(secret))

if __name__ == "__main__":
    main()
