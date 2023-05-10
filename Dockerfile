FROM ubuntu:latest

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

#RUN apt-get install python3 python3-pip

COPY ./ ./

# Install all dependencies (with dev ones)
RUN python3 -m pip install -r requirements.txt

# Expose the listening port
EXPOSE 7860

# Run npm start script when container starts
CMD [ "python3", "server.py" ]
