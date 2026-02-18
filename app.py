import os
import uuid
from flask import Flask, request, send_file, render_template
from webtoepub import WebToEpub

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            tmp_dir = f"/tmp/{uuid.uuid4()}"
            os.makedirs(tmp_dir, exist_ok=True)

            try:
                wt = WebToEpub(url)
                novel_title = wt.metadata.title or "novel"
                safe_title = "".join(c if c.isalnum() or c in " _-" else "_" for c in novel_title)
                output_path = os.path.join(tmp_dir, f"{safe_title}.epub")
                
                wt.convert(output_path)
                return render_template("success.html", filename=f"{safe_title}.epub", file_path=output_path)
            except Exception as e:
                return f"<h2>Error generating EPUB:</h2><pre>{str(e)}</pre>"
    return render_template("index.html")
