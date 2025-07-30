from flask import Flask
import marketmood.frontend.AnalysisPage as AnalysisPage
import marketmood.frontend.HomePage as HomePage

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def runProgramHome():
    return HomePage.homePage()

@app.route('/analyse', methods=['GET', 'POST'])
def runProgramAnalysis():
    return AnalysisPage.analysisPage()
    
