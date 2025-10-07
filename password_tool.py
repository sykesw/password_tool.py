import tkinter as tk
from tkinter import messagebox
import secrets
import string
import math

# ---------- PASSWORD ENTROPY FUNCTION ----------
def calculate_entropy(password):
    if not password:
        return 0

    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    entropy = len(password) * math.log2(pool) if pool > 0 else 0
    return entropy

def strength_label(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Reasonable"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

# ---------- PASSWORD GENERATOR ----------
def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# ---------- GUI ----------
def check_strength():
    password = entry_password.get()
    entropy = calculate_entropy(password)
    strength = strength_label(entropy)
    label_result.config(
        text=f"Entropy: {entropy:.2f} bits\nStrength: {strength}",
        fg=("red" if strength in ["Very Weak", "Weak"] else "green")
    )

def generate_new_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number.")
        return

    new_pw = generate_password(length)
    entry_password.delete(0, tk.END)
