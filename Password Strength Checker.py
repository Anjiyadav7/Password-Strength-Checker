import re
import colorama
from colorama import Fore, Style

colorama.init()

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Upper & Lower Case Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Numbers Check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers to make the password stronger.")

    # Special Characters Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include special characters like @, #, or !.")

    # Common Passwords Check
    common_passwords = ["password", "123456", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        feedback.append("Your password is too common! Choose something unique.")
        score = 0  # Reset score for weak passwords

    # Repeated & Sequential Characters
    if re.search(r'(.)\1\1', password):  # e.g., aaa, 111
        feedback.append("Avoid repeating characters three times in a row.")
    if re.search(r'123|234|345|456|567|678|789', password):
        feedback.append("Avoid sequential numbers.")

    # Strength Rating
    if score >= 5:
        return Fore.GREEN + "Strong Password! ✔" + Style.RESET_ALL, feedback
    elif score >= 3:
        return Fore.YELLOW + "Moderate Password. Improve it!" + Style.RESET_ALL, feedback
    else:
        return Fore.RED + "Weak Password! ❌" + Style.RESET_ALL, feedback

# User Input
password = input("Enter your password: ")
strength, suggestions = check_password_strength(password)

print("\nStrength:", strength)
if suggestions:
    print("\nSuggestions:")
    for tip in suggestions:
        print("-", tip)
