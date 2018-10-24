#!/bin/sh -x
HOST=$1

# get region of host
REGION="us-east-1"

# get ssh key for region
SSH_KEY=$(cat keymap.txt| jq -r ".|.[\"${REGION}\"]")

# add SSH_KEY
SSH_KEY_PATH=$(cat config.txt| jq -r ".|.ssh_key_path")
ssh-add ${SSH_KEY_PATH}/${SSH_KEY}

# check OS to get which user to use
USER_NAME=ec2-user

# find pub IP addy for rules
# whatismyip API

# modify SG rules for ssh access from here.
# build cleanup rule for ssh access.

# ssh to host
ssh $USER_NAME@$HOST 

# execute cleanup SG rules.
