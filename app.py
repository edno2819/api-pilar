import os
from src import create_app

app = create_app()

if __name__ == "__main__":
    debug = True if os.environ.get("DEBUG", False) == "true" else False
    app.run(debug=debug, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
