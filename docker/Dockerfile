FROM alpine:3.7
LABEL maintainer "Marco Antonio Albero Albero <periket2000@gmail.com>" architecture="AMD64/x86_64" version="1.0" date="14-August-2018"

# Installing build dependencies
RUN echo " ... installing python and git ..." \
    && apk add --no-cache python3 python3-dev py-cffi libffi-dev musl-dev openssl-dev sudo shadow \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    && pip3 install virtualenv \
    && apk --update add git build-base \
    && rm -r /root/.cache \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && apk del gcc g++ build-base make \
    && rm -fr /usr/share /usr/libexec/gcc \
    && rm -fr /var/cache/apk \
    && find /usr/ -name '*pycache*' -exec rm -fr {} +;    

ENV PROJECT_DIR /usr/local/pyenv
RUN mkdir -p ${PROJECT_DIR}/conf
RUN sed -e 's/# %wheel ALL=(ALL) NOPASSWD: ALL/%wheel ALL=(ALL) NOPASSWD: ALL/g' -i /etc/sudoers

COPY vendor/* ${PROJECT_DIR}/
COPY init.sh ${PROJECT_DIR}/init-container.sh
COPY env.sh ${PROJECT_DIR}/env.sh
COPY scripts/* ${PROJECT_DIR}/

RUN adduser -S py-user -u 1000 \
    && addgroup -S py-user -g 1000 \
    && chown -R py-user:py-user ${PROJECT_DIR} \
    && chown -R py-user:py-user /usr/lib/python* \
    && chmod +x ${PROJECT_DIR}/*.sh

RUN usermod -aG wheel py-user

USER py-user
ENTRYPOINT ${PROJECT_DIR}/init-container.sh
