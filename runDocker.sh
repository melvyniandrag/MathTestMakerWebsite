#!/bin/bash
docker run --rm -p 0.0.0.0:80:80 -v /root/MathTestMakerWebsite:/root/MathTestMakerWebsite --name mathtestmaker -it -t melvyniandrag/mathtestmaker:first 

