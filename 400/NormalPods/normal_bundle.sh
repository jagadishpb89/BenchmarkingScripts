#! /bin/bash

./run-normal-pod-rs.py 1 1368 2 4 4 8 1 &
./run-normal-pod-rs.py 1 1368 4 8 8 16 2 &
./run-normal-pod-rs.py 1 1368 6 12 12 24 3 &
./run-normal-pod-rs.py 1 1368 8 16 16 32 4 &
./run-normal-pod-rs.py 1 1368 10 20 20 40 5 &
