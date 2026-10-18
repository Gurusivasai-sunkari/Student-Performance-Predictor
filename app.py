
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        previous_scores = float(request.form["previous_scores"])

        # Validate input values
        values = [hours, attendance, previous_scores]

        if not all(np.isfinite(values)):
            raise ValueError

        if not 0 <= hours <= 20:
            return render_template(
                "index.html",
                error="Study hours must be between 0 and 20."
            )

        if not 0 <= attendance <= 100:
            return render_template(
                "index.html",
                error="Attendance must be between 0 and 100."
            )

        if not 0 <= previous_scores <= 100:
            return render_template(
                "index.html",
                error="Previous scores must be between 0 and 100."
            )

        # Predict exam score
        input_data = np.array(
            [[hours, attendance, previous_scores]]
        )

        prediction = model.predict(input_data)
        prediction = float(np.asarray(prediction).reshape(-1)[0])
        prediction = round(prediction, 2)

        # Personalized student feedback
        strengths = []
        suggestions = []

        # Attendance feedback
        if attendance < 75:
            suggestions.append({
                "title": "Make Attendance Your Priority",
                "message": (
                    "Your next step is to build a stronger connection "
                    "with classroom learning. Attend classes regularly, "
                    "stay engaged with your faculty, and avoid missing "
                    "important concepts. Every class you attend is "
                    "another opportunity to move forward."
                )
            })
        else:
            strengths.append(
                "Your attendance reflects a good commitment "
                "to classroom learning. Keep it consistent!"
            )

        # Previous score feedback
        if previous_scores < 60:
            suggestions.append({
                "title": "Build Stronger Fundamentals",
                "message": (
                    "Your previous performance is a starting point, "
                    "not your limit. Focus on understanding concepts "
                    "rather than memorizing answers. Practise questions, "
                    "review your mistakes, and approach every upcoming "
                    "exam as a fresh opportunity to improve."
                )
            })
        else:
            strengths.append(
                "Your previous scores show a promising academic "
                "foundation. Use that experience to aim even higher!"
            )

        # Study hours feedback
        if hours < 3:
            if attendance >= 75 and previous_scores >= 60:
                suggestions.append({
                    "title": "Turn Your Potential into Progress",
                    "message": (
                        "You already have encouraging signs in your "
                        "attendance and previous scores. Now, challenge "
                        "yourself to dedicate more time to focused study. "
                        "Set a realistic daily target, revise consistently, "
                        "and use your existing strengths to work towards "
                        "even better results."
                    )
                })
            else:
                suggestions.append({
                    "title": "Create a Consistent Study Routine",
                    "message": (
                        "Small, consistent efforts can make your learning "
                        "more effective. Start with a manageable study "
                        "schedule, revise what you learn each day, and "
                        "gradually increase your focused study time. "
                        "Consistency matters more than last-minute pressure."
                    )
                })
        elif hours < 5:
            strengths.append(
                "You're putting time into studying. A structured "
                "revision plan and focused practice can help you "
                "make that time more productive."
            )
        else:
            strengths.append(
                "Your study time shows initiative. Keep a healthy "
                "balance between focused learning, revision, and rest."
            )

        # Overall motivational message
        if not suggestions:
            overall_message = (
                "You're building a positive academic routine! "
                "Keep strengthening your concepts, stay consistent, "
                "and challenge yourself to make steady progress. "
                "Your next achievement starts with today's effort."
            )
        elif len(suggestions) >= 2:
            overall_message = (
                "Every strong student has areas to improve. "
                "Don't feel discouraged by where you are today. "
                "Start with one change, stay consistent, and build "
                "better habits step by step. Your progress is "
                "more important than perfection."
            )
        else:
            overall_message = (
                "You already have a foundation to build on. "
                "Focus on the improvement suggested below and "
                "keep moving forward, one day at a time."
            )

        # Return prediction and personalized feedback
        return render_template(
            "index.html",
            prediction=prediction,
            strengths=strengths,
            suggestions=suggestions,
            overall_message=overall_message
        )

    except (ValueError, TypeError, KeyError) as e:
        return render_template(
            "index.html",
            error=f"Input error: {str(e)}"
    )


if __name__ == "__main__":
    app.run(debug=True)
