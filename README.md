# Tensorflow V2 + Jupyter Notebook starter

# Usage

Build and run image (automatically starts jupyter notebook):
```
docker-compose up
```

Execute bash in image:
```
docker exec -it $(docker ps -aqf "name=tf") /bin/bash
```

