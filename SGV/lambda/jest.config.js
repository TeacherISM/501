export default {
    transform: {
      '^.+\\.m?js$': 'babel-jest'
    },
    reporters: [
    'default',
    ['jest-html-reporters', {
      publicPath: './test-report',
      filename: 'test-report.html',
      pageTitle: 'Test Report',
      includeFailureMsg: true,
      includeConsoleLog: true
    }]
  ]
  };
  