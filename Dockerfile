FROM python:3
WORKDIR /usr/app/src
COPY args.py ./
COPY save.py ./
COPY show.py ./
COPY currencySymbolList.txt ./
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENV _COINMARKETCAP_APIKEY=ded7a69d-b172-4478-8228-6c9984ae0b92
COPY cryptopt.py ./
EXPOSE 80
EXPOSE 443
CMD [ "python", "./cryptopt.py" ]