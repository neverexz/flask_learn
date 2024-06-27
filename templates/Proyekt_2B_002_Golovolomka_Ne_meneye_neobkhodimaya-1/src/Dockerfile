FROM python:3.10.2
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install -U langchain-community
RUN pip install gigachain
RUN pip install gigachat
CMD python ./1.py