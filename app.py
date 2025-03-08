from flask import Flask, render_template, request
import google.generativeai as ai

app = Flask(__name__)

# Configure AI model
ai.configure(api_key="AIzaSyCaMq4ro-BN18OTV9XYvmHc-VX5X6P3MxU")
model = ai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def dashboard():
    return render_template("Dashboard.html")

@app.route("/Micro&Macro", methods=["GET", "POST"])
def micro_macro():
    response = ""
    if request.method == "POST":
        ask = request.form.get("ask")
        prompt = f"Give me the micros and macros in {ask} in 100 words, in point-wise format. Provide separate sections for micros and macros.\n\n"
        
        try:
            result = model.generate_content(prompt)
            response = result.text if result.text else "No response from the model."
        except Exception as e:
            response = f"Error: {e}"
            
    return render_template("mm.html", response=response)


@app.route("/Letsmakerecipie", methods=["GET", "POST"])
def Letsmakerecipie():
    response = ""
    if request.method == "POST":
        ask = request.form.get("ask")
        prompt = f"Give me the micros and macros in {ask} recipie in 100 words, in point-wise format. Provide separate sections for micros and macros.\n\n"
        
        try:
            result = model.generate_content(prompt)
            response = result.text if result.text else "No response from the model."
        except Exception as e:
            response = f"Error: {e}"
            
    return render_template("lmr.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
