module.exports.handler = async event => {
  console.log('Event: ', event)
  const responseMessage = 4867 + 2345

  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      message: responseMessage,
    }),
  }
}
