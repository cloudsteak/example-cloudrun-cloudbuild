import os
from flask import Flask
from fastapi.middleware.cors import CORSMiddleware

app = Flask(__name__)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

@app.route('/')
def hello_world():
    return 'Helló Világ! Ez egy Cloud Run alkalmazás, Cloud Build segítségével telepítve. Tényleg egyszerű példa.'

if __name__ == "__main__":
    # A Cloud Run a PORT környezeti változóban adja meg a portot.
    port = int(os.environ.get('PORT', 8080))
    # Ne használd a debug=True-t éles környezetben!
    app.run(host='0.0.0.0', port=port)