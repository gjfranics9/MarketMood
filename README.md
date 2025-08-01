#MarketMood

MarketMood is a real-time sentiment analyser for public news headlines, allowing you to gauge up-to-date sentiment on your favourite topics, people, or companies.

##**Features**

Analyse current sentiment from news headlines (and extendable to tweets)
Clean web interface using Flask
Displays headline summaries with sentiment scores (positive, neutral, negative)

##**Technologies Used**

Python 3
Flask
VADER
Feedparser

##**Setup Instructions**
```
- Clone the repository
- git clone https://github.com/yourusername/marketmood.git
- cd marketmood
- Create and activate virtual environment
- python3 -m venv venv
- source venv/bin/activate  # On Windows use venv\Scripts\activate
- Install requirements
- pip install -r requirements.txt
- Run the Flask app
- export FLASK_APP=app.py
- export FLASK_ENV=development
- flask run
- Then visit http://127.0.0.1:5000/analyse in your browser.
```

##**Project Structure**
```
marketmood/
├── run.py
├── __init__.py
├── frontend/
│   ├── __init__.py
│   ├── mainPage.py
│   └── templates/
│       ├── mainPage.html
│       ├── resultsTemplate.html
│       ├── analysisError.html
│       ├── headlineError.html
│       ├── invalidSearch.html
│       ├── styles.html
│       └── topBar.html
├── marketmood/
│   ├── __init__.py
│   └── googlenews/
│       ├── __init__.py
│       ├── runAnalysis.py
│       ├── analyser.py
│       └── scraper.py
└── README.md
```

##**Currently working on:**

Adding a page that tests for internet connection when run - a "No connection" page

##**Future Improvements**

Integrate Twitter API for live tweet sentiment
Add database storage for analysed results
Deploy on Heroku / Render with custom domain
Enhance UI with Bootstrap or Tailwind
Add graphics to show sentiment over time
Have a list that tracks the same words daily


##**Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.

##**License**

MIT

Created by George Francis – LinkedIn

