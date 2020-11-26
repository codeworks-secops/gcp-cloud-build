Build your app
===

* Install Python

    ```bash
    # Check the Python installation
    python --version
    ```
* Install Pip

    ```bash
    # Update your system dependencies
    sudo apt update
    # Intall pip
    sudo apt install python3-pip
    # Check the Pip installation
    pip3 -V
    pip3 --version
    ```

* Install Flask

    ```bash
    # Install flask using pip
    pip3 install flask
    # Check the Flask installation
    flask --version
    ```

* Run your app

    ```bash
    # Export FLASK_APP environment variable to tell the terminal, the application to work with
    export FLASK_APP=app.py
    # Run the Flask application
    flask run
    # Check url access (on terminal or browser) 
    localhost:5000
    ```

Architecture
===

* Google Drive 

    [Open here](https://app.diagrams.net/#G1Rv2v0LdO8NnDPH_ZkkR2-fBFLGKx5fmi)

* Screenshot

    <img src="./screenshots/architecture.png" alt="cloud_build_architecture"/>

Create new GCP Project
===

```bash
# Get billing accounts list
$> gcloud alpha billing accounts list
# Get the Organisation ID
ORGANISATION_ID=$(gcloud organizations describe codeworks.fr --format=json | jq '.name' | cut -f 2 -d '/' | sed 's/"//g')
# Name project
$> PROJECT_ID=codeworks-cloud-build-test
# Create a new project
$> gcloud projects create ${PROJECT_ID} --organization=${ORGANISATON_ID}
# Grab the project number
$> PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
# Link the project to the billing account
$> gcloud alpha billing accounts projects link ${PROJECT_NUMBER} --account-id=0150EE-171E17-3E357F
# Check the console if you want !!!
```

Init GCP Project
===

```bash
# Configure gcloud to match account / project / zone to use from scratch
$> gcloud init
# Display zones list
$> gcloud compute zones list
$> gcloud init
# Checl all of the configuration
$> gcloud config list
```

Enable APIs
===

* Cloud Build

* Cloud Run

* Container Registry

Configure IAM permissions
====

Cloud Build requires **Cloud Run Admin** and **IAM Service Account User** permissions before it can deploy an image to Cloud Run.

- Grant the **Cloud Run Admin** role to the **Cloud Build** service account, so it will have permissions to deploy the Cloud Run service.

    ```bash
    gcloud projects add-iam-policy-binding $PROJECT_ID \
        --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
        --role=roles/run.admin
    ```

- Grant the **IAM Service Account User** role to the **Cloud Build** service account for the Cloud Run runtime service account. So the Cloud Run service may be configured to allow access from unauthenticated users.

    ```bash
    gcloud iam service-accounts add-iam-policy-binding \
        $PROJECT_NUMBER-compute@developer.gserviceaccount.com \
        --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
        --role=roles/iam.serviceAccountUser
    ```

Configuring our Cloud Build Pipeline
====

* Open the **cloudbuild.yaml** manifest file in the root of the project

Set Up the Cloud Build Trigger
===

* Use the GCP web-based console

* Connect a Github Repository or Cloud Source Repository

Triggering builds
===

* Commit your changes

* Push your changes

Check the console
===

* Cloud Container Registry

* Cloud Build 

* Cloud Run

Accessing the deployed application
===

* Get the URL from Cloud Run console

Clean-up
===

* Delete the deployed Cloud Run service
    
    ```bash
    $> gcloud beta run services list
    
    $> gcloud beta run services delete SERVICE_NAME
    ```

* Delete the Container Registry saved images

    ```bash
    $> gcloud container images list

    $> gcloud container images delete IMAGE_NAME
    ```

* Delete the Cloud Build configured triggers


* Disconnect any connected repositories