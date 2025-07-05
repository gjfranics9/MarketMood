from flask import Flask, request, url_for, redirect, render_template
from marketmood.googlenews import runAnalysis


app = Flask(__name__)

@app.route('/analyse', methods=['GET', 'POST'])
def getDataFromUser():
    
    if 'clear' in request.form:
            return redirect(url_for('getDataFromUser'))

    if request.method == 'POST':
        stored_data = request.form.get('user_input', '')
        return find_results_from_api(stored_data)
    
    template = render_template('mainPage.html')
    return formatPageHTML(template)
    
def format_analysis_results_as_list(analysis):
    results = []
    for headline, sentiment in zip(analysis[0], analysis[1]):
        results.append({
            'headline': headline,
            'sentiment': sentiment
        })
    return results

def formatPageHTML(page_content):
    final_html = """
    """
    final_html += page_content
    final_html += render_template('topBar.html')
    final_html += render_template('styles.html')
    return final_html

def find_results_from_api(stored_data):
    result_html = ""
    template = ""
    
    try:
            if stored_data.strip() == "":
                template = render_template('invalidSearch.html')
                result_html = formatPageHTML(template)
            else:
                analysis = runAnalysis.run_analysis(stored_data)
                print(stored_data)
                if analysis and analysis[0]:
                    results = format_analysis_results_as_list(analysis)
                    template = render_template('resultsTemplate.html', stored_data=stored_data, results=results)
                    result_html = formatPageHTML(template)
                else:
                    template = render_template('headlineError.html', keyword=stored_data)
                    result_html = formatPageHTML(template)
    except Exception as e:
        template = render_template('analysisError.html', error=str(e))
        result_html = formatPageHTML(template)


    template = render_template('mainPage.html', result_html=result_html)
    return formatPageHTML(template)