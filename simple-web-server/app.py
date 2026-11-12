from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

# หน้าเว็บฟอร์ม
form_html = """
<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <title>Submit Message</title>
</head>
<body>
  <h1>Submit your message</h1>
  <form method="post">
    <textarea name="message" rows="5" cols="40"></textarea><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message', '')
        # บันทึกข้อความลงไฟล์ log.txt (รองรับภาษาไทย)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(message + '\n')
        # escape ก่อนแสดงผล เพื่อป้องกันการแทรกสคริปต์ (XSS)
        return f'<h1>Message received:</h1><p>{escape(message)}</p><a href="/">Back</a>'
    return render_template_string(form_html)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)