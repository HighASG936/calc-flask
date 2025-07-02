# Calc Flask Microservices

Flask microservices that perform basic math operations: addition, subtraction, multiplication, and division. Deployed on Railway.

## Endpoints

### ➕ Addition

GET /adder/<a>/<b>

* Returns the sum of `a` and `b`.

Example:

```
curl https://calc-flask-production.up.railway.app/adder/2/5
```

Response:

```
2 + 5 = 7.0
```

---

### ➖ Subtraction

GET /subtractor/<a>/<b>

* Returns the result of `a` minus `b`.

Example:

```
curl https://calc-flask-production.up.railway.app/subtractor/10/4
```

Response:

```
10.0 - 4.0 = 6.0
```

---

### ✖️ Multiplication

GET /multiplier/<a>/<b>

* Returns the product of `a` and `b`.

Example:

```
curl https://calc-flask-production.up.railway.app/multiplier/3/7
```

Response:

```
3.0 * 7.0 = 21.0
```

---

### ➗ Division

GET /divider/<a>/<b>

* Returns the result of dividing `a` by `b`.
* Handles division by zero with an error message.

Valid Example:

```
curl https://calc-flask-production.up.railway.app/divider/20/4
```

Response:

```
20.0 / 4.0 = 5.0
```

Division by zero example:

```
curl https://calc-flask-production.up.railway.app/divider/20/0
```

Response:

```
Cannot Do Zero Division
```

---

## How to Run Locally

1. Clone the repository:

```
git clone https://github.com/HighASG936/calc-flask.git
cd calc-flask
```

2. Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the server:

```
python app.py
```

5. Test endpoints locally, e.g.:

```
curl http://127.0.0.1:8080/adder/2/5
```

Response:

```
2 + 5 = 7.0
```

---

## Project Structure

```
calc-flask/
│
├── app.py
├── requirements.txt
└── microservices/
    ├── __init__.py
    ├── adder.py
    ├── subtractor.py
    ├── multiplier.py
    └── divider.py
```

---

## Deployment

This project is deployed on Railway:

```
https://calc-flask-production.up.railway.app
```

---

## Available Routes

* /adder/<a>/<b>
* /subtractor/<a>/<b>
* /multiplier/<a>/<b>
* /divider/<a>/<b>

---
