from flask import Flask, request, url_for, redirect, make_response
from marketmood.googlenews import runAnalysis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getDataFromUser():
    result_html = ""
    
    if 'clear' in request.form:
            return redirect(url_for('getDataFromUser'))

    if request.method == 'POST':
        stored_data = request.form.get('user_input', '')
        try:
            if stored_data.strip() == "":
                result_html = "<p class='error'>Please enter a valid search term.</p>"
            else:
                analysis = runAnalysis.run_analysis(stored_data)
                if analysis and analysis[0]:
                    headline_results_table = "<br><br>".join(
                        f"<strong>Headline:</strong> {analysis[0][i]}<br><strong>Sentiment:</strong> {analysis[1][i]}"
                        for i in range(len(analysis[0]))
                    )
                    result_html = f'''
                        <div class="results">
                            <h3>Analysis Results for: <em>{stored_data}</em></h3>
                            {headline_results_table}
                        </div>
                    '''
                else:
                    result_html = f"<div class='results'><p>No headlines found for: <em>{stored_data}</em></p></div>"
        except Exception as e:
            result_html = f"<p class='error'>Error during analysis: {e}</p>"

    result_html = f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                padding: 30px;
                color: #333;
            }}
            form {{
                background: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                max-width: 500px;
                margin: auto;
            }}
            input[type="text"] {{
                width: 80%;
                padding: 10px;
                margin-right: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }}
            input[type="submit"] {{
                padding: 10px 15px;
                background-color: #4CAF50;
                border: none;
                color: white;
                border-radius: 4px;
                cursor: pointer;
            }}
            input[type="submit"]:hover {{
                background-color: #45a049;
            }}
            .results {{
                background: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: 20px auto;
            }}
            .error {{
                color: red;
                text-align: center;
            }}
            .button-group {{
                display: flex;
                gap: 10px;
                margin-top: 10px;
            }}

            input[type="submit"] {{
                padding: 10px 15px;
                background-color: #4CAF50;
                border: none;
                color: white;
                border-radius: 4px;
                cursor: pointer;
            }}

            input[type="submit"]:hover {{
                background-color: #45a049;
            }}

            button.clear {{
                padding: 10px 15px;
                background-color: #f44336;
                border: none;
                color: white;
                border-radius: 4px;
                cursor: pointer;
            }}

            button.clear:hover {{
                background-color: #d32f2f;
            }}

        </style>
    </head>
    <body>
        <form method="POST">
        <input type="text" name="user_input" placeholder="Enter something" required>
        <div class="button-group">
            <input type="submit" value="Submit">
            <button type="button" onclick="window.location.href='/'" class="clear">Clear</button>
        </div>
        </form>
        {result_html}
    </body>
    </html>
    '''
    response = make_response(result_html)
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response