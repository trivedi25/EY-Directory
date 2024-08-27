from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)


# Connection string
connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=rahultrivediproject.database.windows.net;'
    'DATABASE=azure_sql_project;'
    'UID=;'
    'PWD='
)

# Connect to the database
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_entry = request.form['text']
        
        # Insert text into database
        cursor.execute("INSERT INTO TextEntries (TextEntry) VALUES (?)", text_entry)
        conn.commit()

        return "Text added to the database successfully!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
