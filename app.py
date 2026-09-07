```python
from flask import Flask

app = Flask(__name__)

def greet():
    return "Hello from Jenkins webhook CI/CD!"

@app.route("/")
def home():
    return greet()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
