# 🤖 J.A.R.V.I.S Beta — Personal Assistant

> *Just A Rather Very Intelligent System*

J.A.R.V.I.S Beta is a Python-based personal assistant developed as part of my programming journey. Its goal is to automate simple tasks and provide useful information through text commands.

This project is a work in progress, built to practise Python, functions, dictionaries, APIs, and program logic.

## ✨ Features

- 🕒 **Time:** Displays the current time.
- 📅 **Date:** Displays the current date and day of the week.
- 🌦️ **Weather:** Retrieves current weather information for Maputo using the WeatherAPI.
- 🧮 **Calculator:** Performs basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- 👋 **Greetings:** Responds to simple greetings.
- 🤖 **Self-introduction:** Explains the meaning of J.A.R.V.I.S.
- 🚪 **Exit command:** Allows the user to close the assistant.

## 🛠️ Technologies

- Python
- `datetime` — date and time handling
- `requests` — HTTP requests to the weather API
- WeatherAPI — current weather data

## 📋 Requirements

- Python 3
- Internet connection for weather information
- A WeatherAPI API key

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/cleytonmanhica/python-learning-journey.git
```

### 2. Enter the project directory

```bash
cd python-learning-journey/projectos/jarvis
```

### 3. Install the required library

```bash
python3 -m pip install requests
```

### 4. Configure the API key

Set your WeatherAPI key as an environment variable named `WEATHER_API_KEY`. Never publish your private API key in your source code.

### 5. Run the assistant

```bash
python3 main.py
```

*Note: Adjust the directory or filename in these commands if your project uses a different structure.*

## 💬 Example Commands

The assistant currently recognises text commands such as:

- `olá`
- `que horas são`
- `qual é a data`
- `qual é a temperatura`
- `calcule`
- `quem és tu`
- `sair`

Commands are currently entered through the terminal. Voice recognition is not yet implemented.

## 🗺️ Roadmap

- [x] Basic text command system
- [x] Date and time functions
- [x] Basic calculator
- [x] Weather API integration
- [ ] Improve error handling
- [ ] Protect API credentials using environment variables
- [ ] Add more commands and features
- [ ] Explore voice recognition
- [ ] Improve the assistant's command recognition

## 📚 What I'm Learning

Through this project, I'm practising:

- Python functions and dictionaries
- Conditional statements and loops
- User input and command processing
- Working with external APIs
- Organising and improving a real programming project

## 👨‍💻 Author

**Cleyton Salomão Manhiça**

Student and aspiring software developer from Mozambique.

GitHub: [@cleytonmanhica](https://github.com/cleytonmanhica)

> *1% better every day.* ⚙️🧠🚀

## 📌 Project Status

**In development — Beta**

J.A.R.V.I.S is an educational project. Features and documentation will evolve as I continue learning Python and software development.

