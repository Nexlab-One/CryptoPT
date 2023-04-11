FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD cryptopt.py /
CMD [ "python", "./cryptopt.py" ]