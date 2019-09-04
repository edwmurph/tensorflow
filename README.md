# Dockerized Tensorflow V2 + Jupyter Notebook Starter

Tensorflow V2 project boilerplate that can check-in shared [Jupyter Notebooks](https://jupyter.org/) to source control and ensure consistent execution environments among developers.

# Usage

Build and run (automatically starts jupyter notebook):
```
docker-compose up
```

Execute an interactive bash shell on the container:
```
docker exec -it $(docker ps -aqf "name=tf") /bin/bash
```

