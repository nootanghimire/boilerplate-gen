import os

from boilerplate_gen.list import list_bp
import configparser

def info(arguments, app_config):
  infos = []
  for b in arguments.boilerplate:
    infos.append(dict(info_one(b, app_config)[0].items('boilerplate')))
    
  print(infos)

def info_one(boilerplate, app_config):
  list_of_bps = list_bp(app_config, 'grouped')

  bp_info = {
    'type': 'does not exist'
  }

  if  boilerplate in list_of_bps['core']:
    bp_info['type'] = 'core'
  elif boilerplate in list_of_bps['external']:
    bp_info['type'] = 'external'
  else:
    raise Exception('Could not find boilerplate, try checking if it exists using the list command')

  path = app_config['core_dir'] + os.sep + boilerplate

  if bp_info['type'] == 'external':
    path = app_config['external_dir'] + os.sep + boilerplate
  
  bp_config = configparser.ConfigParser()
  bp_config_path = path + os.sep + 'config.cfg'
  if not os.path.isfile(bp_config_path):
    raise Exception('Boilerplate is invalid, it does not have a config file')

  bp_config.read(path + os.sep + 'config.cfg');

  return (bp_config, path)

