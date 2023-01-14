# GVSU sports analytics web app
`http://gvsac.pythonanywhere.com/`

### Run Locally Without Dockerfile
`git clone https://github.com/GVSU-Sports-Analytics/Web-App` <br>
`pip3 install -r requirements.txt` <br>
`gunicorn --bind :3000 --workers 1 --threads 8 --timeout 0 app:app`

### Run Locally With Docker
``
