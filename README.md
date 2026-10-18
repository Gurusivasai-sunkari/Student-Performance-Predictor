🎓 Student Performance Predictor

Turning Academic Data into Meaningful Predictions 🚀

An End-to-End Machine Learning Web Application

Predict student exam scores using study hours, attendance, and previous academic performance. Explore how Machine Learning can transform academic data into predictions and personalized suggestions through a simple, interactive web application.

<p align="center">  <a href="https://student-performance-predictor-psyy.onrender.com">
    <img src="https://img.shields.io/badge/🚀_LIVE_DEMO-Try_the_Application-2ea44f?style=for-the-badge" alt="Live Demo"/>
  </a>  <a href="https://github.com/Gurusivasai-sunkari/Student-Performance-Predictor">
    <img src="https://img.shields.io/badge/GitHub-View_Source_Code-181717?style=for-the-badge&logo=github" alt="GitHub Repository"/>
  </a></p>---

🌐 Live Demo

Experience the application here:

👉 "Student Performance Predictor — Open Live Application" (https://student-performance-predictor-psyy.onrender.com)

Enter academic details, generate a predicted exam score, and explore suggestions based on the prediction.

«Note: The application is hosted on Render's free tier. If it has been inactive, the first request may take a little longer to load.»

---

📸 Application Preview

🏠 Home Page

The home page provides a clean interface for entering academic information and generating a prediction.

"Student Performance Predictor - Home Page" (screenshots/homepage.png.png)

📊 Prediction Results

The results page displays the predicted exam score along with suggestions intended to help students reflect on their academic preparation.

"Student Performance Predictor - Prediction Results" (screenshots/prediction-results.png.png)

---

💡 About the Project

The Student Performance Predictor is a Machine Learning project designed to estimate a student's exam score using selected academic factors.

Academic performance can be influenced by several factors, including study habits, attendance, and previous results. This project explores how these inputs can be used by a trained regression model to estimate an exam score.

The application combines a Python-based Machine Learning model with a Flask web interface, allowing users to interact with the model without running Python code themselves.

The project demonstrates a complete workflow, from working with a dataset and training a model to evaluating its performance, integrating it into a web application, and deploying the application online.

🎯 Project Objectives

- Understand the practical application of supervised Machine Learning.
- Explore regression for predicting numerical values.
- Process academic data and select relevant input features.
- Evaluate model performance using appropriate metrics.
- Integrate a trained model into a Flask application.
- Deploy a functional ML application that users can access online.
- Explore how predictions can be presented alongside useful study suggestions.

---

✨ Key Features

- 📚 Exam Score Prediction: Estimates an exam score using academic inputs.
- 🧠 Machine Learning Integration: Uses a trained Linear Regression model.
- 📊 Academic Input Analysis: Takes study hours, attendance, and previous scores into account.
- 💬 Personalized Suggestions: Provides suggestions based on the predicted result.
- 🌐 Interactive Web Interface: Makes the prediction process simple and accessible.
- ✅ Input Validation: Helps prevent invalid or incomplete inputs from being processed.
- ⚡ Real-Time Prediction: Generates a result when the user submits the form.
- 🚀 Online Deployment: Allows users to try the application through a live URL.
- 🧪 Model Evaluation: Includes performance metrics to assess the model's predictive ability.

---

🛠️ Tech Stack

Technology| Purpose
Python| Core programming language
Pandas| Data loading and manipulation
NumPy| Numerical operations
Scikit-learn| Model training, preprocessing, and evaluation
Linear Regression| Exam score prediction
Flask| Backend web framework
HTML5| Web page structure
CSS3| Styling and layout
Pickle| Saving and loading the trained model
Git & GitHub| Version control and source code hosting
Render| Web application deployment

---

🧠 Machine Learning Approach

1. Problem Definition

This project treats student exam score prediction as a supervised regression problem because the target variable, "Exam_Score", is numerical.

2. Input Features

The model uses the following features:

Feature| Description
"Hours_Studied"| Number of hours spent studying
"Attendance"| Student attendance percentage
"Previous_Scores"| Scores from previous academic assessments

Target variable: "Exam_Score"

3. Data Preparation

The dataset is loaded and prepared for model development. The selected input features are separated from the target variable before training and evaluation.

4. Model Selection

Linear Regression was selected as the prediction algorithm. Polynomial feature degrees were also explored during experimentation, with degree 1 performing best among the tested degrees from 1 to 6.

Degree 1 corresponds to the standard linear feature representation used for the final model.

5. Model Evaluation

The model is evaluated using:

- R² Score: Measures how much variation in the target is explained by the model.
- Mean Absolute Error (MAE): Measures the average absolute difference between predicted and actual scores.
- Cross-Validation Mean R²: Provides an additional view of model performance across validation splits.

6. Web Integration

The trained model is saved as "model.pkl" and loaded by the Flask application. When a user submits the form, the application processes the input and generates a prediction.

---

📈 Model Performance

The following are the recorded evaluation results for the current model.

Evaluation Metric| Result
Test R² Score| 0.5156
Mean Absolute Error (MAE)| 1.4631
Cross-Validation Mean R²| 0.5912

What Do These Results Mean?

- R² Score — 0.5156: The model explains approximately 51.56% of the variation in exam scores on the evaluated test data.
- MAE — 1.4631: The average absolute prediction error is approximately 1.46 score points, measured in the target's units.
- Cross-Validation Mean R² — 0.5912: The mean R² across the cross-validation runs is approximately 0.59.

These metrics describe performance on the evaluated data. Actual results may vary on unseen data, and predictions should not be treated as guaranteed exam scores.

📄 Detailed Model Report: "View MODEL_REPORT.md" (MODEL_REPORT.md)

---

⚙️ How the Application Works

The application follows a straightforward prediction workflow:

1. User Input: The user enters study hours, attendance, and previous scores.
2. Input Validation: The application checks that the submitted values are valid.
3. Model Loading: Flask uses the previously trained Machine Learning model.
4. Prediction: The input data is passed to the model to estimate the exam score.
5. Result Display: The predicted score is displayed on the results page.
6. Study Suggestions: The application provides suggestions based on the prediction.

This workflow connects the trained model to a user-friendly web interface.

---

📂 Project Structure
Student-Performance-Predictor/
│
├── app.py                         # Flask application
├── model.pkl                      # Trained ML model
├── student_performance.ipynb       # Data analysis and model development
├── StudentPerformanceFactors.csv   # Dataset
├── requirements.txt                # Python dependencies
├── MODEL_REPORT.md                 # Model evaluation report
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore rules
│
├── templates/
│   └── index.html                  # HTML template
│
├── static/
│   └── style.css                   # Application styling
│
└── screenshots/
    ├── homepage.png.png            # Home page screenshot
    └── prediction-results.png.png  # Prediction screenshot

---

💻 Run the Project Locally

Want to explore the code or run the application on your own computer? Follow these steps.

Prerequisites

Make sure you have installed:

- Python 3.10 or a compatible version for the project's dependencies
- Git
- A code editor such as VS Code

Step 1: Clone the Repository

git clone https://github.com/Gurusivasai-sunkari/Student-Performance-Predictor.git

Step 2: Open the Project Folder

cd Student-Performance-Predictor

Step 3: Create a Virtual Environment (Recommended)

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

On macOS or Linux:

source venv/bin/activate

Step 4: Install Dependencies

pip install -r requirements.txt

Step 5: Run the Application

python app.py

Step 6: Open in Your Browser

Visit:

http://127.0.0.1:5000

The application should now be available locally.

---

🔮 Future Improvements

This project provides a foundation for further experimentation and development. Potential improvements include:

- 📊 Feature Engineering: Explore additional relevant academic features.
- 🧪 Model Comparison: Compare Linear Regression with other regression algorithms.
- 📈 Model Optimization: Experiment with preprocessing, feature selection, and hyperparameter tuning where applicable.
- 📉 Visual Analytics: Add charts to make predictions and academic patterns easier to understand.
- 🎯 Enhanced Recommendations: Develop more detailed, data-driven study suggestions.
- 📚 Larger and Diverse Datasets: Evaluate generalization using more varied data.
- 📱 Responsive UI Improvements: Refine the interface for different screen sizes.
- ☁️ Deployment Improvements: Explore more robust hosting and model-serving options.

These are possible future enhancements, not features currently claimed to be implemented.

---

⚠️ Limitations

- The model uses only three selected academic features.
- The prediction depends on patterns learned from the available dataset.
- Other factors affecting academic performance are not fully represented.
- Model performance on new students may differ from the reported evaluation results.
- The application provides estimates and suggestions, not official academic assessments or guaranteed outcomes.

---

👨‍💻 About the Developer

Guru Siva Sai

B.Tech Computer Science and Engineering Student
Aspiring AI/ML Engineer

I am interested in Machine Learning, Artificial Intelligence, and developing practical applications that turn data into useful insights.

This project represents my learning journey in data processing, regression models, model evaluation, Flask development, and deployment.

🔗 GitHub: "Gurusivasai-sunkari" (https://github.com/Gurusivasai-sunkari)

---

⭐ Support the Project

If you find this project interesting or useful:

- ⭐ Star the repository on GitHub.
- 🍴 Fork the repository to experiment with the code.
- 💡 Explore the project and suggest potential improvements.

Your feedback and suggestions are welcome!

---

<p align="center">
  <b>Built with Python, Machine Learning, and curiosity. 💙</b>
</p><p align="center">
  <a href="https://student-performance-predictor-psyy.onrender.com">
    🚀 Try the Live Application
  </a>
</p>
