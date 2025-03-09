# from flask import Flask, render_template, request
from flask import Flask, render_template, request, jsonify
import google.generativeai as ai

app = Flask(__name__)

# Configure AI model
ai.configure(api_key="API-KEY")
model = ai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"], endpoint="dashboard")
def dashboard():
    return render_template("Dashboard.html")

@app.route("/Micro&Macro", methods=["GET", "POST"], endpoint="micro_macro")
def micro_macro():
    response = ""
    if request.method == "POST":
        ask = request.form.get("ask")
        prompt = f"Give me the macros and it's propotion, micros and it's propotion, and calorie content in {ask} in 100 words, give output without bolding of any word in point-wise format. Provide separate sections for micros and macros.\n\n"
        
        try:
            result = model.generate_content(prompt)
            response = result.text if result.text else "No response from the model."
        except Exception as e:
            response = f"Error: {e}"
            
    return render_template("mm.html", response=response)





@app.route("/Letsmakerecipie", methods=["GET", "POST"], endpoint="Letsmakerecipie")
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




@app.route("/custommealplanner", methods=["GET", "POST"], endpoint="custommealplanner")
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


@app.route('/chat', methods=['GET'], endpoint='chat')
def chat():
    return render_template('chat.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')

    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"Error: {str(e)}"
    
    return jsonify({"reply": reply})




if __name__ == "__main__":
    app.run(debug=True)
