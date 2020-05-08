# clustering-demo
Build a web app to demo clustering results

### Local setup
```
python3 -m venv venv
source venv/bin/activate.fish
poetry install
sh setup.sh
```

### Run app
```
streamlit run app.py
```

#### Preparing data
- Download metadata and embeddings from https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/#metadata.csv
- Run script: `python prepare_data.py`


#### Useful commands
```
poetry show -v
poetry export -f requirements.txt > requirements.txt
heroku logs -a clustering-demo --tail
```
