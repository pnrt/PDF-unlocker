from flask import Flask, request, send_file
from flask_cors import CORS
import PyPDF2
import io
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/unlock', methods=['POST'])
def unlock_pdf():
    if 'file' not in request.files or 'password' not in request.form:
        return "File or password missing", 400

    pdf_file = request.files['file']
    password = request.form['password']
    
    # Get the original filename without extension
    original_filename = os.path.splitext(pdf_file.filename)[0]
    unlocked_filename = f"{original_filename}_unlocked.pdf"

    reader = PyPDF2.PdfReader(pdf_file)

    if not reader.is_encrypted:
        return "PDF is not locked", 400

    if not reader.decrypt(password):
        return "Invalid password", 400

    writer = PyPDF2.PdfWriter()
    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])

    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)

    return send_file(output_pdf, as_attachment=True, download_name=unlocked_filename, mimetype="application/pdf")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
