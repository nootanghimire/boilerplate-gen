import os
from boilerplate_gen.list import list_bp
from boilerplate_gen.info import info_one

import configparser
from subprocess import PIPE, run
from distutils.dir_util import copy_tree



def generate(arguments, appconfig):
  boilerplates = list_bp(appconfig, format='all')

  if not arguments.boilerplate in boilerplates:
    raise Exception('Could not find boilerplate, try checking if it exists using the list command')
  
  if not os.path.isabs(arguments.path):
    arguments.path = os.path.abspath(arguments.path)
    
    do_generate(arguments.boilerplate, arguments.path, appconfig)

def do_generate(boilerplate, path, appconfig):
  print('Generating boilerplate for ' + boilerplate + ' on ' + path)
  print(" ")
  # Get config
  
  bp_config = info_one(boilerplate, appconfig)

  # Validate user env
  # Later: Validate all the depends_on section is installed

  # Prompt user for necessary info and set env vars
  set_proper_env(bp_config)

  bp_dir = appconfig['core_dir'] + os.sep + boilerplate 
  before_copy_script = bp_dir + os.sep + bp_config.get('boilerplate', 'before_copy', fallback='before_copy.py')
  after_copy_script = bp_dir + os.sep + bp_config.get('boilerplate', 'after_copy', fallback='after_copy.py')
  during_install_script = bp_dir + os.sep + bp_config.get('boilerplate', 'during_install', fallback='during_install.py')

  
  # Save current directory 
  cur_dir = os.getcwd()

  # Change dir to bp_dir
  # Suport multiple oses in future
  os.chdir(bp_dir)

  # Run the before copy script if it exists
  if os.path.isfile(before_copy_script) and os.access(before_copy_script, os.X_OK):
    output = out(before_copy_script)
    # Probably needs a flag later on
    print("[OUTPUT FROM BEFORE_COPY_SCRIPT]: ", output)
  else:
    # @todo: if some flag is passed, stop execution here
    if os.path.isfile(before_copy_script) and not os.access(before_copy_script, os.X_OK):
      print("before_copy script is not executable. Please contact boilerplate maintainer")
    else:
      print('Either before_copy script was not provided or we could not find it. Skipping')

  # Get the files to copy
  file_path = bp_dir + os.sep + bp_config.get('boilerplate', 'file_path', fallback='files')

  # Copy them
  copy_tree(file_path, path)

  # Run the after copy script if it exists
  if os.path.isfile(after_copy_script) and os.access(after_copy_script, os.X_OK):
    output = out(after_copy_script)
    # Probably needs a flag later on
    print("[OUTPUT FROM AFTER_COPY]: ", output)
  else:
    # @todo: if some flag is passed, stop execution here
    if os.path.isfile(after_copy_script) and not os.access(after_copy_script, os.X_OK):
      print("after_copy script is not executable. Please contact boilerplate maintainer")
    else:
      print('Either after_copy script was not provided or we could not find it. Skipping')


  # Change to the user specified path 
  os.chdir(path)

  # Perform installation, if script supplied
  if os.path.isfile(during_install_script) and os.access(during_install_script, os.X_OK):
    output = out(during_install_script)
    # Probably needs a flag later on
    print("[OUTPUT FROM DURING_INSTALL]: ", output)
  else:
    # @todo: if some flag is passed, stop execution here
    if os.path.isfile(during_install_script) and not os.access(during_install_script, os.X_OK):
      print("during_install script is not executable. Please contact boilerplate maintainer")
    else:
      print('Either during_install script was not provided or we could not find it. Skipping')




def out(command):
  result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
  return result.stdout

def set_proper_env(config: configparser.ConfigParser):
  if not config.has_section('user_vars'):
    print("Did not find user_vars section on config, moving ahead")
    return

  user_vars = dict(config.items('user_vars'))

  user_vars = {k: (lambda val : val.split(','))(v) for k, v in user_vars.items()}
  final_vars = {k: get_value_from_user(k, v) for k, v in user_vars.items()}
  
  prefix = 'PYTHON_BOILERPLATE_GEN_USERVAR_'
  for k, v in final_vars.items():
    print("Setting var:", prefix + k.upper(), "to ", v)
    os.environ[prefix + k.upper()] = v
  

def get_value_from_user(k, v):
  if v[0] == 'required':
    return get_required_value(k, v)

  return get_optional_value(k, v)  

def get_required_value(k, v):
  while True:
    value = input("Enter value for " + k + " *required*: ")

    if value.strip() == '':
      continue

    return value.strip()

def get_optional_value(k, v):
  value = input("Enter value for" + k + "[optional]: ")

  if value.strip() == '':
    if len(v) > 1:
      value = v[1]  

  return value.strip()
