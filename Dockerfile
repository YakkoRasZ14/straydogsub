FROM kalilinux:kali-linux-docker

ARG DEBIAN_FRONTEND=noninteractive
# Update
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y autoremove && apt-get clean

# Install ZSH shell with custom settings and set it as default shell
RUN apt-get -y install git zsh && wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
COPY config/.zshrc /root/.zshrc

RUN apt-get install -y \
    coreutils \
    bash \
    build-base \
    bzip2-dev \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    util-linux \
    libevent \
    jpeg-dev \
    libffi-dev \
    libpq \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    musl \
    neofetch \
    openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-dev \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    readline-dev \
    sqlite \
    ffmpeg \
    sqlite-dev \
    sudo \
    chromium \
    chromium-chromedriver \
    zlib-dev \
    jpeg \
    zip \
    megatools \
    nodejs \
    freetype-dev \
    nmap

RUN apt-get -y install vim kali-linux-top10 net-tools whois netcat exploitdb man-db dirb nikto wpscan uniscan nodejs npm python3-pip tor proxychains


RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && pip3 install wheel \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

#
# Clone repo and prepare working directory
#
RUN git clone https://github.com/MrRobot222/TESLA/ /root/TESLA
RUN mkdir /root/TESLA/bin/
WORKDIR /root/TESLA/

#
# Copies session and config (if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/

#
# Install requirements
#
RUN pip3 install -r requirements.txt
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
CMD ["python3","-m","userbot"]