#!/bin/bash

# If you need the list of all files in a dir on a remote server based on some patterns.

PATTERN_1="first_pattern.log"
PATTERN_2="second_pattern.txt"
PATTERN_3="third_pattern.csv"

USERNAME=$(whoami)
REMOTE_HOSTNAME="abcdefg.env.host.net"

REMOTE_DIRECTORY="/some/dir/on/the/remote/where/the/files/you/want/are/kept"

ssh "$USERNAME@$REMOTE_HOSTNAME" << EOF | grep -E "${PATTERN_1}|${PATTERN_2}|${PATTERN_3}" > ./logs/target_dir_file_list.log
  cd $REMOTE_DIRECTORY
  ls
EOF
