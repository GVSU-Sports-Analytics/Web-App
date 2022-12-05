# GVSU sports analytics web app

### Run Locally
1. pip3 install -r requirements.txt <br>
2. gunicorn --bind :3000 --workers 1 --threads 8 --timeout 0 app:app
