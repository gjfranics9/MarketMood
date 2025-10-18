from flask import render_template
from FormatHTML import formatPageHTML

def homePage():
    html = render_template("pages/homePage.html")
    return formatPageHTML(html)
