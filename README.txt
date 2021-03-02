Commands to run:

(step 1) 1st terminal type: app.py
(step 2) open 2nd terminal and type: ngrok http <port>

in <port> paste the port number you get from 1st step

eg.

(1st terminal)
(venv) >app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

(2nd terminal)

(venv) >ngrok http 5000

ngrok by @inconshreveable                                                                                                                                                                                                  (Ctrl+C to quit)

Session Status                online
Session Expires               1 hour, 59 minutes
Version                       2.3.35
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://44f7b787746a.ngrok.io -> http://localhost:5000
Forwarding                    https://44f7b787746a.ngrok.io -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90     
                              0       0       0.00    0.00    0.00    0.00   


go to facebook for developers and copy paste http://44f7b787746a.ngrok.io created by ngrok into callback url

should be running, test your bot ;)