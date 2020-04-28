#!/usr/bin/env python

import os
from subprocess import run, PIPE

def install_packages():
  print("Adding dependencis")

  packages = [ 
    "axios",
    "dot-prop",
    "http-status-codes",
    "lodash",
    "moment",
    "react",
    "react-animations",
    "react-barcode",
    "react-dom",
    "react-modal",
    "react-redux",
    "react-router-dom",
    "react-shimmer",
    "react-tabs",
    "redux",
    "redux-devtools-extension",
    "redux-observable",
    "rxjs",
    "styled-components"
  ]

  command = ["npm", "install", "--save"]

  output = out(' '.join(command + packages))
  print(output)


def install_dev_packages():
  print("Adding dev dependencis")
  
  packages = [
    "@babel/runtime",
    "@types/styled-components",
    "@babel/core",
    "@babel/plugin-proposal-optional-chaining",
    "@babel/plugin-transform-runtime",
    "@babel/preset-env",
    "@babel/preset-react",
    "@babel/preset-typescript",
    "@testing-library/jest-dom",
    "@testing-library/react",
    "@types/jest",
    "@types/lodash",
    "@types/react",
    "@types/react-dom",
    "@types/react-modal",
    "@types/react-redux",
    "@types/react-router-dom",
    "@types/react-tabs",
    "@types/redux-mock-store",
    "@typescript-eslint/eslint-plugin",
    "@typescript-eslint/parser",
    "axios-mock-adapter",
    "babel-loader",
    "babel-plugin-module-resolver",
    "clean-webpack-plugin",
    "css-loader",
    "eslint",
    "eslint-config-airbnb",
    "eslint-config-airbnb-typescript",
    "eslint-config-prettier",
    "eslint-plugin-import",
    "eslint-plugin-jest",
    "eslint-plugin-jsx-a11y",
    "eslint-plugin-prettier",
    "eslint-plugin-react",
    "eslint-plugin-react-hooks",
    "faker",
    "file-loader",
    "html-loader",
    "html-webpack-plugin",
    "identity-obj-proxy",
    "jest",
    "jest-css-modules-transform",
    "mini-css-extract-plugin",
    "prettier",
    "readme-md-generator",
    "redux-mock-store",
    "snapshot-diff",
    "source-map-loader",
    "style-loader",
    "terser-webpack-plugin",
    "ts-jest",
    "tslint",
    "tslint-config-airbnb",
    "tslint-react",
    "typescript",
    "webpack",
    "webpack-cli",
    "webpack-dev-server"
  ]

  command = ["npm", "install", "--save-dev"]

  output = out(' '.join(command + packages))
  print(output)

def out(command):
  result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
  return result.stdout

if __name__ == '__main__':
  install_packages()
  install_dev_packages();