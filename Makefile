#
# podman, docker, MyTodo django app
#

#
# variables:
#
APPRUN = python3 manage.py runserver
IMAGE = mytodoapp
APP = mytodoapp
PORT = 8080
ENVIRONMENT = production

# ------------------------------------------------------------------------------------------
# targets:
#
build:
	echo "No need build in Python :)"

run:
	$(APPRUN) 0:$(PORT)

clean:
	echo "No need clean in Python :)"


# Docker-specific targets -------------------------------------------------------------------
local-docker-build:
# docker build -t localhost/$(IMAGE):dev .
	podman build -t localhost/$(IMAGE):dev .


local-docker-run:
# docker run -it --rm --name django --hostname django -p $(PORT):$(PORT) localhost/$(IMAGE):dev
	podman run -it --rm --name mytodo --hostname mytodo -p $(PORT):$(PORT) localhost/$(IMAGE):dev


# GCloud-specific targets --------------------------------------------------------------------
gcloud-docker-init:
	gcloud auth configure-docker
# maybe need in local once:
# gcloud init
# glcoud auth login
# gcloud config set project PROJECT_ID

# GCP Container Registry service:
gcloud-docker-build:
	docker build -t gcr.io/$(GCP_PROJECT_ID)/$(APP):$(ENVIRONMENT) .

gcloud-docker-push:
	docker push gcr.io/$(GCP_PROJECT_ID)/$(APP):$(ENVIRONMENT)

# Google GCP Cloud Run service:
gcloud-run-deploy:
	gcloud run deploy $(APP)-$(ENVIRONMENT) \
	--region europe-west2 \
	--image gcr.io/$(GCP_PROJECT_ID)/$(APP):$(ENVIRONMENT) \
	--port $(PORT) \
	--project $(GCP_PROJECT_ID) \
	--max-instances 1 \
	--platform managed \
	--labels environment=$(ENVIRONMENT) \
	--allow-unauthenticated 

