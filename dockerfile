FROM python:3.10.13


#RUN sudo add-apt-repository ppa:mozillateam/firefox-next
#RUN sudo apt-get update
#RUN apt update && apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa
#RUN apt install python3.10 -y
#RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.10 /usr/bin/python

WORKDIR /app

COPY requeriments.txt ./requirements.txt
COPY app.py ./app.py

#RUN cd /app
RUN pip install streamlit==1.28.2 bardapi==0.1.38

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
