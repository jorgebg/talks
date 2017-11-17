# Setup

```bash
cd project
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations blog
./manage.py migrate
./manage.py shell_plus
```

# Example queries

Check `queries.py` and run the queries in the django shell
