FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc make postgresql-client libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code/

ENV PYTHONPATH=/code/src:$PYTHONPATH

EXPOSE 8000

CMD ["uvicorn", "image_server.main:app", "--host", "0.0.0.0", "--port", "8000"]