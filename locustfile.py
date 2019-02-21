from locust import HttpLocust, TaskSet, task
 
class UserDefinedTask(TaskSet):
    def on_start(self):
        """ call when locust start i.e before exection of tasks"""
        pass
 
    @task(2)
    def home(self):
        self.client.get("/", verify=False)
 
    @task(1)
    def other(self):
        self.client.get("/dqt", verify=False)


class User(HttpLocust):
    """
    Each user wait between 5 and 9 seconds before
    running a new request.
    """
    task_set = UserDefinedTask
    min_wait=5000
    max_wait=9000
