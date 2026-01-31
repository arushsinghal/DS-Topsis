from flask import Flask, render_template, request
import os, re, smtplib
from email.message import EmailMessage
from topsis import topsis

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Get credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your-email@example.com")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "")

def send_email(receiver, file_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result File"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver
    msg.set_content("Attached is your TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="topsis_result.csv"
        )

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        # Email validation
        if not re.match(EMAIL_REGEX, email):
            return "Invalid Email Format"

        weights = list(map(float, weights.split(",")))
        impacts = impacts.split(",")

        if len(weights) != len(impacts):
            return "Number of weights must equal number of impacts"

        if not all(i in ['+', '-'] for i in impacts):
            return "Impacts must be + or -"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "result.csv")

        file.save(input_path)

        topsis(input_path, weights, impacts, output_path)
        send_email(email, output_path)

        return "Result sent successfully to email!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
