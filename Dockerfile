FROM kalilinux/kali-rolling
COPY commands /commands
RUN apt-get update -y && \
    apt-get install -y curl net-tools nmap bash mc && \
    chmod 755 /commands && \
    /commands
