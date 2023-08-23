# Nessus Compliance Check Parser

This Python script extracts information from HTML Report using regular expressions. It specifically targets sections marked by certain HTML classes, such as Info, Solution, and Hosts. The extracted data is then saved in a JSON format.

## Usage

1. Clone this repository.
2. Place your HTML files in the same directory as the script.
3. Update the `html_file_path` variable in the script with the name of your HTML file.
4. Run the script using Python 3.x.

## Script Features

- Extracts and cleans up HTML content using regular expressions.
- Handles potential errors, such as IndexError during extraction.
- Stores extracted data in a structured JSON format.
- Provides clear feedback on successful execution and result file location.

## Important Note

Using regular expressions to parse HTML content might not cover all cases accurately due to HTML's complexity. Consider using a dedicated HTML parsing library like BeautifulSoup for more reliable extraction.


I may update it later to use bs4 instead, but for now, this does the job ! 

Feel free to contribute to the project or report any issues.

Happy auditing!
