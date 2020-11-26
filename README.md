Motivation
===

Workshop to get familiar with Google Cloud Build core concepts  

Build your app
===

* Install Python

* Check the Python install

    ```bash
    python --version
    ```
* Install Pip

    * Update your system dependencies
        ```bash
        sudo apt update
        ```
    * Intall pip
        ```bash
        sudo apt install python3-pip
        ```
    * Check the Pip installation
        ```bash
        pip3 -V
        pip3 --version
        ```

* Install Flask

    * Install flask using pip
        ```bash
        pip3 install flask
        ```
    * Check the Flask installation
        ```bash
        flask --version
        ```

* Run your app

    * Export FLASK_APP environment variable to tell the terminal, the application to work with
        ```bash
        export FLASK_APP=app.py
        ```
    * Run the Flask application
        ```bash
        flask run
        ```
    * Check url access (on terminal or browser) 
        ```bash
        localhost:5000
        ```

Architecture
===

* Google Drive 

    [Open here](https://app.diagrams.net/#G1Rv2v0LdO8NnDPH_ZkkR2-fBFLGKx5fmi)

* Screenshot

    <img src="./screenshots/architecture.png" alt="cloud_build_architecture"/>

Initialize Tooling
===

- Install Google Cloud SDK
    
    * [Official install docs](https://cloud.google.com/sdk/docs/install)
    
    * Make sure that Python is installed in your machine

    * Download the latest version
        ```bash
        curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-319.0.0-linux-x86.tar.gz
        ```
    * Unzip the archive
        ```bash
        tar zxvf google-cloud-sdk-319.0.0-linux-x86
        ```
    * Launch the **instal.sh** script
        ```bash
        ./google-cloud-sdk/install.sh
        ```
    * Verify your local installation
        ```bash
        ./google-cloud-sdk/install.sh --help
        ```
Create new GCP Project
===
* Get the billing accounts list

    ```bash
    gcloud alpha billing accounts list
    ```

* Get the Organisation ID

    ```bash
    ORGANISATION_ID=$(gcloud organizations describe codeworks.fr --format=json | jq '.name' | cut -f 2 -d '/' | sed 's/"//g')
    ```
* Name the project

    ```bash
    PROJECT_ID=codeworks-cloud-build-test 
    ```
* Create new project

    ```bash
    gcloud projects create ${PROJECT_ID} --organization=${ORGANISATON_ID}
    ```

* Get the project number

    ```bash
    PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
    ```

* Link the project to the billing account

    ```bash
    gcloud alpha billing accounts projects link ${PROJECT_NUMBER} --account-id=0150EE-171E17-3E357F
    ```

* Inspects

    * From your terminal
        ```bash
        gcloud projects list
        ```

    * From the Google Cloud Console

Init GCP Project
===

* Configure the gcloud tool to match account / project / zone to use from scratch
    ```bash
    gcloud init
    ```
* Display zones list
    ```bash
    gcloud compute zones list
    ```
* Another init !! to init the compute zone
    ```bash
    gcloud init
    ```

* Checl all of the configuration
    ```bash
    gcloud config list
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

* Open the **cloudbuild.yaml** manifest file located in the root of the project

Set Up the Cloud Build Trigger
===

* Use the GCP web-based console

* Connect a Github Repository

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
    gcloud beta run services list
    
    gcloud beta run services delete SERVICE_NAME
    ```

* Delete the Container Registry saved images

    ```bash
    gcloud container images list

    gcloud container images delete IMAGE_NAME
    ```

* Delete the Cloud Build configured triggers


* Disconnect any connected repositories