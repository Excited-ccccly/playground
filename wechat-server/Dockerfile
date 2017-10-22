FROM groot.nanchao.org:5000/sluff-base:0.3
    WORKDIR /opt/app
    ADD . /opt/app/
    RUN chown -R node:node /opt/app
    USER node
    RUN cd /opt/app &&\
        npm set registry=https://registry.npm.taobao.org &&\
        npm install
    ENTRYPOINT ["npm", "start"]
    EXPOSE 3000
