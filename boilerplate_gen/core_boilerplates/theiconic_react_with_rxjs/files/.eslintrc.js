module.exports = {
  env: {
    browser: true,
    es6: true,
    jest: true
  },
  extends: [
    'airbnb',
    'airbnb-typescript',
    'airbnb/hooks',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended',
    'prettier/@typescript-eslint',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  settings: {
    'import/resolver': {
      node: {
        extensions: ['.js', '.jsx', '.ts', '.tsx', '.d.ts'],
      }
    }
  },
  plugins: ['react', '@typescript-eslint', 'react-hooks', 'prettier'],
  rules: {
    'react/jsx-filename-extension': [1, { 'extensions': ['.js', '.tsx'] }],
    'react/destructuring-assignment': [0, 'always', { 'ignoreClassFields': true }],
    'react/jsx-one-expression-per-line': [0],
    'react/jsx-wrap-multilines': [0],
    'max-len': [2, {'code': 120, 'tabWidth': 2, 'ignoreUrls': true}],
    'import/no-unresolved': [2, { ignore: ['^\@\/'] }],
    'jsx-a11y/no-autofocus': [0],
    'jsx-a11y/aria-role': [0],
    'no-shadow': [2, { 'builtinGlobals': true, 'hoist': 'all', 'allow': [] }],
    'class-methods-use-this': [0],
    'import/extensions': [2, {'ts': 'never'}],
    'import/prefer-default-export': [0],
  },
};