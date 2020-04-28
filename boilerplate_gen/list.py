import os

def list_bp(app_config, format='grouped'):
  external_dir = app_config['external_dir']
  core_dir = app_config['core_dir']
  external_boilerplates = next(os.walk(external_dir))[1]
  core_boilerplates = next(os.walk(core_dir))[1]

  if format == 'grouped': 
    return {
      'core': core_boilerplates,
      'external': external_boilerplates
    }

  return [] + core_boilerplates + external_boilerplates

def main_list(choice, app_config):
  if choice == 'both':
    print(list_bp(app_config, 'all'))
    return 
  
  list_of_bps = list_bp(app_config)
  
  print(list_of_bps[choice])
