# Locust Sample for RippleMatch

This is a really quick prototype for using [Locust.io](http://Locust.io) to run performance tests against RippleMatch sites. This will allow you to explore the Locust.io web ui, the console output and how the package basically works.

## Steps to get going

1. Clone this repo
2. CD into that directory
3. Run `pip3 install -r requirement.txt`
5. Edit **locustfile.py** to add the password to `yohanan@ripplematch.com` on line 17
6. Save your change

## Running the test

1. In the terminal type `locust --host https://test.ripplematch.com`
2. Open a web browser or tab to [http://localhost:8089](http://localhost:8089) 
3. In the UI, don’t change any values, click **Start Swarming**
3. Sit back and watch locust perform the logins & logouts for `yohanan@ripplematch.com`.


