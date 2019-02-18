from locust import HttpLocust, TaskSet, task
 
class UserDefinedTask(TaskSet):
    def on_start(self):
        """ call when locust start i.e before exection of tasks"""
        pass
 
    @task(2)
    def home(self):
        self.client.get("/", verify=False)
 
class User(HttpLocust):
    task_set = UserDefinedTask
    min_wait=5000
    max_wait=9000
