FROM nardtree/anaconda3-debian-stretch
MAINTAINER nardtree <angeldust03@gmail.com>
EXPOSE 8000
WORKDIR /root/
RUN conda install gunicorn -y
RUN git clone https://github.com/GINK03/minimal-csv-uploadable-web-service
RUN conda install matplotlib -y
WORKDIR /root/minimal-csv-uploadable-web-service
CMD sh run_gunicorn.sh
