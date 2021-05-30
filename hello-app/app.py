import os
import json

from flask import Flask, request

app = Flask(__name__)
config = {
    "DATABASE_URI": os.environ.get("DATABASE_URI", ""),
    "HOSTNAME": os.environ["HOSTNAME"],
    "GREETING": os.environ.get("GREETING", "Hello")
}

@app.route("/")
def hello():
    return config["GREETING"] + " from " + config["HOSTNAME"] + "!"

@app.route("/config")
def configuration():
    return json.dumps(config)

@app.route("/version")
def version():
    return {"version": "1.0.0"}

@app.route("/db")
def df():
    from sqlalchemy import create_engine

    engine = create_engine(config["DATABASE_URI"], echo=True)
    rows = []

    with engine.connect() as connection:
        result = connection.execute("select id, name from users")
        rows = [dict(r.items()) for r in result]

    return json.dumps(rows)


@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == "GET":
        from sqlalchemy import create_engine

        engine = create_engine(config["DATABASE_URI"].strip(), echo=True)
        rows = []

        with engine.connect() as connection:
            result = connection.execute("select id, name from users")
            rows = [dict(r.items()) for r in result]

        return json.dumps(rows)
    else:
        body = request.json
        id = int(body["id"])
        name = str(body["name"])
        from sqlalchemy import create_engine

        engine = create_engine(config["DATABASE_URI"].strip(), echo=True)
        rows = []

        with engine.connect() as connection:
            result = connection.execute(f"insert into users(id, name) values({str(id)}, '{name}')")
            print(result)

        return {"status": "ok"}


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=80, debug=True)