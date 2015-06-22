#!/bin/bash
if [[ -z VG_HOOK_EXE ]];then
    echo "[FATAL]: Environment variable VG_HOOK_EXE is not defined for this image."
    exit -1
fi    

mkdir -p /var/atlassian/application-data/stash/external-hooks
mv vg_hook.sh /var/atlassian/application-data/stash/external-hooks

# Set up the hook properly as per the user configuration
python setup_hook.py

if [[ $? -eq 0 ]];then    
   ./run.sh $1
fi   