FROM python:3.12.6-alpine AS build

RUN apk add --no-cache \
    curl git make zlib-dev libbz2 readline-dev \
    sqlite-dev wget ncurses-libs xz tk-dev libffi-dev libmagic \
    python3-dev build-base libssl3 xz-libs

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12.6-alpine

COPY --from=build /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=build /app /app

WORKDIR /app

ENTRYPOINT ["python", "organizex.py"]

CMD []
