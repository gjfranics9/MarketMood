from flask import render_template
from marketmood.frontend.FormatHTML import formatPageHTML

def homePage():
    
    template = render_template('pages/homePage.html')
    
    return formatPageHTML(template)