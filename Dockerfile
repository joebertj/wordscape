FROM python:slim-buster
RUN apt update -y
RUN apt install -y mailutils
WORKDIR /app
RUN mkdir -p html/cgi-bin
COPY html/cgi-bin/. html/cgi-bin
COPY server.py .
ENV PORT 8080
EXPOSE 8080
CMD ["/app/server.py"]
