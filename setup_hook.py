import yaml
import os
import sys

try:
   config_file = os.environ['STASH_CONFIG_PATH'] + "/config.yml"
   with open(config_file,'r') as configuration_file:      
      config = yaml.load(configuration_file) 
      if config is None:
         exit(-1)
      config['host'] = os.environ['STASH_HOST']
      config['stash_port'] = os.environ['STASH_PORT']
      config['stash_git_port'] = os.environ['STASH_GIT_PORT']
      config['stash_home'] = os.environ['STASH_HOME']
except Exception as e:
# If the config file cannot be imported as a dictionary, bail!
   print e
   sys.exit(-1)

if not 'collector_address' in config:
   print "[Error]: Collector address not found in configuration file" 
   sys.exit(-1)

with open(os.environ['VG_HOOK']+"/hook.properties",'w') as f:
   f.write("collector.address="+ config['collector_address'])