import re

def check_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Add special characters")

    # Common Password Check
    try:
        with open("common_passwords.txt") as f:
            common = f.read().splitlines()
            if password in common:
                return {
                    "strength": "Very Weak",
                    "score": 0,
                    "feedback": ["This is a common password!"]
                }
    except:
        pass

    # Strength Level
    if score <= 2:
        strength = "Weak"
    elif score <= 5:
        strength = "Medium"
    elif score <= 7:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }
