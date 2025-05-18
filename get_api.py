from locust import HttpUser, task, between
# https://gorest.co.in/
# https://www.postman.com/postman/published-postman-templates/documentation/ae2ja6x/postman-echo?ctx=documentation
# kill -9 2092614
# sudo fuser 8089/tcp
# locust -f get_api.py -u 1 -r 1 -t 60s
class MyUser(HttpUser):
    wait_time =between(1, 2)
    

    @task
    def get_user_api(self):
        self.client.get("/public/v2/users")

    # @task
    # def get_methods(self):
    #     headers ={
    #         'Accept':'Application/Json'
    #     }
    #     with self.client.get('https://postman-echo.com/basic-auth', headers=headers,
    #                          auth=('postman','password'), catch_response=True) as response:
    #         if response.status_code == 200:
    #             value = response.json()
    #             value = value['authenticated']
    #             print(value)
    #             response.success()
    #         else:
    #             response.failure()