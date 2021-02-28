![GaffCo Consulting Logo](https://github.com/NaoiseGaffney/CI-PTD-II/blob/development/Documentation/Gaffco_Logo.png)

# GaffCo Consulting Professional Training and Development: Professional Communication and Presentation Skills E-Commerce Website

Professional Communication and Presentation Skills - 4th Milestone Project for the Code Institute's Diploma in Full Stack Development. Project requirements: HTML 5, CSS 3, JavaScript, Python 3, Django, PostgreSQL, and API's. This project website is an e-commerce site for a Professional Communications and Presentation Skills Company (Sole Trader) called GaffCo Consulting.
 
Model-View-Template: Model -> View -> URL -> Template or Form -> View -> URL -> Template
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment
### GitHub

1. Create GitHub Repository using the CI Full Template.
2. Create a development branch (master + development).

### Configure Visual Studio Code environment

3. New Window.
4. Clone Repository -> GitHub -> [Training-and-Development](https://github.com/NaoiseGaffney/Training-and-Development).
5. Select development branch.
6. Create a virtual Python environment - Terminal: `python3 -m venv .venv`
7. Activate virtual Python environment - Terminal: `source .venv/bin/activate`
8. Install Django 3.1 - Terminal: `pip3 install Django`
9. Upgrade pip - Terminal: `pip3 install pip --upgrade`
10. Check Django version - Terminal: `python3 -m django --version` = 3.1.7
11. Update `.gitignore` to include `.venv` and `/Snippets`(my local test and fail code directory).

### Create the Initial Django Project

12. Create a Django **Project** called "Training" - Terminal: `django-admin startproject Training .` (created in the current folder)
13. Verify that the initial Django project works - Terminal: `python3 manage.py runserver 8000`, `http://127.0.0.1:8000/`

### Django Migrations (Version Control System for the Database Schema)'

> *migrate*, which is responsible for applying and unapplying migrations.
>
> *makemigrations*, which is responsible for creating new migrations based on the changes you have made to your models.
>
> *sqlmigrate*, which displays the SQL statements for a migration.
>
> *showmigrations*, which lists a project’s migrations and their status.

Link: https://docs.djangoproject.com/en/3.1/topics/migrations/
14. Apply the initial Django migrations: `python3 manage.py migrate`, add `--plan`to validate before commit.
15. Create Django Admin superuser account: `python3 manage.py createsuperuser`, `gaff`, `naoise.gaff.gaffney@gmail.com`, `password...


### Heroku Platform Configuration and Deployment

16. Install gunicorn: `pip3 install gunicorn`, create requirements.txt using `pip3 freeze > requirements.txt`, and create the Procfile: `web: gunicorn myshop.wsgi:application`.
17. Create `.slugignore`with `/Documentation` and `README.md` as we don't want the documentation to upload to Heroku.
18. Link: https://dashboard.heroku.com/apps.
19. VS Code Source Control: `Stage All Changes` -> `Commit All` -> `Push`.
20. Create a new Pipeline: `training-and-development` and connect to GitHub Repository https://dashboard.heroku.com/pipelines/NaoiseGaffney/Training-and-Development.
21. Enable Review Apps: `Create new review apps for new pull requests automatically` and region: `Europe` -> GitHub. New App -> GitHub *development* branch. Name: `training-and-development-<random sequence>`
22. Add app to Heroku *Staging* (GitHub). Create new app: `Create new review apps for new pull requests automatically` and region: `Europe` -> GitHub. New App -> GitHub *master* branch. Name: `training-and-development`.
23. Add app to Heroku *Production*: `Europe` -> GitHub. Name: `training-and-development-prod`.
24. Add `DISABLE_COLLECTSTATIC = 1` to Review App, Staging App, and Production App Configuration Variables (temporary until AWS S3 Bucket configured).

### Configure static and media for Django

25. Create the media folder in the Project root.
26. Create the static folder with the following sub-folders: scripts (js), scripts/vendors (vendor js), styles (css).
27. Configure 'settings.py' and 'urls.py' to accommodate the static and media folders.

### Install django-environ to read a .env file with both confidential and useful variables -> Heroku Variables

28. Link: https://django-environ.readthedocs.io/en/latest/.
29. Install: `pip3 install django-environ`.
30. Configure `settings.py` to use django-environ and copy `.env` file from previous Django Project.

```
from pathlib import Path
import os
import environ

root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
environ.Env.read_env()  # reading .env file
...
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')
```

#### Django Training Project Applications

* Training (Project)
* home
* account
* shop
* cart
* orders
* payment


Work order (some steps are optional, and some dependent on previous steps): Application -> Models -> Admin Views -> Makemigrations and Migrate -> Classes -> Forms -> Views -> Application URL's -> Project URL's -> Templates.

Create application `python3 manage.py startapp <app-name>`.
Add application to `Training/settings.py` INSTALLED_APPS before `'django.contrib.admin',`.
Create a new models (database schema) file in `<app-name>/models.py`.
Create new admin views for the models created previously in `<app-name>/admin.py` -> `<app-name>/models.py`.
Run `python3 manage.py makemigrations` followed by `python3 manage.py migrate`.
Create a new python file with classes and methods (functions).
Update and/or create a form in `<app-name>/forms.py` -> ClassName in python file.
Update and/or create a View in `<app-name>/views.py` -> FormName in `<app-name>/forms.py`.
Update and/or create a URL in `<app-name>/urls.py` -> ViewName in `<app-name>/views.py`.
Update Django Project URL in `Training/urls.py` -> `<app-name>/urls.py`.
Create a template in `<app-name>/templates/<app-name>` -> `<app-name>/urls.py`.


#### Create a Context Processor to (instead of using Django Signals) to make the Cart Update Global

Create `cart/context_processor.py` context processor called `cart`.
Update `settings.py` with the new context processor -> `cart/context_processors.py` in TEMPLATES.

#### Styling and Layout using Materialize CSS 1.0.0

CSS classes in HTML templates and 'base.css'.

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from my first Code Institute Milestone Project, a Training and Development website. I have turned it into an e-commerce site, and will fork this to expand upon it further to turn it into a professional Training and Development Learning and Content Management System.
- I clearly relied heavily upon the Boutique_Ado walkthrough, NetNinja, Udemy Course, and YouTube videos to understand and apply the concepts for this project.
- My Code Institute mentor Spencer Barriball for keeping me sane throughout this coding journey.
- My wife, Fiona, for putting up with long days and late nights locked in the back garden Tea Room/Shed (man-cave).
- The Code Institute for giving me this opportunity to gain new knowledge and applicable job skills.