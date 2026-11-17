# First API - FastAPI Project

## 1. Create Virtual Environment
#### Windows
```bash
python -m venv env
```
#### Linux
```bash
python3 -m venv env
```


## 2. Activate Virtual Environment
#### Windows
```bash
env\Scripts\activate
```
#### Linux
```bash
source env/bin/activate
```
- Check
```bash
which python
```


## 3. Deactivate Virtual Environment
```bash
deactivate
```


## 4. Upgrade PIP
#### Windows
```bash
python.exe -m pip install --upgrade pip
```
#### Linux
```bash
python -m pip install --upgrade pip
```


## 5. Install Packages
```bash
python -m pip install fastapi uvicorn
```


## 6. Install from Requirements File
```bash
pip install -r requirements.txt
```


## 7. Run the Server
```bash
uvicorn main:app --reload
```
or,
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- `main` = file name (main.py)
- `app` = FastAPI instance name
- `--host 0.0.0.0` = accessible from all IPs
- `--port 8000` = runs on port 8000
- `--reload` = auto restart on code changes


## 8. API Documentation
After running the server, visit:

| URL | Description |
|-----|-------------|
| http://127.0.0.1:8000 | Home |
| http://127.0.0.1:8000/docs | Swagger UI (Interactive API Docs) |
| http://127.0.0.1:8000/redoc | ReDoc (Alternative API Docs) |
