
# ============================================================
# PORTADA
# Nombre: Brayan Daniel De Jesús Muños Navarro
# Matrícula: YOUR_ENROLLMENT_NUMBER
# Grupo: YOUR_GROUP
# Asignatura: Python - Manejo de Strings
# ============================================================

# ============================================================
# RESUMEN EJECUTIVO
# Un string en Python es una secuencia de caracteres del tipo str.
# Los strings son inmutables, por lo que su contenido original
# no puede modificarse directamente; las operaciones generan
# nuevas cadenas de texto.
# Python permite concatenar cadenas, conocer su longitud, extraer
# subcadenas, buscar patrones y reemplazar texto.
# La validación y normalización de entradas ayuda a evitar errores
# al procesar nombres, correos electrónicos y contraseñas.
# Este trabajo contiene seis problemas sobre el manejo de strings.
# Cada problema incluye entradas, salidas, validaciones y tres
# casos de prueba: normal, borde y error.
# ============================================================

# ============================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# 1. Los strings son inmutables; los cambios generan otra cadena.
# 2. Utilizar strip() y lower() para normalizar cuando corresponda.
# 3. Documentar los slices para explicar qué caracteres extraen.
# 4. Aprovechar los métodos integrados de Python.
# 5. Validar primero que la entrada no esté vacía y después
#    comprobar que cumpla el formato requerido.
# 6. Utilizar variables descriptivas y mensajes claros de error.
# ============================================================


# ============================================================
# PROBLEM 1: FULL NAME FORMATTER
#
# Description:
# Formats a full name using title case and generates initials.
#
# Inputs:
# full_name: a string containing a person's full name.
#
# Outputs:
# Formatted name and initials.
#
# Validations:
# The name must not be empty and must contain at least two words.
#
# Test cases:
# 1) Normal: "juan carlos tovar" -> "Juan Carlos Tovar"
# 2) Border: " Ana Lopez " -> "Ana Lopez"
# 3) Error: "   " -> "Error: invalid input"
# ============================================================

def problem_1():
    print("\n--- Problem 1: Full Name Formatter ---")

    full_name = input("Enter your full name: ").strip()

    if not full_name:
        print("Error: invalid input")
        return

    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("Error: enter at least two words")
        return

    formatted_name = " ".join(name_parts).title()
    initials = ""

    for name_part in name_parts:
        initials += name_part[0].upper() + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ============================================================
# PROBLEM 2: SIMPLE EMAIL VALIDATOR
#
# Description:
# Checks a basic email format and displays its domain.
#
# Inputs:
# email_text: an email address.
#
# Outputs:
# Valid email: true or false.
# Domain: the domain when the email is valid.
#
# Validations:
# The input must not be empty or contain whitespace.
# It must contain exactly one '@', text before and after it,
# and a domain containing a dot with text on both sides.
#
# Test cases:
# 1) Normal: "student@example.com" -> true
# 2) Border: "a@b.co" -> true
# 3) Error: "studentexample.com" -> false
# ============================================================

def problem_2():
    print("\n--- Problem 2: Simple Email Validator ---")

    email_text = input("Enter an email address: ").strip()

    if not email_text:
        print("Error: invalid input")
        print("Valid email: false")
        return

    valid_email = False
    domain_part = ""

    if (
        not any(character.isspace() for character in email_text)
        and email_text.count("@") == 1
    ):
        at_position = email_text.find("@")
        local_part = email_text[:at_position]
        domain_part = email_text[at_position + 1:]

        if local_part and domain_part and "." in domain_part:
            domain_parts = domain_part.split(".")

            if all(domain_parts):
                valid_email = True

    print(f"Valid email: {str(valid_email).lower()}")

    if valid_email:
        print(f"Domain: {domain_part}")


# ============================================================
# PROBLEM 3: PALINDROME CHECKER
#
# Description:
# Checks whether a phrase reads the same forward and backward,
# ignoring spaces and uppercase/lowercase differences.
#
# Inputs:
# phrase: a text phrase.
#
# Outputs:
# Normalized phrase and palindrome result.
#
# Validations:
# The phrase must not be empty and must contain at least
# three characters after removing spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true
# 2) Border: "aba" -> true
# 3) Error: " a " -> invalid input
# ============================================================

def problem_3():
    print("\n--- Problem 3: Palindrome Checker ---")

    phrase = input("Enter a phrase: ").strip()

    if not phrase:
        print("Error: invalid input")
        return

    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < 3:
        print("Error: enter at least 3 characters")
        return

    reversed_phrase = normalized_phrase[::-1]
    is_palindrome = normalized_phrase == reversed_phrase

    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {str(is_palindrome).lower()}")


