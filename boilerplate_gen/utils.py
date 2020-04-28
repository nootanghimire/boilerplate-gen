import os

def get_package_root():
    """Returns package root folder."""
    return os.path.dirname(os.path.abspath(__file__))

def get_default_config_file():
  """Returns default config filepath"""
  return get_package_root() + os.sep + 'config.default.cfg'

def get_core_boilerplates_dir():
  """Returns core boilerplates directory"""
  return get_package_root() + os.sep + 'core_boilerplates'