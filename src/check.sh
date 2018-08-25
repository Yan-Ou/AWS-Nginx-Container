while true
do
    date >> usage.txt
    docker stats myweb --no-stream >> usage.txt
    echo '---------------------------' >> usage.txt
    sleep 10
done
