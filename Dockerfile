FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -U pip

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"] 