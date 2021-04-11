#!/bin/bash
cd $(dirname $(realpath $0))
file=$(ls -1 videos | grep mp4 | shuf -n 1)
python3 strip.py "videos/$file"
