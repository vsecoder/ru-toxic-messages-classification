FROM python:3.8-slim as python-base

COPY ./ ./

# Install all dependencies (with dev ones)
RUN pip3 install -r requirements.txt

# Expose the listening port
EXPOSE 7860

# Run npm start script when container starts
CMD [ "gradio", "server.py" ]
