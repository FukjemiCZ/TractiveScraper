FROM python:3.10

RUN useradd -rm -d /home/tractive -s /bin/bash -u 1001 tractive

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-build-isolation --no-cache-dir -r requirements.txt

RUN chown -R 1001:1001 /usr/src/app

ENV TZ Europe/Prague

ENV PYTHONUNBUFFERED=1

USER 1001:1001

ENTRYPOINT ["python", "-u", "/usr/src/app/schedul.py"]
