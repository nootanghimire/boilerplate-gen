#!/usr/bin/env python

import os
import json

def create_files():
  print("Creating package json")
  create_package_json()

def create_package_json():
  vars = get_user_vars()
  # Short for - Package.json dictionary
  pjd = {}

  pjd['name'] = vars['app_name']
  pjd['version'] = vars['app_version']
  pjd['description'] = vars['app_desc']
  pjd['main'] = vars['app_main']
  pjd['scripts'] = {
    'start': 'webpack --mode development --config webpack.dev.config.js',
    'dev': 'webpack-dev-server --mode development --open --hot --config webpack.dev.config.js',
    'build': 'webpack --mode production --config webpack.prod.config.js',
    'test': 'NODE_ENV=test jest --verbose',
    'coverage': 'NODE_ENV=test jest --coverage --coverageReporters html',
    'clear': 'jest --clearCache',
    'lint': 'eslint src/** --ext .ts,.tsx',
    'lint:fix': 'eslint src/** --ext .ts,.tsx --fix'
  }
  
  if vars['repo_url'] != None:
    pjd['repository'] = {
      'type': 'git',
      'url': vars['repo_url']
    }

  if vars['keywords'] != None:
    keywords = vars['keywords'].split(',')
    pjd['keywords'] = keywords
  
  if vars['author'] != None:
    pjd['author'] = vars['author']

  pjd['license'] = 'ISC'

  if vars['bug_url'] != None:
    pjd['bugs'] = {
      'url': vars['bug_url']
    }

  if vars['homepage'] != None:
    pjd['homepage'] = vars['homepage']

  pjd['dependencies'] = {}

  pjd['devDependencies'] = {}

  with open('./files/package.json', 'w') as f:
    json.dump(pjd, f)

'''
Get User vars from environment
app_name=required
app_version=optional,text,1.0.0
app_main=optional,text,index.js
repo_url=optional
keywords=optional,multitext
author=optional
bugUrl=optional
homepage=optional
'''
def get_user_vars():
  dict = {
    'app_name': get_env('APP_NAME'),
    'app_version': get_env('APP_VERSION'),
    'app_desc': get_env('APP_DESC'),
    'app_main': get_env('APP_MAIN'),
    'repo_url': get_env('REPO_URL'),
    'keywords': get_env('KEYWORDS'),
    'author': get_env('AUTHOR'),
    'bug_url': get_env('BUG_URL'),
    'homepage': get_env('HOMEPAGE')
  }

  missingKeys = []
  if dict['app_name'] is None:
    missingKeys.push('app_name')

  if dict['app_version'] is None:
    missingKeys.push('app_version')

  if dict['app_main'] is None:
    missingKeys.push('app_main')

  if dict['app_desc'] is None:
    missingKeys.push('app_desc')

  if len(missingKeys) > 0:
    raise Exception('Missing Values: ' + ",".join(missingKeys))

  return dict

def get_env(var):
  prefix = 'PYTHON_BOILERPLATE_GEN_USERVAR_'
  return os.environ.get(prefix + var)

if __name__ == '__main__':
  create_files()