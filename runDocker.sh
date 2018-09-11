#!/bin/bash

docker run --rm \
            -p 0.0.0.0:80:80 \
            -p 0.0.0.0:443:443 \
            -v /etc/letsencrypt:/etc/letsencrypt \
            -v /root/__DO_NOT_COMMIT__/envvars:/etc/apache2/envvars \
            --name mathtestmaker \
            -e HELLO \
            -e STRIPE_PUBLISHABLE_KEY \
            -e STRIPE_SECRET_KEY \
            -itd \
            -t melvyniandrag/mathtestmaker:first 

