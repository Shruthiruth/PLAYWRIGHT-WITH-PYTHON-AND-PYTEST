

def test_api(playwright):
    request = playwright.request.new_context(
    #     extra_http_headers={
    #         "Accept": "application/json",
    #         "Authorization": "Bearer mysecrettoken"
    #         }
     )
    
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == 1
    
    request.dispose()
    print("API test completed successfully.")