# TOPSIS Decision Tool - Arush-102303889

[![PyPI Version](https://img.shields.io/pypi/v/topsis-arush-102303889.svg)](https://pypi.org/project/topsis-arush-102303889/)

A comprehensive TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) implementation for multi-criteria decision making.

## 📦 Official Package

The package is published on PyPI: https://pypi.org/project/topsis-arush-102303889/

## 🚀 Installation

```bash
pip install topsis-arush-102303889
```

## 📋 Features

- Multi-criteria decision making using TOPSIS method
- Web interface for easy file upload and analysis
- Email functionality to send results
- Supports CSV input files
- Calculates TOPSIS scores and ranks alternatives

## 🎯 What is TOPSIS?

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a decision-making method that helps rank alternatives based on their similarity to the ideal solution.

## 💻 Project Structure

- **Topsis-Arush-102303889/** - Main package directory
  - `topsis.py` - Core TOPSIS implementation
  - `setup.py` - Package configuration
  - `README.md` - Package documentation

- **topsis_web/** - Flask web application
  - `app.py` - Main Flask application
  - `templates/` - HTML templates
  - `topsis.py` - TOPSIS logic for web app

## 🌐 Web Interface

The project includes a Flask-based web application for easy TOPSIS analysis:

```bash
cd topsis_web
pip install -r requirements.txt
SENDER_PASSWORD="your-gmail-app-password" python3 app.py
```

Then visit: `http://localhost:5000`

### Features:
- Upload CSV file with criteria data
- Specify weights for each criterion
- Define impacts (+ for benefit, - for cost)
- Get TOPSIS scores and rankings
- Receive results via email

## 📊 Example Usage

### Command Line:
```bash
topsis input.csv "0.25,0.25,0.25,0.25" "+,-,+,+" output.csv
```

### Python:
```python
from topsis import topsis

topsis("input.csv", [0.25, 0.25, 0.25, 0.25], ['+', '-', '+', '+'], "output.csv")
```

## 📝 Input Format

Your CSV file should have:
- First column: Alternative names (e.g., Product names)
- Remaining columns: Criteria values (numeric)

Example:
```
Phone,Price,RAM,ROM,Processor
A1,20000,4,128,8
A2,25000,6,256,9
A3,30000,8,512,10
```

## 📧 Email Setup

To use the email functionality:

1. Enable 2-Step Verification on your Gmail account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Set environment variable: `export SENDER_PASSWORD="your-16-char-password"`

## 🔒 Security

- No hardcoded credentials
- Sensitive data uses environment variables
- Email password never stored in code

## 👨‍💻 Author

**Arush Singhal** (102303889)

## 📄 License

See LICENSE file for details

## 🤝 Contributing

This is an academic assignment. For questions or improvements, feel free to open an issue!

## 🔗 Links

- GitHub: https://github.com/arushsinghal/DS-Topsis
- PyPI: https://pypi.org/project/topsis-arush-102303889/
