from flask import Flask
from app import create_app


app = create_app()


@app.route("/test")
def test():
    return {"message": "Test route works!"}

if __name__ == "__main__":
    app.run(debug=True)
