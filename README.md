# Flask and Heroku
## _Deploying a python flask app using Heroku and pipelines to implement a deployment workflow with staging environment_
------------------------------
### Heroku Account Setup
The first step is to create a [Heroku account](https://signup.heroku.com/), If you don't already have one:
### Heroku CLI
The **Heroku** command line interface is a tool that allows you to create and manage Heroku applications from the terminal.
Install the CLI from the following link (you also need GIT insalled as well):
[![N|Download](https://drive.google.com/uc?export=view&id=12ClfpbqNAUZHwyEyvwBqripzJ55vwLIL)](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

Next, you have to login by running the following command:
```sh
heroku login
```
This will open a website to complete the login process.
After logging in, you're ready to start using the **Heroku CLI** to manage your applications and workflows.

### Deploy application to Heroku
Depoly your web application to Heroku using **Heroku CLI** and **GIT**.
First step is to create a file named _Procfile_ (with a capital P) in the project's root directory:
```sh
echo "web: gunicorn app:app" > Procfile
```

If you are working on windows, make sure the file is in UTF-8 encoding (via notepad++) 
Next up, install Gunicorn in your virtual environment and update the requirements file:
```sh
python -m pip install gunicorn
python -m pip freeze > requirements.txt
```
Your virtual env should be up to date with the latest version in the git repo.
Now we can create our Heroku application by running the following command:
```sh
heroku create my-app-name --remote prod
```
This should create a Git remote named prod (instead of the default heroku).
You can verify that by running:
```sh
git remote -v
```
Next, push the git repo to this remote to build and deploy your app:
```sh
git push prod master
```
Our application is now online!
We can use the following command to open our application URL:
```sh
heroku open
```
You can make changes to your app (for example app.py file), commit them and then push the changes to heroku remote:
```sh
git add app.py
git commit -m "change somthing in the welcome screen app.py file"
git push heroku master
```
### Heroku pipelines
We will create three environments for our application:
- Development - our local wroking station
- Staging - or preprod used for review and testing (Heroku)
- Production - live site accessed by users (Heroku)

Create a new Heroku app for staging and depoly the application to it using git:
```sh
heroku create my-app-name-staging --remote staging
git push staging master
```
Now that we have two Heroku applications for production and staging, we can create a pipeline to link them togehter:
```sh
heroku pipelines:create --app my-app-name --stage production my-app-name-pipeline
```
Create a new pipeline named _my-app-name-pipeline_ and add the app named _my-app-name_ as the production environment.

Next, we will add the staging application to the same pipeline:
```sh
heroku pipelines:add --app my-app-name-staging --stage staging my-app-name-pipeline
```
Now our pipeline consists of two apps:
- my-app-name (prod)
- my-app-name-staging (stg)

### Depolying and promoting to Staging and Production
Say we made some changes to our app and we want to deploy it to staging for review and test:
```sh
git add app.py
git commit -m "some change to app.py"
git push staging master
```
Production environment is still using the previous version.
Only then, when we are happy with the cahnges,  we can promote our new application version to production:
```sh
heroku pipelines:promote --remote staging
```
