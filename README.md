# Web Scraper with Table Extraction

This project is a web scraper built with Python and Flask that allows users to extract data from HTML tables on a specified webpage. The application handles complex table structures, including cells with `rowspan` and `colspan` attributes, and correctly formats bullet points within table cells. The extracted data can be downloaded as a CSV file.

## Features

- **URL Input:** Users can enter the URL of the webpage containing the table they wish to scrape.
- **Table Selection:** The application displays all tables found on the webpage, allowing users to select which table to extract.
- **Data Handling:** Properly handles `rowspan` and `colspan` attributes to ensure data is correctly aligned in the output CSV.
- **Bullet Points:** Concatenates text from list items within table cells, ensuring bullet points are included in the extracted data.
- **CSV Export:** Extracted data is converted to a pandas DataFrame and saved as a CSV file for download.

## Requirements

- Python 3.x
- Flask
- requests
- BeautifulSoup4
- pandas

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Rishurajgautam24/Web-Scrapper.git
    cd web-scraper
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter the URL of the webpage containing the table you wish to scrape and click "Submit".

4. Select the table you want to extract from the list of displayed tables.

5. Click "Extract" to download the table data as a CSV file.

## Project Structure
```python
web-scraper/
│
├── templates/
│ ├── index.html # HTML template for the URL input page
│ └── select_table.html # HTML template for table selection page
│
├── app.py # Main Flask application
├── requirements.txt # List of required packages
└── README.md # Project description and instructions
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
- Main area of Contribution will be GUI and adding more features to it

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)
