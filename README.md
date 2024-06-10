
# Backend AI Company

## Introduction

Welcome to the Backend AI Company project! This project is the server-side part of our AI company system. It is built using FastAPI, a modern web framework for building APIs with Python.

## Prerequisites

To run this project, you need to have the following installed on your computer:
- **Python**: A programming language.
- **Git**: A version control system.

Don't worry if you don't have these installed. Here are some easy steps to get you started:

### Install Python

1. Go to the Python website: [https://www.python.org/](https://www.python.org/)
2. Download and install the latest version of Python.

### Install Git

1. Go to the Git website: [https://git-scm.com/](https://git-scm.com/)
2. Download and install Git for your operating system.

## Cloning the Repository

First, you need to get a copy of the project on your computer. Open the terminal (Command Prompt on Windows, Terminal on macOS, or your favorite terminal on Linux) and run the following command:

```sh
git clone https://github.com/JnerdQ/backend-AI-company.git
```

This command downloads the project files to your computer.

## Setting Up the Project

1. Navigate to the project directory:

```sh
cd backend-AI-company
```

2. Create a virtual environment to manage dependencies:

```sh
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```sh
venv\Scripts\activate
```

- On macOS/Linux:

```sh
source venv/bin/activate
```

4. Install the necessary dependencies:

```sh
pip install -r requirements.txt
```

## Running the Project

1. Start the FastAPI server:

```sh
uvicorn main:app --reload
```

2. After running the above command, the server will start, and you can access the API documentation by opening your web browser and going to [http://localhost:8000/docs](http://localhost:8000/docs).

## Conclusion

That's it! You now have the backend of the AI company running on your computer. If you encounter any issues, feel free to reach out for help. Enjoy exploring the project!
