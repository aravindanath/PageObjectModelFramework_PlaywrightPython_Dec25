# PageObjectModelFramework_Playwright

A robust, maintainable, and scalable Playwright-based Python test automation framework using the Page Object Model (POM) design pattern. This framework supports:
- Modular page objects
- Pytest for test execution
- HTML and Allure reporting (with screenshots on failure)
- Easy dependency management

## Project Structure

```
PageObjectModelFramework_Playwright/
├── pages/                # Page Object Model classes
│   ├── __init__.py
│   ├── BasePage.py
│   ├── LoginPage.py
│   └── AdminPage.py
├── tests/                # Test cases and configuration
│   ├── __init__.py
│   ├── conftest.py       # Pytest fixtures and hooks (HTML/Allure screenshot integration)
│   ├── test_001.py
│   ├── test_002.py
│   ├── test_003.py
│   ├── test_004.py
│   └── assets/           # Static assets (e.g., CSS)
│       └── style.css
├── requirements.txt      # All required Python dependencies
├── Command               # Quick reference for setup and execution commands
└── README.md             # (This file)
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repo-url>
cd PageObjectModelFramework_Playwright
```

### 2. Create and Activate a Virtual Environment (Recommended)
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies
```sh
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```sh
playwright install
```

### 5. (Optional) Install Allure Command-Line Tool
- **macOS (Homebrew):**
  ```sh
  brew install allure
  ```
- **Windows:**
  Download from https://docs.qameta.io/allure/

## Running Tests

### Basic Test Run with HTML Report
```sh
pytest --maxfail=1 --disable-warnings -q --html=report.html --log-level=INFO
```
Or
```sh
pytest --html=report.html --log-level=INFO
```

### Run Tests with Allure Reporting
```sh
pytest --maxfail=1 --disable-warnings -q --html=report.html --log-level=INFO --alluredir=allure-results
```

### Generate and View Allure Report
```sh
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Features
- **Page Object Model:** All page interactions are encapsulated in `pages/`.
- **Logging:** All steps are logged for traceability.
- **Screenshots on Failure:** Automatically attached to both HTML and Allure reports.
- **Pytest Fixtures:** Centralized browser/page management in `conftest.py`.
- **Easy Dependency Management:** All requirements in `requirements.txt`.

## Adding New Tests
- Create new test files in `tests/` (e.g., `test_005.py`).
- Use existing page objects or add new ones in `pages/` as needed.

## Troubleshooting
- Ensure all dependencies are installed and the virtual environment is activated.
- If browsers are missing, run `playwright install` again.
- For Allure, ensure the CLI is installed and available in your PATH.

## Quick Reference (see `Command` file)
```
pip install -r requirements.txt
playwright install
pytest --maxfail=1 --disable-warnings -q --html=report.html --log-level=INFO --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
```

---

**Author:** Aravindanath


