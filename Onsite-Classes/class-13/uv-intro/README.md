# About `main.py`

The `main.py` file demonstrates basic Object-Oriented Programming (OOP) concepts in Python using a `Car` class.

## `Car` Class

The `Car` class is defined with the following attributes and methods:

### Attributes

-   `name`: The name of the car (e.g., "G-Wagon").
-   `model`: The model of the car (e.g., "G63").
-   `year`: The manufacturing year of the car.
-   `color`: The color of the car.
-   `__price`: A private attribute for the car's price, demonstrating encapsulation.

### Methods

-   `__init__(self, name, model, year, color)`: The constructor to initialize a new `Car` object.
-   `display_info(self)`: Prints the car's details.
-   `get_price(self)`: A getter method to access the private `__price` attribute.
-   `set_price(self)`: A setter method to modify the private `__price` attribute.

The script then creates several instances of the `Car` class and demonstrates the use of its methods.

# What is `uv`?

`uv` is an extremely fast Python package installer and resolver, written in Rust. It is designed to be a drop-in replacement for `pip` and `pip-tools`, offering a significant speed improvement for installing and managing Python packages.

# `uv` Installation and Usage

Here are the basic commands to get started with `uv`:

## Installation

-   `pip install uv` (only needs to be done once)

## Project Setup

1.  **Initialize a new project:**
    ```bash
    uv init
    ```
2.  **Create a virtual environment:**
    ```bash
    uv venv
    ```
3.  **Activate the virtual environment:**
    -   On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
4.  **Install packages:**
    ```bash
    uv pip install <package-name>
    ```
    For example:
    ```bash
    uv pip install rich
    ```