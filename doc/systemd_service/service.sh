#!/bin/sh

# ADAPT to your needs and point this.service parameter to this file.

cd /home/newera/dqt
. ./dedup.profile

case "$1" in
  start)
        proc_find=$(ps -ef | grep 'dedup' | grep -v grep | awk '{print $2}')
        if [ "${proc_find}" = '' ]
        then
            dedup -a
            echo DQT started
        else
            echo DQT already started:
            echo ${proc_find}
            exit 1
        fi
        ;;
  stop)
        process=$(ps -ef | grep 'dedup' | grep -v grep | awk '{print $2}')
        if [ "${process}" != '' ]
        then
            kill -9 ${process}
            echo DQT stopped
        else
            echo DQT not running
            exit 1
        fi
        ;;
  restart)
        $0 stop
        sleep 2
        $0 start
        ;;
  status)
        proc_find=$(ps -ef | grep 'dedup' | grep -v grep | awk '{print $2}')
        if [ "${proc_find}" = '' ]
        then
              echo DQT stopped
        else
              echo DQT started:
              echo ${proc_find}
        fi
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|status}"
        exit 1
esac

exit 0
