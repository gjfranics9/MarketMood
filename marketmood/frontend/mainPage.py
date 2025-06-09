from flask import Flask
from marketmood.googlenews import runAnalysis


app = Flask(__name__)


@app.route('/')
def inial_page():
    bitcoin_analysis = runAnalysis.run_analysis("bitcoin")
    headline_results_table = "<br>".join(
    f"Headline: {bitcoin_analysis[0][i]}<br>Sentiment: {bitcoin_analysis[1][i]}"
    for i in range(len(bitcoin_analysis[0]))
    )
    return headline_results_table


