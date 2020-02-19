import sys

sys.path.insert(0, "./src")

from api import app  # noqa: E402


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
