from flask import Flask, render_template, request
import google.generativeai as ai

app = Flask(__name__)

ai.configure(api_key="AIzaSyCaMq4ro-BN18OTV9XYvmHc-VX5X6P3MxU")
model = ai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        ask = request.form.get("ask")
        # prompt = f"Give me micros and macros in {ask} in 100 words. in point wise format. Give seperate seperate \n\n"
        prompt = f"Give me 1 week diet plan for  {ask} in 100 words with food recipies. in point wise format. Give seperate seperate \n\n"
        try:
            result = model.generate_content(prompt)
            response = result.text
        except Exception as e:
            response = f"Error: {e}"
    return render_template("sample.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
