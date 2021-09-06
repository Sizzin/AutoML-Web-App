import requests as rq
import streamlit as st

import custom_warning

def get_api(url):
    """A simple GET request that return the Response object of the request"""
    return rq.get(url)

def app():
    st.write('''
    # Usage of APIs
    ''')
    api_url = st.text_input('Insert an API endpoint and I\'ll bring you the JSON results.')
    if api_url:
        res = get_api(api_url)
        st.write(res.json())
    else:
        st.write('Try an API!')

    api_examples = {
        'Exchange': 'https://economia.awesomeapi.com.br/last/USD-EUR,BTC-USD,USD-JPY',
        'COVID-19': 'https://api.covidtracking.com/v1/us/20201231.json',
        'Pokemon': 'https://pokeapi.co/api/v2/pokemon?limit=10',
    }
    st.write('Some aweome API examples:')
    for name, url in api_examples.items():
        st.write(f'{name} - {url}')

    