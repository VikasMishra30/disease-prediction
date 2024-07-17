import os
import pickle
import openai
import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))
breast_cancer_model = pickle.load(open(f'{working_dir}/saved_models/breast_cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction',
                            'Medical ChatBot'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'heartbeat', 'robot'],
                           default_index=0)

# Function to query OpenAI API
def query_openai_api(question):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Answer the following medical-related question: {question}\n\nIf the question is not related to medicine, respond with: 'I can only answer medical-related questions.'",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        return f"Sorry, I am unable to answer that question at the moment. ({str(e)})"

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1: Pregnancies = st.text_input('Number of Pregnancies')
    with col2: Glucose = st.text_input('Glucose Level')
    with col3: BloodPressure = st.text_input('Blood Pressure value')
    with col1: SkinThickness = st.text_input('Skin Thickness value')
    with col2: Insulin = st.text_input('Insulin Level')
    with col3: BMI = st.text_input('BMI value')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2: Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age')
    with col2: sex = st.text_input('Sex')
    with col3: cp = st.text_input('Chest Pain types')
    with col1: trestbps = st.text_input('Resting Blood Pressure')
    with col2: chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3: fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1: restecg = st.text_input('Resting Electrocardiographic results')
    with col2: thalach = st.text_input('Maximum Heart Rate achieved')
    with col3: exang = st.text_input('Exercise Induced Angina')
    with col1: oldpeak = st.text_input('ST depression induced by exercise')
    with col2: slope = st.text_input('Slope of the peak exercise ST segment')
    with col3: ca = st.text_input('Major vessels colored by flourosopy')
    with col1: thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: fo = st.text_input('MDVP:Fo(Hz)')
    with col2: fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3: flo = st.text_input('MDVP:Flo(Hz)')
    with col4: Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5: Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1: RAP = st.text_input('MDVP:RAP')
    with col2: PPQ = st.text_input('MDVP:PPQ')
    with col3: DDP = st.text_input('Jitter:DDP')
    with col4: Shimmer = st.text_input('MDVP:Shimmer')
    with col5: Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1: APQ3 = st.text_input('Shimmer:APQ3')
    with col2: APQ5 = st.text_input('Shimmer:APQ5')
    with col3: APQ = st.text_input('MDVP:APQ')
    with col4: DDA = st.text_input('Shimmer:DDA')
    with col5: NHR = st.text_input('NHR')
    with col1: HNR = st.text_input('HNR')
    with col2: RPDE = st.text_input('RPDE')
    with col3: DFA = st.text_input('DFA')
    with col4: spread1 = st.text_input('spread1')
    with col5: spread2 = st.text_input('spread2')
    with col1: D2 = st.text_input('D2')
    with col2: PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)

# Breast Cancer Prediction Page
if selected == "Breast Cancer Prediction":
    st.title("Breast Cancer Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1: mean_radius = st.text_input('Mean Radius')
    with col2: mean_texture = st.text_input('Mean Texture')
    with col3: mean_perimeter = st.text_input('Mean Perimeter')
    with col1: mean_area = st.text_input('Mean Area')
    with col2: mean_smoothness = st.text_input('Mean Smoothness')
    with col3: mean_compactness = st.text_input('Mean Compactness')
    with col1: mean_concavity = st.text_input('Mean Concavity')
    with col2: mean_concave_points = st.text_input('Mean Concave Points')
    with col3: mean_symmetry = st.text_input('Mean Symmetry')
    with col1: mean_fractal_dimension = st.text_input('Mean Fractal Dimension')

    breast_cancer_diagnosis = ''
    if st.button("Breast Cancer Test Result"):
        user_input = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension]
        user_input = [float(x) for x in user_input]
        breast_cancer_prediction = breast_cancer_model.predict([user_input])
        breast_cancer_diagnosis = "The person has breast cancer" if breast_cancer_prediction[0] == 1 else "The person does not have breast cancer"
    st.success(breast_cancer_diagnosis)

# Medical ChatBot Page
if selected == "Medical ChatBot":
    st.title("Medical ChatBot")
    user_input = st.text_input("Ask a medical-related question:")
    if user_input:
        response = query_openai_api(user_input)
        st.text_area("Response:", response, height=200)