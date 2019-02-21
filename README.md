# LOCUST SWARM

## Standalone

locust --host=http://<ip target>

## Running master

locust --host=http://<ip target> --master
locust --host=http://goku.mesos --master

## Running slave

locust --host=http://<ip target> --slave --master-host=<master ip>
locust --host=http://goku.mesos --slave --master-host=192.168.100.8
