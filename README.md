![GaffCo Consulting Logo](https://github.com/NaoiseGaffney/CI-PTD-II/blob/development/Documentation/Gaffco_Logo.png)

# GaffCo Consulting Professional Training and Development: Professional Communication and Presentation Skills E-Commerce Website

Professional Communication and Presentation Skills - 4th Milestone Project for the Code Institute's Diploma in Full Stack Development. Project requirements: HTML 5, CSS 3, JavaScript, Python 3, Django, PostgreSQL, and API's. This project website is an e-commerce site for a Professional Communications and Presentation Skills Company (Sole Trader) called GaffCo Consulting.
 
Model-View-Template: Model -> View -> URL -> Template or Form -> View -> URL -> Template
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

### User Stories, Use Cases, and Tasks Mapped to Information Architecture and Navigation

The User Experience links the Business goals of the external user and site owner to a number of user stories. A user story captures a description of a software feature from an end-user perspective. A user story describes the type of user, what they want and why. A use case is a list of actions or event steps describing the interactions between a role and a system to achieve a goal.

A user story has one or more use cases with one or more tasks with steps associated with it, describing how the user story, and subsequent fulfilment of the external user's and site owner's business goals are realised: Business Goals -> User Story -> Use Case(s) -> Task(s).

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



Business Driven Development aims to overcome the common mismatch between the Business and IT. BDD consists of a continuous cycle of Modelling -> Building -> Deploying -> Managing. Testing is a part of Building, through unit, integration, and regression testing. These tests won't validate the user experience in the form of user stories and use cases. Behaviour Driven Development (BDD) is a branch of Test Driven Development (TDD). BDD uses human-readable descriptions of software user requirements as the basis for software tests.

BDD Testing is performed manually, and automated using Selenium IDE.

### Validation of HTML, CSS, JS, and Python Code
### Manual Testing

### Automated Behaviour Driven Development Testing using Selenium IDE and PyTest
Selenium IDE runs automated, and scripted tests when configured. In this case the Selenium IDE recording function is used to create the scripts, the scripts are exported to PyTest code, and then run to validate the test cases.

To prepare for the tests:
* Install pytest, selenium and the correct webdriver (ChromeDriver)
* * pip3 install pytest
* * pip3 install selenium
* * http://chromedriver.chromium.org/downloads
* * * Unzip and copy 'chromedriver 2' to the virtual Python/bin directory. Rename it to 'chromedriver'.
* * * Execute chromedriver in the terminal to ensure the correct version is running; it has to match the version in "About Google Chrome". If using other browsers, other webdrivers must be installed. Don't do "pip3 install ChromeDriver" as it's likely to install an older version which means that the tests won't run as Chrome can't be controlled.
* Create a new '.env' file at the Project Root. Add the following variables, with values:

```
USER_TEST_NAME=<name>
USER_TEST_PASSWORD=<your password>
NEW_USER_TEST_NAME=<test_user_name>
NEW_USER_FIRST_NAME=<new_name>
NEW_USER_EMAIL=<your email>
NEW_USER_TEST_PASSWORD=<secret password>
PROFILE_FIRST_NAME=<profile_name>
PROFILE_LAST_NAME=<profile_surname>
PROFILE_EMAIL=<profile_email>
PROFILE_ADDRESS=<profile_address>
PROFILE_POST_CODE=<profile_post_code>
PROFILE_CITY=<profile_city>
PASSWORD_CHANGE_PASSWORD=<change_to_this_password>
```

* Execute the test: `pytest`. Runs `test_trainingBDDSuite.py`.

```
# Generated by Selenium IDE and refined by Gaff
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Read '.env' file created for Testing Parameters stored in Project Root
import environ
import os
root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
environ.Env.read_env()  # reading .env file

class TestTrainingBDDSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_useCase001ViewHomePageandLinkedIn(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.vars["window_handles"] = self.driver.window_handles
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Connect: LinkedInlink").click()
    self.vars["win7260"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win7260"])
  
  def test_useCase002RegisterLoginLogout(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, "#nav-mobile > li:nth-child(2) > .black-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#nav-mobile > li:nth-child(2) > .black-text").click()
    self.driver.find_element(By.LINK_TEXT, "register here").click()
    self.driver.find_element(By.ID, "id_username").send_keys("Naoise")
    self.driver.find_element(By.ID, "id_first_name").send_keys("Naoise")
    self.driver.find_element(By.ID, "id_email").send_keys("naoise.gaff.gaffney@gmail.com")
    self.driver.find_element(By.ID, "id_password").send_keys("Jam3s0n8@")
    self.driver.find_element(By.ID, "id_password2").send_keys("Jam3s0n8@")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "log in").click()
    self.driver.find_element(By.ID, "id_username").send_keys("Naoise")
    self.driver.find_element(By.ID, "id_password").send_keys("Jam3s0n8@")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
  def test_useCase003ViewandPurchaseCourseandCoachinganonymoususer(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".dropdown-trigger > .material-icons").click()
    # self.driver.find_element(By.CSS_SELECTOR, "#dropdown_test > li:nth-child(1) > .black-text").click()
    self.driver.get("http://127.0.0.1:8000/shop/")
    self.driver.find_element(By.CSS_SELECTOR, ".active").click()
    self.driver.find_element(By.CSS_SELECTOR, ".select-dropdown:nth-child(1)").send_keys(Keys.UP)
    self.driver.find_element(By.CSS_SELECTOR, ".select-dropdown:nth-child(1)").send_keys(Keys.ENTER)
    # dropdown = self.driver.find_element(By.ID, "id_quantity")
    # dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.get("http://127.0.0.1:8000/shop/courses/")
    self.driver.find_element(By.CSS_SELECTOR, ".active").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".select-dropdown:nth-child(1)").send_keys(Keys.DOWN)
    # dropdown = self.driver.find_element(By.ID, "id_quantity")
    # dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".select-dropdown:nth-child(1)").send_keys(Keys.TAB)
    self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(2) input:nth-child(3)").click()
    self.driver.get("http://127.0.0.1:8000/shop/coaching/")
    self.driver.find_element(By.CSS_SELECTOR, ".active").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(5)").click()
    self.driver.get("http://127.0.0.1:8000/shop/")
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-item:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2) .waves-button-input").click()
    self.driver.get("http://127.0.0.1:8000/orders/create/")
    self.driver.find_element(By.ID, "id_first_name").send_keys("Naoise")
    self.driver.find_element(By.ID, "id_last_name").send_keys("Gaffney")
    self.driver.find_element(By.ID, "id_email").send_keys("naoise.gaff.gaffney@gmail.com")
    self.driver.find_element(By.ID, "id_address").send_keys("6 Oldcourt Close, Ballycullen")
    self.driver.find_element(By.ID, "id_postal_code").send_keys("D24 RHY2")
    self.driver.find_element(By.ID, "id_city").send_keys("Dublin")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    time.sleep(6)
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.ID, "credit-card-number").send_keys("4242 4242 4242 4242")
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.ID, "cvv").send_keys("123")
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.ID, "expiration").send_keys("12 / 28")
    self.driver.switch_to.default_content()
    time.sleep(6)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(9)").click()
  
  def test_useCase004EditProfileLoginEditProfileLogout(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#nav-mobile > li:nth-child(2) > .black-text").click()
    self.driver.find_element(By.ID, "id_username").send_keys("Naoise")
    self.driver.find_element(By.ID, "id_password").send_keys("Jam3s0n8@")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "edit your profile").click()
    self.driver.find_element(By.ID, "id_last_name").send_keys("Gaffney")
    self.driver.find_element(By.ID, "id_address").send_keys("6 Oldcourt Close, Ballycullen")
    self.driver.find_element(By.ID, "id_post_code").send_keys("D24 RHY2")
    self.driver.find_element(By.ID, "id_city").send_keys("Dublin")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Character Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
  def test_useCase005ChangePassword(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#nav-mobile > li:nth-child(2) > .black-text").click()
    self.driver.find_element(By.ID, "id_username").send_keys("Naoise")
    self.driver.find_element(By.ID, "id_password").send_keys("Jam3s0n8@")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "change your password").click()
    self.driver.find_element(By.ID, "id_old_password").send_keys("Jam3s0n8@")
    self.driver.find_element(By.ID, "id_new_password1").send_keys("VoiceOver123")
    self.driver.find_element(By.ID, "id_new_password2").send_keys("VoiceOver123")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "Character Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "change your password").click()
    self.driver.find_element(By.ID, "id_old_password").send_keys("VoiceOver123")
    self.driver.find_element(By.ID, "id_new_password1").send_keys("Jam3s0n8@")
    self.driver.find_element(By.ID, "id_new_password2").send_keys("Jam3s0n8@")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "Character Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
  def test_useCase006PasswordReset(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#nav-mobile > li:nth-child(2) > .black-text").click()
    self.driver.find_element(By.LINK_TEXT, "Forgotten your password?").click()
    self.driver.find_element(By.ID, "id_email").send_keys("naoise.gaff.gaffney@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
```


```
(.venv) gaff@Naoises-MacBook-Pro Training % pytest
===================================================================== test session starts ======================================================================
platform darwin -- Python 3.8.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/gaff/Dropbox/GaffCo/Repository/Training
collected 6 items                                                                                                                                              

test_trainingBDDSuite.py ......                                                                                                                          [100%]

================================================================= 6 passed in 78.88s (0:01:18) =================================================================
(.venv) gaff@Naoises-MacBook-Pro Training % 
```

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
Updated the (Shopping) Cart to use cards instead of a table as the table doesn't work well on mobiles. Added styling to the cards in `base.css`.
Added a dynamic `<h3>` header to the Shop for All Training, Courses, and Coaching checking request.path for the relevant link contents. This shows the user/buyer what products s/he is looking at.
Spacing for paragraphs (empty space = cleaner look and easier to read), except for paragraph buttons, nor for the carousel. Used CSS selectors for Django forms to style the p elements:

```
/* Create breathing space between paragraph elements */
p.padding, div > form + p, div > form + p + p {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}
```

Your order summary space between product and price:

```
li > span {
    padding-left: 0.5rem;
}
```

Course and Coaching Detail Form Block to allow for a better display on desktop screens. Media query providing a better view on desktop screens (relies upon the 'display: inline-block' to contain the form label):

```
.inline_form_block {
    display: inline-block;
}

@media only screen and (min-width: 800px) {
    .product-detail img {
        width: 50%;
        float: left;
        padding: 0 20px 20px 0;
    }
}
```

Added navigation links to account, cart and payment templates to improve user navigation and experience. Removed the Checkout button on the Total Price = 0 (empty cart) so no empty orders are ordered, nor paid for.

Created Favicon: https://www.favicon-generator.org/. Added Favicon, updated `templates/base.html` header with Favicon links, and placed the icons in `static/img/`.

#### AWS S3 Bucket Configuration

#### PostgreSQL Configuration

#### Issues

Heroku and AWS S3 Bucket (static and media folders and files): Bad Request (400).

```
Dear Coders,
I have resolved an issue with Heroku, AWS S3, hard-coded URL’s, and static plus media files that occurred after configuring AWS S3 and deploying (successful build) to Heroku. Accessing the Heroku URL I received a “Bad Request (400)“. I had the same issue locally after configuring to use AWS S3 locally too. I didn’t have this issue with Boutique_Ado, nor with a test project I did before my MS4 to get my head around it all.
Running locally in Debug mode I received an error message stating “Suspicious activity… /static/base.css…AWS S3”.
Turns out I had two issues:
Using leading slashes  in my / URL’s, for example <link rel="stylesheet" href="{% static '/styles/base.css' %}">  and removing the leading slash to this <link rel="stylesheet" href="{% static 'styles/base.css' %}"> worked.
Hard-coded URL’s for images and links. I’ve changed all my links to:
{% static 'img/Gaffco_Logo.png' %} and uploading my images to AWS S3 manually to correspond to the links in my templates.
{% url 'shop:product_list' %}  = https://trainingdjango.s3.amazonaws.com/static/img/Gaffco_Logo.png
 or {% url 'shop:product_list' %}coaching/  = <a href="/shop/coaching/"
… or {% url 'shop:product_detail' 3 'communication-skills' %} = <a href="/shop/3/communication-skills/">
Some of you may already know this, I didn’t. It’s a learning experience, especially at half-past-four in the morning. :slightly_smiling_face:
Sláinte!
Gaff
```






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