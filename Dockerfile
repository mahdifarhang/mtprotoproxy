FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y python3 python3-uvloop python3-cryptography python3-socks libcap2-bin ca-certificates && rm -rf /var/lib/apt/lists/*
RUN setcap cap_net_bind_service=+ep /usr/bin/python3.8

USER root

WORKDIR /home/tgproxy/

COPY --chown=root mtprotoproxy.py config.py /home/tgproxy/
RUN mkdir data &&\
    touch data/users_links.txt &&\
    touch data/users_data.csv &&\
    echo "name,connects,curr_connects,octets_from_client,octets_to_client,msgs_from_client,msgs_to_client,year,month,date,hour,minute\n" > data/users_data.csv &&\
    chmod 777 data/users_links.txt data/users_data.csv


CMD ["python3", "mtprotoproxy.py"]
