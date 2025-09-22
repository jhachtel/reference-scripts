#!/bin/bash

# If you need to know if some types of files are in a dir on a remote server.

PATTERN_1="first_pattern"
PATTERN_2="second_pattern"
PATTERN_3="third_pattern"

USERNAME=$(whoami)
REMOTE_HOSTNAME="abcdefg.env.host.net"

REMOTE_DIRECTORY="/some/dir/on/the/remote/where/the/files/you/want/are/kept"

ssh "$USERNAME@$REMOTE_HOSTNAME" << EOF | grep -E "\.txt$" > ./logs/target_file_list.log
  cd $REMOTE_DIRECTORY
  ls | grep -Ei "${PATTERN_1}|${PATTERN_2}|${PATTERN_3}"
EOF
