module.exports = {
  transform: {
    '^.+\\.tsx?$': 'babel-jest',
    '^(?!.*\\.(js|jsx|mjs|css|json)$)': '<rootDir>/config/jest/fileTransform.js'
  },
  moduleNameMapper: {
    "\\.(css|less)$": "identity-obj-proxy"
  },
  testRegex: '(/__tests__/.*|(\\.|/)(test|spec))\\.(jsx?|tsx?)$',
  testPathIgnorePatterns: [
    '/node_modules/',
    '/build/'
  ],
  moduleFileExtensions: [
    'ts',
    'tsx',
    'js',
    'jsx'
  ],
  collectCoverageFrom: [
    '!src/interface/**/*.ts',
    '!src/config/*.ts',
    '!src/error/*.ts?(x)',
    '!src/index.tsx',
    'src/**/*.ts?(x)'
  ],
  collectCoverage: true,
  coverageDirectory: 'coverage',
  setupFiles: ['<rootDir>/tests/setup.js'],
  setupFilesAfterEnv: ['<rootDir>/tests/setupAfterEnv.js'],
}