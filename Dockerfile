FROM python:3.9.6

COPY simple.py /simple.py

CMD ["python", "/simple.py"]
