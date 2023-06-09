import app


def test_handler():
    event = {}
    context = {}
    response = app.handler(event, context)

    print("::set-output name=status_code::{}".format(response['statusCode']))
    print("::set-output name=body::{}".format(response['body']))

    assert response['statusCode'] == 200
    assert response['body'] == '55.5'
