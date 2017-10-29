FROM alpine:latest

RUN apk --no-cache add dnsmasq python ca-certificates && \
    mkdir -p /etc/ad-hole/

COPY dnsmasq.conf /etc/dnsmasq.conf
COPY download-lists.py /download-lists.py
COPY entrypoint.sh /entrypoint.sh

EXPOSE 53/tcp 53/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD ["dnsmasq", "-k"]
