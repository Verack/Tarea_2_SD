FROM python:3.5

RUN pip install grpcio \
		&& pip install grpcio-tools

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY chat_server.py .

COPY chat_pb2.py .

COPY chat_pb2_grpc.py .

CMD ["python", "/usr/src/app/chat_server.py"]