# ============================================================
# PROBLEM 4: SENTENCE WORD STATISTICS
#
# Description:
# Counts the words in a sentence and identifies its first,
# last, shortest, and longest words.
#
# Inputs:
# sentence: a non-empty sentence.
#
# Outputs:
# Word count, first word, last word, shortest word,
# and longest word.
#
# Validations:
# The sentence must not be empty and must contain at least
# one word after split().
#
# Test cases:
# 1) Normal: "Python is very useful" -> count: 4
# 2) Border: "Hello" -> count: 1
# 3) Error: "   " -> "Error: invalid input"
# ============================================================

def problem_4():
    print("\n--- Problem 4: Sentence Word Statistics ---")

    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    words = sentence.split()

    if not words:
        print("Error: no valid words")
        return

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ============================================================
# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
#
# Description:
# Classifies a password as weak, medium, or strong according
# to its length and character types.
#
# Inputs:
# password_input: a password string.
#
# Outputs:
# Password strength: weak, medium, or strong.
#
# Validations:
# The password must not be empty.
#
# Rules:
# Weak: fewer than 8 characters.
# Strong: at least 8 characters with uppercase, lowercase,
# a digit, and a non-alphanumeric symbol.
# Medium: at least 8 characters but not strong.
#
# Test cases:
# 1) Normal: "Hello123!" -> strong
# 2) Border: "Abcdef12" -> medium
# 3) Error: empty input -> "Error: invalid input"
# ============================================================

MIN_PASSWORD_LENGTH = 8


def problem_5():
    print("\n--- Problem 5: Password Strength Classifier ---")

    password_input = input("Enter a password: ")

    if not password_input.strip():
        print("Error: invalid input")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True

        if character.islower():
            has_lower = True

        if character.isdigit():
            has_digit = True

        if not character.isalnum() and not character.isspace():
            has_symbol = True

    if len(password_input) < MIN_PASSWORD_LENGTH:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")


# ============================================================
# PROBLEM 6: PRODUCT LABEL FORMATTER
#
# Description:
# Creates a product label with its name and price.
# The final label must contain exactly 30 characters.
# Short labels are padded with spaces; long labels are truncated.
#
# Inputs:
# product_name: a product name.
# price_value: a positive numeric price.
#
# Outputs:
# Label containing exactly 30 characters.
#
# Validations:
# The product name must not be empty.
# The price must be numeric and greater than zero.
#
# Test cases:
# 1) Normal: "Pen", "12.50" -> 30-character label
# 2) Border: "A", "0.01" -> 30-character label
# 3) Error: "Pen", "abc" -> "Error: invalid price"
# ============================================================

LABEL_WIDTH = 30


def problem_6():
    print("\n--- Problem 6: Product Label Formatter ---")

    product_name = input("Enter product name: ").strip()

    if not product_name:
        print("Error: invalid product name")
        return

    price_text = input("Enter product price: ").strip()

    try:
        price_value = float(price_text)
    except ValueError:
        print("Error: invalid price")
        return

    if price_value <= 0:
        print("Error: price must be positive")
        return

    price_string = f"{price_value:.2f}"
    base_label = f"Product: {product_name} | Price: ${price_string}"

    # Keep the first 30 characters or pad the label with spaces.
    label = base_label[:LABEL_WIDTH].ljust(LABEL_WIDTH)

    print(f'Label: "{label}"')
    print(f"Label length: {len(label)}")


# ============================================================
# MAIN PROGRAM
# Executes all six problems in order.
# ============================================================

def main():
    print("PYTHON STRING MANIPULATION ASSIGNMENT")

    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()

    print("\nAssignment completed.")


if __name__ == "__main__":
    main()


# ============================================================
# CONCLUSIONES
# El manejo de strings es fundamental para recibir, procesar
# y mostrar información de manera clara y organizada.
# El método strip() elimina los espacios al principio y al final,
# mientras que lower() facilita comparar texto sin distinguir
# entre mayúsculas y minúsculas.
# El método split() separa palabras y join() permite unirlas.
# Las validaciones ayudan a detectar entradas vacías o incorrectas
# antes de procesarlas y reducen los errores en los programas.
# Aprendí que los strings son inmutables y que los slices permiten
# extraer o recortar partes de una cadena de forma sencilla.
# ============================================================

# ============================================================
# REFERENCES
# 1. Python Software Foundation. Built-in Types: str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2. Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 3. Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
#
# 4. Python Software Foundation. More Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 5. Python Software Foundation. An Informal Introduction to Python.
#    https://docs.python.org/3/tutorial/introduction.html
# ============================================================
