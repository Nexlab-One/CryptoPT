FROM python:3
WORKDIR /usr/app/src
COPY args.py ./ \
    save.py ./ \
    show.py ./ \
    currencySymbolList.txt ./ \
    requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY cryptopt.py ./
ENV _COINMARKETCAP_APIKEY=ded7a69d-b172-4478-8228-6c9984ae0b92
EXPOSE 80 \
    443
CMD [ "python", "./cryptopt.py" ]