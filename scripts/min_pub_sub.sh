#!/bin/bash

#launch pub and sub modes with cleanup
cleanup(){
  echo "Restarting ROS2 daemon to cleanup before shutting down"
  ros2 daemon stop
  sleep 1
  ros2 daemon start
  echo "Terminating all ROS 2-related processes..."
  kill 0
  exit
}

trap 'cleanup' SIGINT

# Lanuch the pub
ros2 run ros2_fun py_min.py &

sleep 2

#Lanuch the sub
ros2 run ros2_fun py_min_sub.py