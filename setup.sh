docker image build -t web_security_demo .
docker run -d -p 5000:5000 --read-only --name web_security_demo web_security_demo