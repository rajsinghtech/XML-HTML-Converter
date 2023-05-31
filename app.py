from flask import Flask, request, redirect, url_for, send_from_directory
from lxml import etree
import os
import uuid

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_file_form():
    return '''
<!doctype html>
<html>
<head>
    <title>Upload XML and XSL Files</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        h1 {
            color: #333;
        }
        form {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        p {
            margin-bottom: 10px;
        }
        input[type="file"] {
            border: 1px solid #ddd;
            padding: 5px;
        }
        input[type="submit"] {
            background-color: #4CAF50; 
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition-duration: 0.4s;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form method="post" enctype="multipart/form-data" action="/convert">
        <h1>Upload XML and XSL Files</h1>
        <p>XML <input type="file" name="xml_file"></p>
        <p>XSL <input type="file" name="xsl_file"></p>
        <p><input type="submit" value="Submit"></p>
    </form>
</body>
</html>
    '''

@app.route('/convert', methods=['GET', 'POST'])
def convert_file():
    if request.method == 'POST':
        xml_file = request.files['xml_file']
        xsl_file = request.files['xsl_file']

        xml_tree = etree.parse(xml_file)
        xsl_tree = etree.parse(xsl_file)

        transform = etree.XSLT(xsl_tree)
        html_tree = transform(xml_tree)

        html_file_name = str(uuid.uuid4()) + ".html"
        html_file_path = os.path.join(app.config['UPLOAD_FOLDER'], html_file_name)
        with open(html_file_path, 'w') as file:
            file.write(str(html_tree))

        return redirect(url_for('uploaded_file', filename=html_file_name))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=8069)
