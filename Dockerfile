FROM yeop2/kogpt6b-ryan1.5b-float16

WORKDIR /workspace

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "main.py"]
