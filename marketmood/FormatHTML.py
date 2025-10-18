from flask import render_template

def formatPageHTML(page_content):
    final_html = """
    """
    final_html += page_content
    final_html += render_template('topBar.html')
    final_html += render_template('styles.html')
    return final_html