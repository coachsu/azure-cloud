FROM --platform=linux/amd64 python
RUN mkdir /usr/src/translator
WORKDIR /usr/src/translator
COPY translator/ .
RUN pip install -r requirements.txt
CMD ["python","app.py"]