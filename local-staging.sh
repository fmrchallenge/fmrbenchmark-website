#!/bin/sh -e
#
# stdout and stderr of processes spawned by this script are directed
# to files with names that end in `.out`. E.g., terminal output from
# `memcached` is directed to the file memcached.out.
#
#
# SCL

function killsub
{
    kill $MEMCACHED_PID
    sudo pkill -U rabbitmq
}


# Enable debugging support from Python
# cf. https://docs.python.org/3.5/library/asyncio-dev.html#debug-mode-of-asyncio
export PYTHONASYNCIODEBUG=1

memcached -l 127.0.0.1:11211 > memcached.out 2>&1 &
MEMCACHED_PID=$!

sudo -b -u rabbitmq /bin/sh -c 'for k in `cat etc/rabbitmq-env.conf`; do export RABBITMQ_$k; done && rabbitmq-server' > rabbitmq.out 2>&1


echo "support processes launched!"


trap killsub SIGINT SIGTERM SIGKILL

wait $MEMCACHED_PID
