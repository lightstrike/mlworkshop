# Machine Learning Django Workshop

## Local Setup
*(this instructions assume a Mac/Linux terminal shell is used)*

1. Clone the project into a local working directory: `git clone https://github.com/lightstrike/mlworkshop.git`
2. Create a python3 virtual environment.
    * Vanilla virtualenv inside the project directory: `virtualenv -p python3 venv`
    * Using virtualenvwrapper: `mkvirtualenv mlworkshop`
3. Install all project Python packages: `pip install -r requirements.txt`
4. Create the Django database: `python manage.py migrate`
5. Create a superuser to access the admin: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`
7. Go to `http://localhost:8000` and `http://localhost:8000/admin` to start exploring. Remember to upload a [valid CSV file](https://www.cms.gov/research-statistics-data-and-systems/statistics-trends-and-reports/bsapufs/chronic_conditions_puf.html).
