#!/bin/bash

container_ids=$(docker ps -aq --filter name=dazzle_compute)

if [ -z "$container_ids" ]; then
    echo "No containers found matching 'dazzle_compute'"
    exit 1
fi

successful_ids=()
restarted_ids=()
for container_id in $container_ids; do
    # restart the whole container
    # docker restart $container_id

    # restart the dizzy server inside the container
    docker exec $container_id /bin/bash -c "pkill -f dizzy-server.py; python /app/dizzy-server.py &"
    if [ $? -ne 0 ]; then
        echo -e "\e[31mFailed to restart dizzy server in container $container_id\e[0m"
        read -p "Do you want to restart the container? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            docker restart $container_id
            restarted_ids+=($container_id)
        fi
    else
        successful_ids+=($container_id)
    fi
    
    # Wait a moment for the server to start
    # sleep 2
    
    # echo "Server state in container $container_id:"
    # docker exec $container_id /bin/bash -c "ps aux | grep dizzy-server.py"
    # echo "---"
done

# echo out the ids of the containers
echo "Restarted dizzy servers for containers:"
echo $successful_ids
echo "Had to restart the container to get the server running in some cases:"
echo $restarted_ids