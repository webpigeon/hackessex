#! /bin/bash
# build and push the docker image

docker build -t fossgalaxy/faqs .
docker push fossgalaxy/faqs

