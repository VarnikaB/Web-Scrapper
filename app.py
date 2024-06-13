from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')
        tables_html = [str(table) for table in tables]  # Convert tables to HTML strings
        return render_template('select_table.html', tables=tables_html, url=url, enumerate=enumerate)
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    url = request.form['url']
    table_index = int(request.form['table_index'])
    filetype = request.form['filetype']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
    selected_table = tables[table_index]
    
    # Extract table data
    headers = []
    rows = selected_table.find_all('tr')
    
    # Determine the number of columns
    max_columns = 0
    for row in rows:
        cells = row.find_all(['th', 'td'])
        colspan_count = sum([int(cell.get('colspan', 1)) for cell in cells])
        max_columns = max(max_columns, colspan_count)
    
    # Initialize the grid
    grid = [['' for _ in range(max_columns)] for _ in range(len(rows))]
    
    # Fill the grid with table data
    for row_index, row in enumerate(rows):
        col_index = 0
        for cell in row.find_all(['th', 'td']):
            while grid[row_index][col_index] != '':
                col_index += 1
            cell_text = ' '.join(cell.stripped_strings)
            if cell.find('ul'):
                cell_text = ' '.join(['- ' + li.get_text(strip=True) for li in cell.find_all('li')])
            rowspan = int(cell.get('rowspan', 1))
            colspan = int(cell.get('colspan', 1))
            for r in range(rowspan):
                for c in range(colspan):
                    grid[row_index + r][col_index + c] = cell_text
            col_index += colspan
    
    # Extract headers and data from the grid
    headers = grid[0]
    data = grid[1:]
    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(data, columns=headers if headers else None)
    output = BytesIO()
    if filetype == 'CSV':
        df.to_csv(output, index=False)
        output.seek(0)
        return send_file(output, mimetype='text/csv', as_attachment=True, download_name='extracted_data.csv')
    elif filetype == 'JSON':
        try:
            df.to_json(output, orient='records')
        except:
            return 'Error: Could not convert the table to JSON format. Please try again with a different table or filetype'
        return send_file(output, mimetype='text/csv', as_attachment=True, download_name='extracted_data.json')

if __name__ == '__main__':
    app.run(debug=True)
