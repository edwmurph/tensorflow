FROM tensorflow/tensorflow:2.0.0rc0-gpu-py3-jupyter

RUN apt-get update && apt-get install -y git

RUN pip install git+https://github.com/edwmurph/ds
