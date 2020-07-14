# Sample Django App

A skeleton for new projects prepared to become large applications
Ready to deploy on Heroku

## Features

- [x] Common models for document and image uploads, user addresses, and notes
- [x] Use [django-simple-history](https://github.com/jazzband/django-simple-history) to keep record of historical model state on every create/update/delete

- [x] Model Behaviors, Inspired by Kevin Stone's [Django Model Behaviors](http://blog.kevinastone.com/django-model-behaviors.html).
  - [x] Authorable: add assign user as author/creator and toggle public anonymity
  - [x] Annotatable: add authored notes to any model
  - [x] Expirable: set validitidy and expiration dates
  - [x] Permalinkable: set url slug and define url pattern (great for blog posts or user profiles)
  - [x] Publishable: set dates for publishing and editing
  - [x] Timestampable: created_at and modified_at dates - great to add on all models (Rails has this on all models by default)
  - [x] Uploadable: connect a model dircetly to all your file uploading features (great for documents

- [x] Communication App Models
  - [x] Email
  - [x] SMS
  - [x] Slack, Telegram

- [x] Enhanced Default User Model
  - [x] email verification
  - [x] can use phone number instead of email for login, password reset
  - [x] check has agreed to latest legal T&C
  - [x] [OTP code](https://gist.github.com/tomcounsell/78d0a587b6107369792f1e05471e50cc)
  - [x] Facebook login tokens

- [x] Common Utilities
  - [x] AWS S3 and SQS connection methods
  - [x] multithreading - see [related SO answer](https://stackoverflow.com/a/28913218)
  - [x] WritableSerializerMethodField for Django Rest Framework
  - [x] WhoIs domain lookups
  - [x] Transloadit integration methods
  - [x] Auth tokens for JWT
  - [x] Wordwide language codes for your L11N
  - [x] [Iommi](https://github.com/TriOptima/iommi) classes
  


## Docker
1. How to install docker
  - go to this page `https://docs.docker.com/docker-for-mac/` and Follow first step

2. How to run develop environment
  - `docker-compose up --build`

3. How to stop develop environment
  - `docker-compose stop`

4. How to shell to develop environment
  - `docker-compose exec web bash`

5. How to run test
  - `docker-compose exec web python manage.py test`

6. Install new pagkage in requirement.txt have to build docker again(ps. It like a vagrant destroy and vagrant up again, all data gone)
  - `docker-compose down && docker-compose up --build`

7. Check test coverage
  - shell to docker `docker-compose exec web bash`
  - run test coverage `coverage run manage.py test`
  - see report `coverage report`
  - Ps you can run on your host sever for example `docker-compose exec web coverage run manage.py test`

