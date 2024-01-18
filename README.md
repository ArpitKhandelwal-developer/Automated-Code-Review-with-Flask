# Automated Code Review with Flask

This project leverages Flask to create a simple web application for automated code review. Users can submit code snippets for review, and an AI-based logic (placeholder for actual implementation) provides feedback.

## Project Structure

- **main.py:** The Flask application file containing routes and logic.
- **templates/index.html:** HTML template for the homepage.
- **templates/review_result.html:** HTML template for displaying code review results.

## How to Run

1. Ensure you have Python and Flask installed.
   ```bash
   pip install Flask
   ```

2. Run the Flask application.
   ```bash
   python main.py
   ```

3. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. Enter your code in the provided textarea on the homepage.
2. Click the "Review Code" button.
3. View the code review result, including the original code and feedback.
4. Use the "Go back" link to return to the homepage.

## AI-based Code Review Logic

The AI-based code review logic in `review_code_with_ai` currently checks for the presence of the word "bug" in the code. Replace this logic with your actual AI-based code review implementation.

Feel free to customize the templates, add more sophisticated code review logic, or integrate with external services.

**Note:** This is a basic template, and the actual AI-based code review logic should be tailored to your specific requirements.

## Contributions

Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).
