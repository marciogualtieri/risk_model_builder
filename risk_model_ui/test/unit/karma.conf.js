var webpackConfig = require('../../webpack.config');

module.exports = function (config) {
  config.set({
    browsers: ['Chrome'],
    frameworks: ['mocha', 'sinon-chai'],
    reporters: ['spec', 'coverage'],
    files: [
      {pattern: '../../src/**/*.js', watched: false},
      {pattern: './test.utils.js', watched: false},
      {pattern: './**/*.spec.js', watched: false}
    ],

    preprocessors: {
      // add webpack as preprocessor
      './test.utils.js': ['webpack'],
      './**/*.spec.js': ['webpack'],
      '../../src/**/*.js': ['webpack', 'coverage']
    },
    plugins: [
      // Launchers
      'karma-chrome-launcher',

      // Test Libraries
      'karma-mocha',
      'karma-sinon-chai',

      // Preprocessors
      'karma-webpack',
      'karma-sourcemap-loader',

      // Reporters
      'karma-spec-reporter',
      'karma-coverage'
    ],
    webpack: webpackConfig,
    webpackMiddleware: {
      noInfo: true
    },
    coverageReporter: {
      dir: './coverage',
      reporters: [
        { type: 'lcov', subdir: '.' },
        { type: 'text-summary' }
      ]
    },
    client: {
      captureConsole: false
    }
  })
}