from flask import request, url_for, redirect, render_template
from marketmood.frontend.FormatHTML import formatPageHTML
from marketmood.googlenews import runAnalysis


def analysisPage():
    
    if 'clear' in request.form:
        return redirect(url_for('analysisPage'))

    if request.method == 'POST':
        stored_data = request.form.get('user_input', '')
        return find_results_from_api(stored_data)
    
    template = render_template('analysisPage.html')
    return formatPageHTML(template)
    
def format_analysis_results_as_list(analysis):
    results = []
    for headline, sentiment in zip(analysis[0], analysis[1]):
        results.append({
            'headline': headline,
            'sentiment': sentiment
        })
    return results



def find_results_from_api(stored_data):
    result_html = ""
    template = ""
    
    try:
        if stored_data.strip() != "":
            analysis = runAnalysis.run_analysis(stored_data)
            print(stored_data)
            if analysis and analysis[0]:
                results = format_analysis_results_as_list(analysis)
                template = render_template('dataSummary.html', Sentiment="Positive", Score=0)
                template1 = render_template('resultsTemplate.html', stored_data=stored_data, results=results)
                result_html = formatPageHTML(template)
                result_html += formatPageHTML(template1)
            else:
                template = render_template('headlineError.html', keyword=stored_data)
                result_html = formatPageHTML(template)     
        else:
            template = render_template('invalidSearch.html')
            result_html = formatPageHTML(template)
    except Exception as e:
        template = render_template('analysisError.html', error=str(e))
        result_html = formatPageHTML(template)

    template = render_template('analysisPage.html', result_html=result_html)
    return formatPageHTML(template)