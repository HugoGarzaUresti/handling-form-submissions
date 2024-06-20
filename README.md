# Handling Form Submission

This guide demonstrates how to handle form submissions in a Flask application. It includes a simple web form where users can enter their name. Upon submission, the form data is processed and displayed on a results page.

## Requirements

- Python 3.x
- `Flask` library
- `Flask-WTF` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000/` to see the form.

## Code Explanation

### `forms.py`

This module contains the form definition using `Flask-WTF`.

- **`NameForm`**: A form with a single name field and a submit button.

### `routes.py`

This module contains the route handlers for the Flask application.

- **`form`**: Handles the display and submission of the form.
- **`result`**: Displays the result page with the submitted name.

### `form.html`

This template renders the form for user input.

### `result.html`

This template displays the result page with the submitted name.

### `run.py`

This script serves as the entry point for the application.

## Additional Information

- Ensure you set a secret key for CSRF protection in Flask.
- You can customize the form and result templates as needed.
