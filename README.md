# Under Construction

> Dazzle is a docker-compose system for deploying a Django website frontend for [dizzy](https://github.com/GRAYgoose124/dizzy).

## Install and Run

    docker-compose up [-d]

Then in your browser:

    http://localhost?entity=einz&workflow=einzy

Check images/compute/data/.dizzy for project-specific dizzy files.


## TODO:
- [ ] In production we want to remove the /app volumes and instead COPY the /image/x/appfolders into the container.
- [ ] automatic python manage.py collectstatic
- [ ] automatic python manage.py migrate