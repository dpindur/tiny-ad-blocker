#!/bin/sh

python /download-lists.py /etc/ad-hole/ads.list

exec "$@"
