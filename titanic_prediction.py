import pandas as pd
import streamlit as st

from rich.console import Console
console = Console()

import model, custom_warning

def load_model():
    return model.load_model('model')


def create_prediction_fields():
    st.write('### Insert the values to predict whether the person would surive the tragedy.')
    p_class = st.selectbox('Ticket class', [1, 2, 3])
    sex = st.selectbox('Genre', ['male', 'female'])
    age = st.slider('Age', 1, 90)
    sib_sp = st.slider('# of siblings/spouses aboard', 0, 10)
    parch = st.slider('# of parents/children aboard', 0, 10)
    embarked = st.selectbox('Port of Embarkation', ['S', 'C', 'Q'])
    values = {
        'Pclass': [p_class],
        'Sex': [sex],
        'Age': [age],
        'SibSp': [sib_sp],
        'Parch': [parch],
        'Embarked': [embarked],        
    }
    return pd.DataFrame(values)

def app():
    console.log('Loading model...')
    trained_model = load_model()
    console.log('Model loaded!')
    st.write('''
    # Titanic Survivor Prediction
    ''')
    pred_values = create_prediction_fields()
    prediction = trained_model.predict(pred_values)
    survived = {
        0: 'Survived? <span style="color: red; font-weight: bold;">No</span>',
        1:  'Survived? <span style="color: green; font-weight: bold;">Yes</span>',
    }
    st.markdown(survived[prediction[0]], unsafe_allow_html=True)