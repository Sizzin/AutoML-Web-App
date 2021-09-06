import streamlit as st

import titanic_prediction, titanic_exploration, apis

def main():
    st.set_page_config(page_title='AutoML')
    # Hides menu and Streamlit logo
    hide_menu = '''
    <style>
        #MainMenu {display: none;}
        footer {visibility: hidden;}
    </style>
    '''
    st.markdown(hide_menu, unsafe_allow_html=True)

    st.sidebar.title('AutoML')
    page = st.sidebar.selectbox('Choose a page', ['Titanic Dataset AutoML', 'Titanic Survivor Prediction', 'Usage of APIs'])

    pages = {
        'Titanic Dataset AutoML': titanic_exploration.app,
        'Titanic Survivor Prediction': titanic_prediction.app,
        'Usage of APIs': apis.app
    }

    pages[page]()

if __name__ == '__main__':
    main()


