FROM prefecthq/prefect:2.6.5-python3.9
COPY . /opt/prefect
RUN pip install .
