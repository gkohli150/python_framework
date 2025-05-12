

# Playwright Pytest Test Automation Framework

## 📌 Overview
This repository contains an end-to-end test automation framework built using [Playwright](https://playwright.dev/python/) and [Pytest](https://docs.pytest.org/en/latest/) for web application testing. The framework is designed to be scalable, maintainable, and easy to use, providing robust automation capabilities.

## 🚀 Features
- **Cross-Browser Testing**: Supports Chrome, Firefox
- **Headless & Headed Mode Execution**
- **Parallel Test Execution** using Pytest-xdist
- **Fixtures for Setup & Teardown**
- **Page Object Model (POM) Structure** for better maintainability
- **Environment-based Configurations**
- **CI/CD Ready**: Can be integrated with Jenkins/GitHub Actions


## 🛠 Installation & Setup
### Prerequisites
Ensure you have Python 3.7+ installed.

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Install Playwright Browsers
```bash
playwright install
```

## 🚦 Running Tests
### Run All Tests
```bash
pytest
```

### Run Tests in Headless Mode
```bash
pytest --headed=false
```

### Run Tests in Parallel
```bash
pytest -n 4  # Runs tests in 4 parallel threads
```

