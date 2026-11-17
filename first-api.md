# Python First API Project - Step by Step Guide

## Step 1: Python Install আছে কিনা Check করো

Terminal/CMD open করো এবং run করো:

```bash
python --version
```

যদি Python version দেখায় (e.g., `Python 3.10.x`), তাহলে ঠিক আছে।
যদি না দেখায়, তাহলে [python.org](https://www.python.org/downloads/) থেকে download করে install করো।

---

## Step 2: Project Folder তৈরি করো

```bash
mkdir first-api
cd first-api
```

---

## Step 3: Virtual Environment তৈরি করো

Virtual environment হলো তোমার project এর জন্য আলাদা একটা Python environment, যাতে অন্য project এর সাথে conflict না হয়।

```bash
python -m venv venv
```

### Activate করো:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

Activate হলে terminal এ `(venv)` দেখাবে।

---

## Step 4: FastAPI ও Uvicorn Install করো

FastAPI হলো Python এর একটা modern, fast web framework যেটা দিয়ে API বানানো যায়।
Uvicorn হলো server যেটা তোমার API run করবে।

```bash
pip install fastapi uvicorn
```
or,
```bash
python -m pip install fastapi uvicorn
```

---

## Step 5: Main File তৈরি করো

`main.py` নামে একটা file তৈরি করো:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, World! This is my first API!"}


@app.get("/about")
def about():
    return {
        "name": "My First API",
        "version": "1.0.0",
        "description": "This is my first API built with FastAPI"
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to my API!"}
```

### Code Explanation:

- `FastAPI()` - এটা তোমার app তৈরি করে
- `@app.get("/")` - এটা একটা GET route define করে। Browser এ `/` এ গেলে এই function run হবে
- `@app.get("/greet/{name}")` - এখানে `{name}` হলো dynamic parameter। URL এ যেকোনো নাম দিলে সেটা receive করবে

---

## Step 6: Server Run করো

```bash
uvicorn main:app --reload
```

- `main` = তোমার file এর নাম (main.py)
- `app` = FastAPI() instance এর নাম
- `--reload` = code change করলে auto restart হবে

Terminal এ এরকম দেখাবে:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## Step 7: Browser এ Test করো

Browser open করে এই URLs গুলো visit করো:

| URL | কী হবে |
|-----|--------|
| `http://127.0.0.1:8000/` | Home page - Hello World message দেখাবে |
| `http://127.0.0.1:8000/about` | About info দেখাবে |
| `http://127.0.0.1:8000/greet/Rakib` | "Hello, Rakib!" message দেখাবে |
| `http://127.0.0.1:8000/docs` | Swagger UI - interactive API documentation |

> **Swagger UI** (`/docs`) হলো FastAPI এর সবচেয়ে useful feature। এখানে তুমি directly browser থেকে তোমার API test করতে পারবে।

---

## Step 8: POST Request যোগ করো

এখন data receive করার জন্য POST endpoint যোগ করো। `main.py` update করো:

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Data model define করো
class Item(BaseModel):
    name: str
    price: float
    description: str = None  # Optional field


# In-memory storage (simple list)
items = []


@app.get("/")
def home():
    return {"message": "Hello, World! This is my first API!"}


@app.get("/items")
def get_items():
    return {"items": items}


@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return {"message": "Item created successfully!", "item": item}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found!"}
    return {"item": items[item_id]}
```

### Code Explanation:

- `BaseModel` - Pydantic এর model। এটা data validation করে automatically
- `Item` class - define করে কোন data accept করবে (name, price, description)
- `items = []` - simple in-memory storage। Server restart দিলে data মুছে যাবে
- `@app.post("/items")` - POST request handle করে। নতুন item create করে

---

## Step 9: POST Request Test করো

### Option 1: Swagger UI দিয়ে (`/docs`)

1. Browser এ `http://127.0.0.1:8000/docs` যাও
2. `POST /items` section expand করো
3. "Try it out" button click করো
4. Request body তে লেখো:
```json
{
    "name": "Laptop",
    "price": 50000.00,
    "description": "A gaming laptop"
}
```
5. "Execute" click করো

### Option 2: curl দিয়ে

```bash
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d "{\"name\": \"Laptop\", \"price\": 50000.00, \"description\": \"A gaming laptop\"}"
```

---

## Step 10: Requirements File তৈরি করো

তোমার project এর dependencies save করো, যাতে অন্য কেউ easily setup করতে পারে:

```bash
pip freeze > requirements.txt
```

পরে অন্য কেউ install করতে চাইলে:
```bash
pip install -r requirements.txt
```

---

## Final Project Structure

```
first-api/
├── venv/
├── main.py
└── requirements.txt
```

---

## Quick Reference

| বিষয় | Command |
|-------|---------|
| Venv তৈরি | `python -m venv venv` |
| Venv activate (Windows) | `venv\Scripts\activate` |
| Install packages | `pip install fastapi uvicorn` |
| Server run | `uvicorn main:app --reload` |
| API docs | `http://127.0.0.1:8000/docs` |
| Deactivate venv | `deactivate` |

---

## Next Steps

এই basic API শেখা হলে, পরের ধাপে এগুলো শিখতে পারো:

1. **Database connect করা** - SQLAlchemy বা Tortoise ORM ব্যবহার করে
2. **Authentication** - JWT token দিয়ে user login system
3. **CRUD operations** - Create, Read, Update, Delete পুরোপুরি implement করা
4. **File upload** - Image বা file upload handle করা
5. **Deploy করা** - Render, Railway বা VPS এ deploy করা
