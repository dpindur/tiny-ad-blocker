#!/bin/bash

sudo docker run -it --name tiny-ad-blocker --cap-add=NET_ADMIN -p 53:53/tcp -p 53:53/udp dpindur/tiny-ad-blocker:latest
sudo docker stop tiny-ad-blocker
sudo docker rm tiny-ad-blocker
