# 🔐 Password Strength Checker

A simple and effective Python script that checks the strength of a user-entered password based on multiple criteria like length, character variety, and common password usage.

---

## 🚀 Features

- Checks password **length**
- Detects presence of:
  - ✅ Uppercase letters
  - ✅ Lowercase letters
  - ✅ Numbers
  - ✅ Special characters
- Warns if password is found in a **common/weak passwords list**
- Provides a **score-based strength rating**:
  - 🔴 Weak
  - 🟡 Moderate
  - 🟢 Strong
- Gives **real-time feedback** on how to improve your password

---

## 🧠 How It Works

Each password is evaluated based on the following:

| Criteria                  | Score |
|---------------------------|-------|
| Length ≥ 8 characters     | +1    |
| Contains uppercase letter | +1    |
| Contains lowercase letter | +1    |
| Contains number           | +1    |
| Contains special char     | +1    |
| Found in common passwords | 0     |

- **Final Score:**
  - `5` → Strong 💪
  - `3-4` → Moderate ⚠️
  - `<3` → Weak ❌

---

## 📝 Usage

1. Clone the repo or copy the code into a `.py` file.

```bash
python password_checker.py
