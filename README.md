# AUTO TYPE KEYBOARD - TEXT

## overview
This is a desktop application that autocomplete the keyboard typing. Created using PyQT5 and Python

## Project Structure

AutoTypeKeyboard_Text/<br>
│<br>
├─ app/<br>
│  ├─ resources/<br>
│  │  └─ images/<br>
│  │    └─ logo-decalltect00.png<br>
│  ├─ ui/<br>
│  │  └─ autoTypedKeyboardtext.ui<br>
│  ├─ __init__.py<br>
│  ├─ const.py<br>
│  ├─ gui.py<br>
│  └─ main.py<br>
├─ docs/<br>
├─ test/<br>
├─ .gitignore<br>
├─ LICENSE<br>
├─ README.md<br>
└─ requirements.txt<br>

## Features
- Open files using a file doalog
- Automate fill the file contents on the text input field
- Periodically update UI elements using QTimer

## Prerequisites
- Python 3.x
- PyQt5
- keyboard

## Installation
1. **Clone the repository**
    ```bash
    git clone {repository url}
2. **Create and activate virtual environment**
    ```bash
    python -m venv env
    # On Windows use
    env\Scripts\activate
    # On MacOS use
    source env/bin/activate
3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt

## Running the Application
To run the application, execute the `main.py` file from the root directory:

    python app/main.py

## Using the application
1. **Open the application**
   Run the executable generated in the previous step, or run `python app/main.py`
2. Interact with the UI
   - Click the "Choose File" button to open a file dialog and select a file.
   - The selected file's content will be displayed in the application specifically on `text input field`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like. `Contribution are welcome! Please create an issue or submit a pull request`

## License
This project is licensed under the MIT License. See the
[MIT](https://choosealicense.com/licenses/mit/) file for details

## Contact
For any inquiries, please contact rizkypffdev37@gmail.com