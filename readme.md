# Tiny Ad Blocker

A simple [dnsmasq](https://en.wikipedia.org/wiki/Dnsmasq) Docker image which blocks ads at a DNS-level. When started the container will download a list of ad domains which are then redirected to localhost.

Inspired by [Pi-Hole](https://github.com/pi-hole/pi-hole), which is much more full featured and worth checking out if you're interested.


## Running 
```bash
docker run -d -p 53:53/tcp -p 53:53/udp --cap-add=NET_ADMIN dpindur/tiny-ad-blocker:latest
```
