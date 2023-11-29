# final project requirements

## functionality

* Take the Cloud Run version of the homework code developed previously and adapt it to utilize APIs of your choice. For graduate students, a minimum of 2 API integrations must be implemented for a passing grade.

  * Integrations will be graded on the level of functionality that has been leveraged from the API within the application.
  
  * Note that, as this course is a backend one, integrations must be done within the container running on Cloud Run.

* Development should be organized and incremental, with frequent commits.

* Ensure any API keys do not show up in your source files.

* Configuring credentials for Cloud Run services can be done via environment variables either via Google Cloud's Secrets Manager or in the deployment step using the --set-env-vars flag.

  * e.x. `gcloud run deploy final --image gcr.io/... --set-env-vars APP_ID=e5c9382,API_KEY=cae2635...343`

## screencast

* Show the following in this exact order via screencast once the project is complete.

  * check out the source code from your repo

  * describe the steps one would need to take to run the project, including google cloud configuration e.x. service accounts, enabling APIs

  * Build and deploy the container; pause the screencast to wait for deployment.

  * Demo the app, stepping through all functionality that it supports.

  * Walk through the source code on gitlab and explain how each feature is implemented.

  * Walk through the commit history and describe the timeline of the development process.

  * **The screencast must be less than 15 minutes long.**

## submission

* For your submission,

  * All application code including the Dockerfile should be in the final directory (../).

  * project_url.txt should contain the URL of a live instance of the project running on Cloud Run. This must be left up for a week after submission.

  * publish the screencast as unlisted on mediaspace and include the URL of the video in project_url.txt.
