# 🔐 Password Strength Checker (Web-Based)

A modern **Password Strength Checker Web Application** built using **Python (Flask) + JavaScript** that evaluates password security in real-time.

---

## 🚀 Features

* 🔴 **Real-time password strength detection**
* 🎯 **Live character counter**
* 🔐 **Show / Hide password**
* 🧹 **Clear password button**
* 📊 **Dynamic progress bar**
* ⚡ **No page reload (AJAX / Fetch API)**
* 🧠 **Security-based scoring system**
* ⚠️ **Common password detection**
* 💬 **Smart feedback suggestions**

---

## 🧠 How It Works

The system evaluates passwords based on:

* Length (minimum 8 characters)
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Common password list check

Each condition contributes to a **score**, which determines the final strength:

| Score Range | Strength    |
| ----------- | ----------- |
| 0 - 2       | Weak        |
| 3 - 5       | Medium      |
| 6 - 7       | Strong      |
| 8+          | Very Strong |

---

## 🏗️ Tech Stack

| Layer       | Technology                    |
| ----------- | ----------------------------- |
| Backend     | Python (Flask)                |
| Frontend    | HTML, CSS, Bootstrap          |
| Logic       | Python (Regex, File Handling) |
| API         | Flask JSON API                |
| Client-side | JavaScript (Fetch API)        |

---

## 📁 Project Structure

```
password-strength-checker/
│
├── app.py
├── strength_checker.py
├── common_passwords.txt
│
├── templates/
│   └── index.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
```

---

### 2️⃣ Install Dependencies

```bash
pip install flask
```

---

### 3️⃣ Run Application

```bash
python app.py
```

---

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🎯 Example Output

Input:

```
Abc@1234
```

Output:

* Strength: Strong
* Score: 7/10
* Suggestions:

  * Improve password length
  * Avoid common patterns

---

## 🔒 Security Notes

* ❌ Passwords are **NOT stored**
* ❌ No logging of user input
* ✅ Only real-time analysis is performed

---

## 💡 Future Improvements

* 🔥 Password entropy calculation
* 🔥 Estimated crack time (Brute-force simulation)
* 🔥 HaveIBeenPwned API integration
* 🔥 Animated UI enhancements
* 🔥 Multi-language support
