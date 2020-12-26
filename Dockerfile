FROM python:3.9
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pipenv install twitchio
COPY . .
CMD ["python", "bot.py"]