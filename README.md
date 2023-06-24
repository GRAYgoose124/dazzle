# Under Construction

> Dazzle is a docker-compose system for deploying a Django website frontend for [dizzy](https://github.com/GRAYgoose124/dizzy).

## Install and Run

    docker-compose up

Then in your browser:

http://localhost:8000/dizzy/?entity=einz&workflow=einzy

Check images/compute/data/.dizzy after first run to see the generated dizzy files. 

TODO: The .dizzy files will be committed in the future as the website is developed and API is fleshed out.


## TODO:
- [ ] In production we want to remove the /app volumes and instead COPY the /image/x/appfolders into the container.