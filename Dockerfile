FROM python:slim-buster
RUN apt update -y
RUN apt install -y mailutils
RUN echo -n "kenchlightyear.com" > /etc/mailname
RUN sed -i "s/^dc_eximconfig_configtype.\+/dc_eximconfig_configtype='internet'/" /etc/exim4/update-exim4.conf.conf
RUN update-exim4.conf
WORKDIR /app
RUN mkdir -p html/cgi-bin
COPY html/cgi-bin/. html/cgi-bin
COPY server.py .
ENV PORT 8080
EXPOSE 8080
CMD ["/app/server.py"]
