import time
import hashlib
from faker import Faker
from locust import HttpUser, task, between


class SampleLogin(HttpUser):
    wait_time = between(3, 8)
    clientFingerprint = ''

    @task
    def step1(self):

        # logging in
        loginResponse = self.client.post(
            "/api/v2/auth/token",
            json={"username": "yohanan@ripplematch.com", "password": "{replace me with the passowrd}"},
            headers={"X-DEVICE-FINGERPRINT": self.clientFingerprint}
        )

        time.sleep(3)
        print("Login Response:", loginResponse.status_code)

        recruiterResponse = self.client.get("/match/api/recruiters/")
        time.sleep(3)
        print("Recruiter Response:", recruiterResponse.status_code)
        print("Recruiter Text:", recruiterResponse.text)
        self.client.get("/logout")

    def on_start(self):
        fake = Faker()
        self.clientFingerprint = hashlib.md5(fake.name_nonbinary().encode()).hexdigest()
        print("clientFingerprint: ", self.clientFingerprint)
        self.client.get("/login")

    def on_stop(self):
        print("You killed all the locust")

