FROM debian:latest
ENTRYPOINT []
CMD ["echo OIVAS7572"]
RUN apt-get update && \
    apt-get -y install sudo
RUN useradd OIVAS7572 && echo "OIVAS7572:OIVAS7572" | chpasswd && adduser OIVAS7572 sudo
USER OIVAS7572
ADD /engine/ .
#RUN chmod -R 777 ./engine/
RUN chmod +x stockfishbmi2
RUN chmod +x stockfishmodern
RUN chmod +x stockfishavx2
RUN chmod +x stockfishssse


RUN echo OIVAS7572 | sudo -S apt-get update && sudo apt-get install -y vim
RUN echo OIVAS7572 | sudo -S apt-get install -y wget
RUN echo OIVAS7572 | sudo -S apt-get update
RUN echo OIVAS7572 | sudo -S apt-get install -y python3 python3-pip


RUN apt install python3-pip -y
RUN apt install python3-venv
RUN python3 -m venv venv
RUN source ./venv/bin/activate
COPY requirements.txt .
RUN echo OIVAS7572 | sudo -S python3 -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python3 lichess-bot.py -u

