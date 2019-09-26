FROM python:3.7.4-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt --prefix=/install
COPY . .

FROM base
WORKDIR /app
COPY --from=builder /app .
COPY --from=builder /install /usr/local
