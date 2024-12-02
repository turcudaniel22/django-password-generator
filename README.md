
# Django Password Generator  
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)  
![Django](https://img.shields.io/badge/Django-4.2-green.svg?logo=django&logoColor=white)  
![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white)  
![VS Code](https://img.shields.io/badge/VS%20Code-0078D4.svg?logo=visual-studio-code&logoColor=white)  

🔒 **Django Password Generator**  

A simple and secure Django Password Generator web application that lets users create customizable passwords for better online security.

---

## ✨ Features  

- 🔑 **Customizable Passwords**: Choose from uppercase, lowercase, numbers, and symbols.  
- 📏 **Adjustable Length**: Generate passwords of any desired length.  
- ⚡ **Fast and Secure**: Uses Python’s `secrets` library for secure password generation.  
- 📱 **Responsive Design**: Fully functional on mobile and desktop browsers.  

---

## 📂 Project Structure  

```plaintext
django-password-generator/
├── manage.py
├── db.sqlite3
├── Generator/
│   ├── templates/Generator/
│   │   ├── about.html
│   │   ├── home.html
│   │   └── password.html
│   ├── urls.py
│   └── views.py
└── passwordgenerator/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

---

## 🚀 Quick Start  

### Prerequisites  

- **Python 3.9+**  
- **Pip**  
- **Virtualenv** (optional but recommended)  

### Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/turcudaniel22/django-password-generator.git
   cd django-password-generator
   ```

2. Create a virtual environment:  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:  
   ```bash
   python manage.py migrate
   ```

5. Start the development server:  
   ```bash
   python manage.py runserver
   ```

6. Open in browser:  
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Usage  

1. Navigate to the homepage.  
2. Customize your password preferences:  
   - Adjust the length.  
   - Choose character types.  
3. Click **Generate Password**.  
4. Copy the generated password for use.  

---

## 📸 Screenshots  

### Home Page  

### Password Generator  

---

## 🤝 Contributing  

Contributions are always welcome!  

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Add some feature"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```  
5. Open a pull request.  

---

## 📄 License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## 🧑‍💻 Author  

👤 **Daniel Turcu**  
- **Email**: [turcudanieli22@gmail.com](mailto:turcudanieli22@gmail.com)  
```


