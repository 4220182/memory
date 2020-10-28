FROM python

# Install source files
COPY start.py /start.py
WORKDIR /

ENTRYPOINT []
CMD ["python2", "start.py", "50"]

