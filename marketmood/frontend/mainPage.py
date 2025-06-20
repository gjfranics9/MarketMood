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
                result_html = render_template('invalidSearch.html')
            else:
                analysis = runAnalysis.run_analysis(stored_data)
                print(stored_data)
                if analysis and analysis[0]:
                    headline_results_list = "<br><br>".join(
                        f"<strong>Headline:</strong> {analysis[0][i]}<br><strong>Sentiment:</strong> {analysis[1][i]}"
                        for i in range(len(analysis[0]))
                    )
                    result_html = render_template('resultsTemplate.html', stored_data=stored_data, headline_results_list=headline_results_list)
                else:
                    result_html = render_template('headlineError.html', keyword=stored_data)
        except Exception as e:
            result_html = render_template('analysisError.html', error=str(e))


    return render_template('mainPage.html', result_html=result_html)