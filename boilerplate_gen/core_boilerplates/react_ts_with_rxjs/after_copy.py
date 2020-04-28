#!/usr/bin/env python

import os

def remove_files():
  print("Removig package.json from boilerplate folder")
  os.remove('./files/package.json')

if __name__ == '__main__':
  remove_files()