# Dazzle  🚧 Under Construction 🚧

> Dazzle is a docker-compose system for deploying a Django website frontend for [dizzy](https://github.com/GRAYgoose124/dizzy).


Loosely speaking, one makes a request to a backend library with a custom dizzy wrapper. The web uses a `dizzy.daemon.Client` to substantiate this interaction. `compute/data/.dizzy` holds the information and python code for the custom dizzy protocol. See dizzy itself to learn more about customizing dizzy protocols.

S/N: Dizzy itself is very incomplete. [Zmqer](https://github.com/GRAYgoose124/codespace_play/tree/main/zmqer) is a similar experiment which I may merge in achieving RPC-like behaviour with zmq through dizzy.

## See also 

Here's a temporary [demo](http://piedhyper.space) link. Hoping to dedicate a subdomain to this project soon and get a CI/CD pipeline to production release.


## Install and Run

    docker-compose up [-d]

Then in your browser:

    localhost?entity=einz&workflow=einzy

Check images/compute/data/.dizzy for project-specific dizzy files.


## TODO:
- [ ] In production we may want to remove the /app volumes and instead COPY the /image/x/appfolders into the container.
- [ ] automatic python manage.py 
  - [ ] collectstatic
  - [ ] migrate