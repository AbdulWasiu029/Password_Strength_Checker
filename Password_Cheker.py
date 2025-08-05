import re

# Common weak passwords list (you can expand this)
common_passwords = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "123123", "password1", "1234", "admin", "password123"
]

def password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) < 6:
        feedback.append("❌ Password is too short (minimum 6 characters).")
    elif len(password) >= 8:
        score += 1
        feedback.append("✅ Good length.")
    else:
        feedback.append("⚠️ Try using at least 8 characters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase letter.")
    else:
        feedback.append("⚠️ Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase letter.")
    else:
        feedback.append("⚠️ Add at least one lowercase letter.")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Contains a number.")
    else:
        feedback.append("⚠️ Add at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("✅ Contains a special character.")
    else:
        feedback.append("⚠️ Add at least one special character.")

    # Check for common passwords
    if password.lower() in common_passwords:
        feedback.append("❌ This is a common/weak password.")
        score = 0 

    # Final strength
    strength = ""
    if score == 5:
        strength = "Strong 💪"
    elif 3 <= score < 5:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, feedback

# Run checker
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength, tips = password_strength(user_password)
    print(f"\nPassword Strength: {strength}")
    print("Feedback:")
    for tip in tips:
        print(f"- {tip}")
