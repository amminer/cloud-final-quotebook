# Dockerfile.large

* Take the hw2 application and contstruct a container using Ubuntu 20.04 as a base layer.

* This command should build the container locally:

    `docker build -f Dockerfile.large -t amminer/hw3large .`

# Dockerfile.small

* Take the hw2 app and construct a container that employs a base Linux image that's as small as possible (i.e. python-alpine?) Tips for shrinking containers [here](https://docs.docker.com/build/building/multi-stage/) [here](https://blog.codeship.com/reduce-docker-image-size/) and [here](https://codefresh.io/docker-tutorial/not-ignore-dockerignore-2/).

* This command should build the container locally:

    `docker build -f Dockerfile.small -t amminer/hw3small .`


# Docker Hub Submission

* Upload both images to your Docker Hub account.

# screenshots.pdf

Using a google doc, collect

* The size of both containers on Docker Hub (2 screenshots)

* On the Ubuntu VM, delete all containers and images (`docker ps`, `docker stop`, `docker rm`, `docker rmi`) then instantiate each container image on Docker Hub, ensuring it maps Ubuntu's port 8000 to the container's port 5000. Show console output displaying container images being pulled. Perform a wget to the container's port 5000 and show that it returns the landing page.
