"""
=============================================================================
HARISH KUMAR - PORTFOLIO WEB APPLICATION (FLASK BACKEND)
Education: MCA - Master of Computer Applications (Pursuing) | B.Sc. AI (Completed)
College: Annai College of Arts and Science (Bharathidasan University)
Role: AI & Python Developer | MCA 
Tech Stack: Python, Flask, HTML5, CSS3, JavaScript, SQLite/JSON
=============================================================================
This backend serves the portfolio web application and provides endpoints for:
1. Serving index.html and static assets (CSS, JS, images, PDF)
2. Handling contact form submissions and storing them in data/messages.json
3. Handling file uploads (e.g. resumes for ATS analyzer) into uploads/
4. Serving the resume PDF for download
=============================================================================
"""

import os
import sys
import json
import time
import threading
import webbrowser
from datetime import datetime
from werkzeug.utils import secure_filename

try:
    from flask import Flask, send_from_directory, request, jsonify, redirect
except ImportError:
    print("[ERROR] Flask is not installed. Run: pip install flask")
    sys.exit(1)

# Base directory setup
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
DATA_DIR = os.path.join(BASE_DIR, "data")
MESSAGES_FILE = os.path.join(DATA_DIR, "messages.json")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Ensure required directories exist
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize messages file if not present
if not os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# Create Flask application
app = Flask(__name__, static_folder=None)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max upload limit
ALLOWED_EXTENSIONS = {"pdf", "docx", "doc", "txt", "png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------------------------------------------------------
# Static File Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Serve the main portfolio landing page."""
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/css/<path:filename>")
def serve_css(filename):
    """Serve CSS stylesheets."""
    return send_from_directory(os.path.join(BASE_DIR, "css"), filename)

@app.route("/js/<path:filename>")
def serve_js(filename):
    """Serve JavaScript files."""
    return send_from_directory(os.path.join(BASE_DIR, "js"), filename)

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    """Serve static media, images, and documents."""
    return send_from_directory(ASSETS_DIR, filename)

@app.route("/download-resume")
def download_resume():
    """Direct route to download Harish Kumar's resume."""
    resume_path = os.path.join(ASSETS_DIR, "Harish_Kumar_Resume.pdf")
    if os.path.exists(resume_path):
        return send_from_directory(ASSETS_DIR, "Harish_Kumar_Resume.pdf", as_attachment=True, download_name="Harish_KM_Resume.pdf")
    return jsonify({"error": "Resume file not found"}), 404

@app.route("/view-resume")
def view_resume():
    """Direct route to view Harish Kumar's resume inline in browser."""
    resume_path = os.path.join(ASSETS_DIR, "Harish_Kumar_Resume.pdf")
    if os.path.exists(resume_path):
        return send_from_directory(ASSETS_DIR, "Harish_Kumar_Resume.pdf", as_attachment=False, mimetype="application/pdf")
    return jsonify({"error": "Resume file not found"}), 404



# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.route("/api/status", methods=["GET"])
def api_status():
    """Health check endpoint."""
    return jsonify({
        "status": "online",
        "developer": "Harish Kumar",
        "role": "AI & Python Developer",
        "college": "Annai College of Arts and Science",
        "server_time": datetime.now().isoformat()
    })

@app.route("/api/contact", methods=["POST"])
def api_contact():
    """
    Handle contact form submissions.
    Saves incoming messages into data/messages.json.
    """
    try:
        # Support both JSON payload and Form Data
        data = request.get_json(silent=True) or request.form.to_dict()
        
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        message = data.get("message", "").strip()

        if not name or not email or not message:
            return jsonify({"status": "error", "message": "All fields are required."}), 400

        # Construct message record
        record = {
            "id": int(time.time() * 1000),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": name,
            "email": email,
            "message": message,
            "ip": request.remote_addr
        }

        # Read existing messages safely
        messages = []
        if os.path.exists(MESSAGES_FILE):
            try:
                with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
                    messages = json.load(f)
            except Exception:
                messages = []

        messages.append(record)

        # Write back to JSON file
        with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2)

        print(f"[CONTACT] New message from {name} ({email}): {message[:50]}...")

        return jsonify({
            "status": "success",
            "message": f"Thank you, {name}! Your message has been received and saved successfully."
        })

    except Exception as e:
        print(f"[ERROR] /api/contact failed: {e}")
        return jsonify({"status": "error", "message": "Internal server error occurred."}), 500


