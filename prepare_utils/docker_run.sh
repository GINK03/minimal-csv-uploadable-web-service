CNAME=$1
echo $CNAME
docker run -p 8000:8000 -it --mount type=bind,source=$HOME/logs,target=/logs $CNAME 
