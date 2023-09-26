FROM python:3.11 
RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

RUN pip3 install flask_cors  # Agrega esta línea para instalar flask_cors

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
