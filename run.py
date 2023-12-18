import os
from waitress import serve
from app import app

if __name__ == "__main__":
    # Check if the environment variable FLASK_ENV is set to 'development'
    if os.environ.get('FLASK_ENV') == 'development':
        # Run the development server
        app.run(debug=True)
    else:
        # Run Waitress in production mode
        serve(app, host="127.0.0.1", port=5000)
