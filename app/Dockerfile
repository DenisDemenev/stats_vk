FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . ./

CMD ["gunicorn", "stats_vk.wsgi:application", "--bind", "0:8000" ]