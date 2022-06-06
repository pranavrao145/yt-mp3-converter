FROM python:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN apt-get update -y && apt-get install ffmpeg -y

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
