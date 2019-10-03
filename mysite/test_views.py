def test_index_ok(client):
    #Make a GET request to / and store the response object
    #using the Django test clientself.
    response = client.get('/banana')
    #Assert that the status_code == 200 (OK)
    assert response.status_code == 200
