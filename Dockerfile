FROM python:alpine
RUN mkdir -p /html/cgi-bin
COPY html/cgi-bin/aword.py /html/cgi-bin
COPY html/cgi-bin/words /html/cgi-bin
COPY server.py /
ENV PORT 8080
EXPOSE 8080
CMD ["/server.py"]
