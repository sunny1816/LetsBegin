from flask import Flask, send_from_directory
import subprocess
import os

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'templates/index.html')

# Route to execute the C++ program
@app.route('/run_cpp', methods=['GET'])
def run_cpp():
    try:
        # Path to your compiled C++ executable
        program_path = 'static/urlurl.exe'

        # Check if the file exists and is executable
        if not os.path.isfile(program_path) or not os.access(program_path, os.X_OK):
            return "Error: Executable not found or not executable", 500

        result = subprocess.run([program_path], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr}", 500
        return result.stdout  # Output from the C++ program
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
