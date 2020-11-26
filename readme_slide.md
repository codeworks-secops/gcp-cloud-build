Cloud Build
===

- Benefits
    
    * Fully serverless platform : 
        
        Cloud Build scales up and scales down in response to load with no need to pre-provision servers or pay in advance for additional capacity.
        
        Pay only for what you use.

    * Flexibility : 

        With custom build steps and pre-created extensions to third party apps, enterprises can easily tie their legacy or home-grown tools as a part of their build process.

    * Security and compliance : 

        Guard against security threats in your software supply chain with vulnerability scanning.
        
        Automatically block deployment of vulnerable images based on policies set by DevSecOps.

- Key features
    
    * Extremely fast builds

        Access machines connected via Google’s global network to significantly reduce your build time.
        
        Run builds on high-CPU VMs or cache source code, images, or other dependencies to further increase your build speed.

    * Automate your deployments

        Create pipelines as a part of your build steps to automate deployments.
        
        Deploy using built-in integrations to Google Kubernetes Engine, App Engine, Cloud Functions, and Firebase.
        
        Use Spinnaker with Cloud Build for creating and executing complex pipelines.

    * Support for multi-cloud

        Deploy to multiple clouds as a part of your CI/CD pipeline.
        
        Cloud Build comes with builder images which have languages and tools already installed.
        
        Likewise containerized tasks of Cloud Build are fully portable across different clouds.

    * Commit to deploy in minutes

        Going from PR to build, test, and deploy can’t be simpler.
        
        Set up triggers to automatically build, test, or deploy source code when you push changes to GitHub, Cloud Source Repositories, or a Bitbucket repository.

    * Unparalleled privacy

        Run builds on infrastructure protected by Google Cloud security.
        
        Get full control over who can create and view your builds, what source code can be used, and where your build artifacts can be stored.

    * Native Docker support

        Just import your existing Docker file to get started. Push images directly to Docker image storage repositories such as Docker Hub and Container Registry.
        
        Automate deployments to Google Kubernetes Engine or Cloud Run for continuous delivery.

    * Identify vulnerabilities

        Identify package vulnerabilities for your container images.
        
        Automatically perform package vulnerability scanning for Ubuntu, Debian, and Alpine.

    * Build locally or in the cloud

        Run builds locally before submitting to the cloud.
        
        Build and debug on your local machine with the open source local builder.

- Pricing

    * Pay for what you use above a daily free tier.


        FEATURE	                                PRICING (USD)

        First 120 build-minutes per day	        Free
        
        Additional build-minutes	            $0.003 per minute

    * If you pay in a currency other than USD, the prices listed in your currency on Google Cloud SKUs apply.

- Deployment pipeline on GCP

    * Cloud Build : [Docs](https://cloud.google.com/cloud-build/docs)

    * Container Registry : [Docs](https://cloud.google.com/container-registry/docs/overview)

    * Cloud Run : [Docs](https://cloud.google.com/run/docs)

    * IAM Permissions

- Configuring a specific pipeline
    
    * Watches a Github Repository

    * Build the Docker image
    
    * Push the Docker image into Container Registry
    
    * Deploy the Docker image on Cloud Run

