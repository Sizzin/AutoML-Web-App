import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

import custom_warning

@st.cache
def load_df(df):
    df = pd.read_csv(df)
    chosen_model = df[df['tags.Source'] == 'finalize_model']
    run_time = df['tags.Run Time'].sum()
    df = df[df['tags.Source'] == 'compare_models']
    df = df[['tags.mlflow.runName', 'metrics.Accuracy', 'metrics.Prec', 'metrics.F1', 'metrics.Recall', 'tags.Run Time']]
    df.sort_values(by='metrics.Accuracy', ascending=False, inplace=True)
    new_columns = ['Algorithm', 'Accuracy', 'Precision', 'F1', 'Recall', 'Run time']
    df.columns = new_columns
    df.reset_index(drop='index', inplace=True)
    return df, chosen_model, run_time


def app():
    st.write('This is a simple web app to show the results of a AutoML test using PyCaret and the Kaggle Titanic Dataset.')
    st.write('''
    # Titanic Dataset with AutoML (PyCaret)
    ''')
    df, chosen_model, run_time = load_df('clf-default-name_logs.csv')
    st.write(f'PyCaret AutoML tested a total of {df.shape[0]} algorithms in {run_time} seconds.')
    chosen_model_name, chosen_model_accuracy = chosen_model['tags.mlflow.runName'].values[0], chosen_model['metrics.Accuracy'].values[0]
    st.markdown(f'Best model: <span style="font-weight: bold;">{chosen_model_name} - {chosen_model_accuracy * 100:.2f}%</span>', unsafe_allow_html=True)
    st.write(df)