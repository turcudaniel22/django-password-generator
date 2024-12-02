# Django Password Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)  
![Django](https://img.shields.io/badge/Django-4.2-green.svg?logo=django&logoColor=white)  
![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white)  
![VS Code](https://img.shields.io/badge/VS%20Code-0078D4.svg?logo=visual-studio-code&logoColor=white)  

🔒 Django Password Generator


A simple and secure Django Password Generator web application that lets users create customizable passwords for better online security.

✨ Features

🔑 Customizable Passwords: Choose from uppercase, lowercase, numbers, and symbols.
📏 Adjustable Length: Generate passwords of any desired length.
⚡ Fast and Secure: Uses Python’s secrets library for secure password generation.
📱 Responsive Design: Fully functional on mobile and desktop browsers.
📂 Project Structure

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

🚀 Quick Start

Prerequisites
Python 3.9+
Pip
Virtualenv (optional but recommended)
Installation
Clone the repository:
git clone https://github.com/turcudaniel22/django-password-generator.git
cd django-password-generator
Create a virtual environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Start the development server:
python manage.py runserver
Open in browser:
Visit http://127.0.0.1:8000
🛠 Usage

Navigate to the homepage.
Customize your password preferences:
Adjust the length.
Choose character types.
Click Generate Password.
Copy the generated password for use.
📸 Screenshots

Home Page
Password Generator
🤝 Contributing

Contributions are always welcome!

Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m "Add some feature").
Push to the branch (git push origin feature-name).
Open a pull request.
📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

🧑‍💻 Turcu Daniel

👤 Daniel

Email: turcudanieli22@gmail.com
