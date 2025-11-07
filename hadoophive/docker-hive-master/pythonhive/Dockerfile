FROM bde2020/hadoop-base:2.0.0-hadoop3.2.1-java8
RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list.d/stretch.list && \
    echo "deb http://archive.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list.d/stretch.list && \
    apt update

RUN apt install -y wget
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh
RUN mkdir -p /root/.conda
ENV PATH="/opt/conda/bin:${PATH}"


RUN apt install -y libsasl2-dev
RUN apt install -y gcc
RUN apt install -y g++
RUN apt install -y libsasl2-modules libsasl2-dev
RUN pip install PyHive
RUN pip install sasl
RUN pip install thrift
RUN pip install thrift-sasl
COPY ./app /home/app
ADD run.sh /tmp/run.sh
RUN chmod +x /tmp/run.sh

CMD ["/tmp/run.sh"]
