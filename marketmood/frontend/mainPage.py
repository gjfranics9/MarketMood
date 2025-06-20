from flask import Flask, request, url_for, redirect, render_template
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
                print(stored_data)
                if analysis and analysis[0]:
                    headline_results_list = "<br><br>".join(
                        f"<strong>Headline:</strong> {analysis[0][i]}<br><strong>Sentiment:</strong> {analysis[1][i]}"
                        for i in range(len(analysis[0]))
                    )

                    result_html = f'''
                        <div class="results">
                            <details>
                                <summary><strong>Results for:</strong> <em>{stored_data}</em></summary>
                                <div style="margin-left: 20px; padding-top: 10px;">
                                    {headline_results_list}
                                </div>
                            </details>
                        </div>
                    '''



                else:
                    result_html = f"<div class='results'><p>No headlines found for: <em>{stored_data}</em></p></div>"
        except Exception as e:
            result_html = f"<p class='error'>Error during analysis: {e}</p>"


    return render_template('mainPage.html', result_html=result_html)