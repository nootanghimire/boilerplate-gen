import os
import configparser
import argparse

from boilerplate_gen.utils import get_default_config_file, get_core_boilerplates_dir
from boilerplate_gen.generator import generate
from boilerplate_gen.list import main_list
from boilerplate_gen.info import info

def get_app_config(arg_config_file):
  # Instantiate configparser
  config = configparser.ConfigParser()

  # Default config
  defaultConfig  = configparser.ConfigParser()
  defaultConfig.read(get_default_config_file())

  # if there is a config file provided in arg, check if it exists
  if not arg_config_file is None:
    arg_config_file = os.path.abspath(arg_config_file)
    if os.path.isfile(arg_config_file) is False:
      raise FileNotFoundError('File ' + arg_config_file + ' not found')

  # Read configuration file
  config_file = os.environ.get('PYTHON_BOILERPLATE_GEN_CONFIG_FILE')
  if config_file is None:
      config_file = os.environ.get('HOME') + os.sep + '.py-boilerplate-gen' + os.sep + 'config.cfg'

  # Get config if defined, or else, get default config
  if os.path.isfile(config_file):
    config.read(config_file)
  else:
    config.read(get_default_config_file())

  # Get the boilerplates directory from config
  boilerplates_dir = os.path.expanduser(config.get(
    'config',
    'boilerplates_dir',
    fallback=defaultConfig.get('config', 'boilerplates_dir')
  ))

  if not os.path.exists(boilerplates_dir):
    raise FileNotFoundError('Boilerplate directory specified in config not found. Please create the following dir: ' + boilerplates_dir)


  # Get the core boilerplates directory from config
  core_boilerplates_dir = get_core_boilerplates_dir()

  return {
    'external_dir': boilerplates_dir,
    'core_dir': core_boilerplates_dir
  }


def choose_commands(config, arguments):
  subcommand = arguments.subcommand

  if subcommand == 'generate':
    generate(arguments, config)
  if subcommand == 'list':
    print('aa', config)
    main_list(arguments.type, config)
  if subcommand == 'info':
    info(arguments, config)

def parser_setup_and_parse():
  # Start parsing arguments
  parser = argparse.ArgumentParser('boilerplate_gen', description='Generates Boilerplate codes')
  parser.add_argument('-c', '--config', help="path to config file")

  subparsers = parser.add_subparsers(title='commands', description='append -h with each command to see its help', dest='subcommand')


  generator_parser = subparsers.add_parser('generate', help='Generate a boilerplate')
  generator_parser.add_argument('-b', '--boilerplate', help='Boilerplate name', required=True)
  generator_parser.add_argument('-p', '--path', help="path to where you want to generate boilerplate", default=".")
  generator_parser.add_argument('-d', '--dry-run', help="Runs the steps, but does not actually change anything. Good way to debug your config", action='store_true')

  info_parser = subparsers.add_parser('info', help='Get information about particular boilerplate')
  info_parser.add_argument('-b', '--boilerplate', help='Boilerplate name(s)', action='append', required=True)
  # info_parser.add_argument('-l', '--level', help='Level of info ', action='count', default=0)


  list_parser = subparsers.add_parser('list', help='Lists all boilerplates')
  list_parser.add_argument('type', choices=['core', 'external', 'both'])

  namespace = parser.parse_args()

  # See config override
  configFile = namespace.config

  if not configFile is None:
    if not os.path.isabs(configFile):
      config = os.path.abspath(configFile)
      if not os.path.isfile(configFile):
        print("Incorrect config file supplied")
        return
      os.environ['PYTHON_BOILERPLATE_GEN_CONFIG_FILE'] = configFile
  
  
  try:
    config = get_app_config(namespace.config)
    # print(config)
    choose_commands(config, namespace)
  except FileNotFoundError as err:
    print(err)
  # except Exception as ex:
  #   print(ex)

 

if __name__ == '__main__':
  parser_setup_and_parse()
