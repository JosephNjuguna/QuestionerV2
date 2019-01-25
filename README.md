# QuestionerV2
Questioner V2 uses Postresql Database without ORM.

 `language : Python`

**Badges**
[![Build Status](https://travis-ci.org/JosephNjuguna/QuestionerV2.svg?branch=develop)](https://travis-ci.org/JosephNjuguna/QuestionerV2)
[![Maintainability](https://api.codeclimate.com/v1/badges/0d21ec27baca9ef2c0fd/maintainability)](https://codeclimate.com/github/JosephNjuguna/QuestionerV2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0d21ec27baca9ef2c0fd/test_coverage)](https://codeclimate.com/github/JosephNjuguna/QuestionerV2/test_coverage)

**Badges**
## Getting started
---
This is a Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize
questions to be answered. Other users can vote on asked questions and they bubble to the top
or bottom of the log.

Visit the Questioner UI templates on :

https://josephnjuguna.github.io/Questioner/UI/templates/ 

Get the Questioner API on : 

https://questioner123.herokuapp.com/

## Prerequisites
what you need for the app to run ??

#### `postman`
#### `terminal of your choice`

**Installing**

1. open your terminal
2. copy the link below and clone this repo on your machine
```
git clone https://github.com/JosephNjuguna/Questioner.git
```
3. after cloning the repo open your change directory into this repo folder  by running following command :

```
cd Questioner
```

4. Setting up Virtualenv
   
   ```bash
    virtualenv venv

   ```

   Activation

   ```bash
    source .env
   ```

5. Installing dependencies

    ```bash
      pip install -r requirements.txt
    ```

**Running the App**

1. then run the following command on the terminal to start the app 

```
flask run
```
5. Open Postman app  and  navigate into following api endpoints:

| FEATURES                          | API ENDPOINT                                           |
| --------------------------------- | ------------------------------------------------------ |
| user sign up                      | [POST] /api/v2/auth/signup                             |
| user log in                       | [POST] /api/v2/auth/login                              |
| create meetup                     | [POST]  /api/v2/meetup  
| user view upcoming meetups        | [GET]  /api/v2/meetup/upcoming
| user view specific meetup details | [GET]  /api/v1/meetup/upcoming/<meetup:id>/ 
| user delete specific meetup details|[DELETE]  /api/v1/meetup/upcoming/<meetup:id>/delete                   |
| user RSVP for a meetup            | [POST] /api/v1/meetup/<meetup:id>/rsvp   
| user post a question              | [POST] /api/v1/meetup/<meetup:id>/question   
| user get a specific question      | [GET] /api/v1/meetup/<meetup:id>/question/<question:id> |
| user comment a specific question  | [GET] /api/v1/meetup/<meetup:id>/question/<meetup:id>/comment |
| user upvote question              | [PATCH]/api/v1/questions/<question:id>/upvote                 |
| user downvote question            | [PATCH]/api/v1/questions/<question:id>/downvote               |



**Running Test**
---
open the project with terminal/cmd and
at the root of the folder run 

`python -m pytest`

you will get to run atleast 12 test for the app

### AVAILIABLE FEAUTURES

#### AUTHENTICATION
  1. USER SIGN UP 
  2. USER LOG IN

 #### MEETUP

1. USER RSVP FOR A MEETUP
2. USER GET SPECIFIC RECORDS OF A MEETUP
3. USER GET ALL UP COMING MEETUPS
4. USER GET RECORD OF SPECIFIC QUESTION IN A MEET UP
5. USER DELETE MEETUP
 
#### QUESTION
 1. USER CAN POST QUESTION
 2. USER CAN UPVOTE QUESTION 
 3. USER CAN DOWNVOTE QUESTION


### BUILT WITH:
>Flask - Python MicroFramework

>Python 3.6



## API VERSION
```
v2
```
### Authors 

JosephNjuguna
