FROM python:3.12-alpine as build

RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --deploy --ignore-pipfile

FROM python:3.12-alpine

WORKDIR /app

COPY --from=build /app /app

COPY . .

ENTRYPOINT ["pipenv", "run", "python", "organizex.py"]

CMD []
