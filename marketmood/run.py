import os
from flask import Flask
import HomePage
import AnalysisPage

BASE_DIR = os.path.dirname(__file__)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/", methods=["GET", "POST"])
def runProgramHome():
    return HomePage.homePage()

@app.route("/analyse", methods=["GET", "POST"])
def runProgramAnalysis():
    return AnalysisPage.analysisPage()

if __name__ == "__main__":
    app.run(debug=True)
