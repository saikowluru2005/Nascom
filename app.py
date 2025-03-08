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



@app.route("/custommealplanner", methods=["GET", "POST"])
def custommealplanner():
    response = ""
    if request.method == "POST":
        # Collect form data
        age= request.form.get("age")
        height = request.form.get("height")
        weight = request.form.get("weight")
        target_weight = request.form.get("target_weight")
        diet = request.form.get("diet")
        preferred_vegetables = request.form.get("preferred_vegetables", "No preference")
        carbs = request.form.get("carbs", "No preference")
        proteins = request.form.get("proteins", "No preference")
        fats = request.form.get("fats", "No preference")
        vitamins = request.form.get("vitamins", "No preference")
        minerals = request.form.get("minerals", "No preference")
        allergies = request.form.get("allergies", "No")
        activity_level = request.form.get("activity_level")
        notes = request.form.get("notes", "")

        prompt = f"""
        Create a personalized meal plan , a {age}-year-old person with a height of {height} cm and a weight of {weight} kg. 
        Goal is to reach {target_weight} kg.
        
        Diet preference: {diet}
        Preferred vegetables: {preferred_vegetables}
        Macronutrient preferences:
        - Carbohydrates: {carbs}
        - Proteins: {proteins}
        - Fats: {fats}
        Micronutrient preferences:
        - Vitamins: {vitamins}
        - Minerals: {minerals}
        Allergies: {allergies}
        Activity level: {activity_level}
        
        Additional notes: {notes}

        Provide a detailed 1 week meal plan in 200 words with recipies, in point-wise format, including meals for breakfast, lunch, and dinner.
        """

        try:
            # Generate AI-based meal plan
            result = model.generate_content(prompt)
            response = result.text if result.text else "No response from the model."
        except Exception as e:
            response = f"Error: {e}"

    return render_template("cmp.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
