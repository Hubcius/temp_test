# temp_test

A simple Python project for testing purposes with a calculator module and comprehensive tests.

## Overview

This repository contains a basic calculator module (`calculator.py`) with four operations:
- Addition
- Subtraction
- Multiplication
- Division

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest test_calculator.py -v
```

Run a specific test class:

```bash
pytest test_calculator.py::TestAdd -v
```

## Usage

```python
from calculator import add, subtract, multiply, divide

# Basic operations
result = add(5, 3)        # 8
result = subtract(10, 4)  # 6
result = multiply(3, 7)   # 21
result = divide(20, 4)    # 5.0
```

## Project Structure

```
temp_test/
├── README.md              # This file
├── calculator.py          # Calculator module with basic operations
├── test_calculator.py     # Comprehensive test suite
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore rules
```