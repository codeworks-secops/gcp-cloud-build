Motivation
===

Workshop to get familiar with **Google Cloud Build** core concepts  

1 . Build your app
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

* Clone the following project

    [Gtihub Link](https://github.com/codeworks-secops/gcp-cloud-build)

* What about our Application ?

    - The goals of our sample greeting application are multiple : 
 
        - Say `Hello from CodeDay!` when the `/hello` route is invoked
        
        - Say `I'm hamza from CodeDay!` when the `/hello/hamza` route is invoked
        
        - Display an increment counter each time we visit one of the previous routes

* Some screenshots !

    * Route `/hello`

        <img src="screenshots/hello.png" width="550">

    * Route `/hello/<name>`

        <img src="screenshots/hello_name.png" width="550">

* Run the app in your local machine
    
    * Go to the **gcp-cloud-build** project location
        ```bash
        cd PATH_TO_YOUR_LOCAL_REPOSITORY/gcp-cloud-build
        ```

    * Export FLASK_APP environment variable to tell the terminal, the application to work with
        ```bash
        export FLASK_APP=app/app.py
        ```
    * Run the Flask application
        ```bash
        flask run
        ```
    * Check url access (on terminal or browser) 
        ```bash
        http://localhost:5000/hello
        ```

        ```bash
        curl http://localhost:5000/hello
        ```

2 . Architecture
===

* Google Drive 

    [Open here](https://app.diagrams.net/#G1Rv2v0LdO8NnDPH_ZkkR2-fBFLGKx5fmi)

* Screenshot

    <img src="./screenshots/architecture.png" alt="cloud_build_architecture"/>

3 . Initialize Tooling
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
4 . Create a new GCP Project
===
* Get the billing accounts list

    ```bash
    gcloud alpha billing accounts list
    ```

* Get the GCP Folder ID

    ```bash
    GCP_FOLDER_ID=$( gcloud alpha resource-manager folders list --folder=695487100615 --format=json | jq -c '.[] | select( .displayName | contains("GCP"))' | jq '.name' | cut -f 2 -d '/' | sed 's/"//g')
    ```

* Name the project

    ```bash
    # Replace <FIRSTNAME-LASTNAME> with your own value
    PROJECT_ID=codeworks-<FIRSTNAME-LASTNAME>-cbw
    
    # Here's an example
    PROJECT_ID=codeworks-hamza-elyaaqoubi-cbw
    ```
* Create new project

    ```bash
    gcloud projects create ${PROJECT_ID} --folder=${GCP_FOLDER_ID}
    ```

* Get the project number

    ```bash
    PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
    ```

* Link the project to the billing account

    ```bash
    gcloud alpha billing accounts projects link ${PROJECT_NUMBER} --account-id=${REPLACE_WITH_AN_ENABLED_ACCOUNT_ID}
    ```

* Inspects

    * From your terminal
        ```bash
        gcloud projects list
        ```

    * From the Google Cloud Console

5 . Init GCP configuration
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

6 . Enable APIs
===

* Services available to the project to enable. This list will include any services that the project has already enabled.
    
    ```bash
    gcloud services list --available
    ```

* Enable Cloud Run Admin API

    ```bash
    gcloud services enable run.googleapis.com
    ```

* Enable Cloud Build service

    ```bash
    gcloud services enable cloudbuild.googleapis.com 
    ```
* enable Container Registry service

    ```bash
    gcloud services enable containerregistry.googleapis.com 
    ```

7 . Configure IAM permissions
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

8 . Cloud Build Configuration
====

* Open the **cloudbuild.yaml** manifest file located in the root of the project

* What do you think ? 

* Rename this variable **CHANGE_ME_WITH_YOUR_OWN_CLOUD_RUN_SERVICE_NAME** in the manifest file like this :
    
    ```bash
    codeworks-<FIRSTNAME-LASTNAME>-service
    ```

9 . Setup the Cloud Build Trigger
===

* Use the GCP web-based Console

* Choose Push to a branch

* Connect your Github Repository (https://github.com/codeworks-secops)

* Choose gcp-cloud-build project

* Choose only your own branch to be triggered

* Choose the Cloud Build Configutation as Build configuration

* Click CREATE button

10 . Trigger builds
===
* Create a new Git branch with your name

* Commit your local changes

* Push your new branch

11 . Check the GCP Console
===

* Cloud Container Registry

* Cloud Build 

* Cloud Run

12 . Access the deployed application
===

* Pick the URL from the Cloud Run Console

13 . Clean-up all resources
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

* Delete your project using its project ID or project number

    ```bash
    gcloud projects delete $PROJECT_ID
    ```