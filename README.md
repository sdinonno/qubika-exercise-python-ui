# qubika-exercise-python-ui

# Preconditions
1. You need to install Python 3.10 or higher
2. Clone this project and create a virtual environment
3. Install depencies from requirements.txt

## How to run the tests
1. Set browser in the file config.json 
2. You can run the test from your favourite IDE :)
3. Run from terminal:  python3 -m pytest tests/test_search.py

## Solution
- Applied POM to order the code better 
- Applied page factory to easily initialize elements
- Created an util called file to open and get a value from a json file
- config.json file contains base configurations to start the execution

## Disclaimer
- I changed 'teting' to 'teesting' as the first option did not yield suggestions.
- When clicking on the suggestion, the url is not updated and neither does the attribute "value" in the element. So I decided to take the suggestion link and open it in a new tab. In this way it was possible to validate that the url and the text area correctly contain the new value.
- The test fails at the end, I faced some issues to validate it was selected.

## Next steps (improvements)
- Include the test data in a file (.json for example) or parameterize the execution with pytest
- Improve the locator for the images button. In case the search is performed in another language the word will not be found in Spanish and therefore it will not be possible to find the element.
- Improve the get_result_title() method so that you can return the title of any of the results.
- Add support for Firefox and other browsers
- Implement a report.
- Add GitHub Actions workflow

