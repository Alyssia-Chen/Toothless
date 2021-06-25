FROM python:3.7.2

WORKDIR /usr/src/app/

COPY scripts/install_dependencies.sh /usr/src/app/scripts/install_dependencies.sh
COPY requirements.txt /usr/src/app/
RUN scripts/install_dependencies.sh

#Copy everything from our current context (.) into Heroku's remote directory
COPY . /usr/src/app/

CMD scripts/start_app.sh