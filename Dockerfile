FROM python:alpine
RUN mkdir /html
RUN mkdir /html/cgi-bin
COPY html/cgi-bin/aword.py /html/cgi-bin
COPY html/cgi-bin/words /html/cgi-bin
COPY privkey.pem /
COPY fullchain.pem /
COPY servers.py /
EXPOSE 8082
CMD /servers.py