@app.route("/api/upload", methods=["POST"])
def api_upload():
    """
    Handle file uploads (for ATS resume analyzer demonstration).
    Saves uploaded file to uploads/ directory and extracts basic metadata.
    """
    if "file" not in request.files:
        return jsonify({"status": "error", "message": "No file part in request."}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"status": "error", "message": "No file selected."}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Prefix timestamp to avoid naming collision
        timestamped_name = f"{int(time.time())}_{filename}"
        save_path = os.path.join(UPLOADS_DIR, timestamped_name)
        file.save(save_path)

        file_size_kb = round(os.path.getsize(save_path) / 1024, 2)
        ext = filename.rsplit(".", 1)[1].lower()

        # Simulated ATS extraction insights based on resume file
        ats_extracted_keywords = [
            "Python", "Machine Learning", "SQL", "Deep Learning",
            "Problem Solving", "Data Analysis", "Communication"
        ]

        print(f"[UPLOAD] Saved file {timestamped_name} ({file_size_kb} KB)")

        return jsonify({
            "status": "success",
            "message": f"File '{name}' uploaded successfully.",
            "ats_preview": {
                "match_score": 88,
                "extracted_skills": ats_extracted_keywords,
            },
            "file": {
                "original_name": filename,
                "saved_as": timestamped_name,
                "size_kb": file_size_kb,
                "type": ext,
                "parsing_status": "Complete (100%)"
            }
        })

    return jsonify({
        "status": "error",
        "message": "Unsupported file format. Allowed formats: pdf, docx, doc, txt, png, jpg."
    }), 400


# ---------------------------------------------------------------------------
# Main Server Runner
# ---------------------------------------------------------------------------

def run_server(host="127.0.0.1", port=5000, open_browser=False):
    """Start the Flask server with clean, Windows-compatible console output."""
    # Ensure stdout handles utf-8 safely if possible
    try:
        if sys.stdout.encoding != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    banner = f"""
=============================================================================
   HARISH KUMAR -- AI & PYTHON DEVELOPER PORTFOLIO
   Degree: B.Sc. Artificial Intelligence (Annai College of Arts and Science)
-----------------------------------------------------------------------------
   * Local URL:     http://localhost:{port}
   * Network URL:   http://{host}:{port}
   * Static Files:  index.html, css/, js/, assets/
   * Uploads Dir:   {UPLOADS_DIR}
   * Messages File: {MESSAGES_FILE}
   
   Endpoints:
   - GET  /                -> Portfolio Landing Page
   - GET  /download-resume -> Download Resume PDF
   - POST /api/contact     -> Contact Form Message Submission
   - POST /api/upload      -> Resume & File Upload (ATS Analyzer)
   - GET  /api/status      -> Server Health Status
-----------------------------------------------------------------------------
   Press Ctrl+C to terminate the server.
=============================================================================
"""
    print(banner)

    if open_browser:
        def _launch_browser():
            time.sleep(0.8)
            try:
                webbrowser.open(f"http://localhost:{port}")
            except Exception:
                pass
        threading.Thread(target=_launch_browser, daemon=True).start()

    app.run(host=host, port=port, debug=False)


if __name__ == "__main__":
    port = 5000
    should_open_browser = True

    if "--no-browser" in sys.argv:
        should_open_browser = False
        sys.argv.remove("--no-browser")

    # Allow overriding port via command line argument: python main.py 8000
    for arg in sys.argv[1:]:
        if arg.isdigit():
            port = int(arg)

    run_server(host="127.0.0.1", port=port, open_browser=should_open_browser)


