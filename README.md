![GaffCo Consulting Logo](documentation/PCC_Logo.png)

# Professional Communication and Presentation Skills E-Commerce Website

"Organisations Achieve Greater Value through Professionally Coached Employees." - Gaff

Professional Communication and Presentation Skills - 4th Milestone Project for the Code Institute's Diploma in Full Stack Development. Project requirements: HTML 5, CSS 3, JavaScript, Python 3, Django, PostgreSQL, Payment System, and API's. This project website is an e-commerce site for a Professional Communications and Presentation Skills Company (Sole Trader) called GaffCo Consulting.

![Section Divider: Title and Business](documentation/section%20divider.png)

PLACEHOLDER FOR THE TABLE-OF-CONTENTS

![Section Divider: Title and Business](documentation/section%20divider.png)

## Business
The Business goals describe the expected consumer and site owner goals, and drive the design, development, and deployment of the application which in this case is the Professional Training and Development E-commerce site. The fulfilment of these goals determine the success of the application.

### External User's (Consumer) Goals
Find suitable courses and coaching sessions to improve presentation and communication skills to get their audience to feel, think, and ideally do something as a result of a presentation.

### Site Owner's Goals
Motivate and inspire learners (consumers) to achieve excellent results through presentation and communication skills by attending the courses and coaching sessions provided on this site.

![Section Divider: Title and Business](documentation/section%20divider.png)

## User Experience
User experience (UX) design is the design process used to create applications and websites that provide meaningful and relevant experiences to users.

### Persona Summary of the Consumer
![Persona Summary](documentation/persona_summary.png)
This site is aimed at individuals at age 18 and above, and businessess seeking professional courses and coaching on presentation and communication skills. Consumers can view the courses and coaching sessions on offer to select the ones most suitable to their requirements to increase their knowledge, improve their skills and give them the confidence to put the new knowledge and skills to good use.

### Strategy Trade-Off
UX Design is driven by business goals and user needs, and features developed are aligned to these. However, each feature requires time and effort, and often time is constrained as is effort as the greater the effort the higher the cost. Therefore some features are prioritised or mandatory, while others are optional and developed pending time and ultimately cost.

The selected features are driven by the opportunity matrix, which helps us understand what is both more important and viable to create. In this case all features mentioned below are implemented as the features made sense to provide in this initial release. Additional and future features are documented under the Features section, and not documented here.

#### Opportunity Matrices for Training and Development
![Opportunty Matrix - Account Management](documentation/OppMatrix_Account.png)

![Opportunty Matrix - Shop to Pay](documentation/OppMatrix_ShopToPay.png)

[Initial Plans for MS4](documentation/MS4.pdf) scribbled on a several A4 pages (PDF). This gave me purpose and direction for the project. However, time contraints and continuous assessments changed the initial plan.

### User Stories, Use Cases, and Tasks Mapped to Information Architecture and Navigation

The User Experience links the Business goals of the external user and site owner to a number of user stories. A user story captures a description of a software feature from an end-user perspective. A user story describes the type of user, what they want and why. A use case is a list of actions or event steps describing the interactions between a role and a system to achieve a goal.

A user story has one or more use cases with one or more tasks with steps associated with it, describing how the user story, and subsequent fulfilment of the external user's and site owner's business goals are realised: Business Goals -> User Story -> Use Case(s) -> Task(s).

---

![Information Architecture and Navigation](documentation/InformationArchitectureNavigation.png)

The User Experience links the Business goals of the external user (consumer) and site owner to a number of user stories. A user story captures a description of a software feature from an end-user perspective. A user story describes the type of user, what they want and why. A use case is a list of actions or event steps describing the interactions between a role and a system to achieve a goal.

A user story has one or more use cases with one or more tasks with steps associated with it, describing how the user story, and subsequent fulfilment of the external user's and site owner's business goals are realised: Business Goals -> User Story -> Use Case(s) -> Task(s).

Information Architecture is hierarchical (home -> shop, home -> character, home -> cart) and sequential (shop -> cart -> orders -> payment). The navigation bar provides the same options for anymous and logged in consumers.

---

* **User Story 001 (Consumer):** As a consumer I want to view and purchase the courses and coaching sessions on offer so that I can attend them to imorove my professional presentation and communication skills.
	* **Use Case 001-001 - View Home / Index Page and LinkedIn Profile:** As a consumer I want to view what GaffCo Consulting is all about, and what is on offer.
		* **Task 1:** Access the home / index page [Training and Development](https://training-and-development.herokuapp.com/). Scroll through the content on the page.
		* **Task 2:** Click on the LinkedIn Profile link to access further details about the owner of GaffCo Consulting.
	* **Use Case 001-002 - Register, Login, Logout:** As a consumer I want to register, login, and logout to access further future content and details.
		* **Task 1:** Access the character dashboard via the naviagation bar menu [Character Dashboard](https://training-and-development.herokuapp.com/account/dashboard/).
		* **Task 2:** Click on [Register Here](https://training-and-development.herokuapp.com/account/register/) to create an account. Fill in the details in the form and click on "Create my account" button.
		* **Task 3:** Click on [Log-in](http://127.0.0.1:8000/account/login/), enter your username and password, and click on the "Log-in" button.
		* **Task 4:** Perform the relevant actions on the website.
		* **Task 5:** Click on [Logout](http://127.0.0.1:8000/account/logout/) when done.
	* **Use Case 001-003 - View and Purchase Courses and Coaching Sessions:** As a consumer I want to view and purchase courses and coaching sessions to increase my knowledge and improve my skills.
		* **Task 1:** Access the home / index page [Training and Development](https://training-and-development.herokuapp.com/).
		* **Task 2:** Click on "Courses & Coaching" in the naviagation bar and select either "All Training" or "Courses" or "Coaching".
		* **Task 3:** Use the carousel to find a course or coaching session you want to view the details of, and potentially purchase.
		* **Task 4:** Select (click on) on the course or coaching session you want further details on, and potentially want to purchase.
		* **Task 5:** Review the details of the course or coaching session. If required, updated the number of course seats or coaching sessions, and click on "Add to cart".
		* **Task 6:** Review your choice, update the number of course or coaching sessions, or remove if you change your mind. Review the price, item price, total item price, and the total price. If you want to add further courses or coaching sessions, click on "Continue shopping". If happy with your choice click on the "Checkout" button.
		* **Task 7:** Review your order before filling in the Checkout Form. If happy click on the "Place order" button.
		* **Task 8:** Fill in the credit-card payment form and click on the "Pay" button.
		* **Task 9:** Continue shopping, or click on [Home](http://127.0.0.1:8000/), or close the browser.
	* **Use Case 001-004 - Edit / Update the Character (Consumer) Profile:** As a consumer I want to edit / update my Character (Consumer) Profile for future features and content.
		* **Task 1:** Access the character dashboard via the naviagation bar menu [Character Dashboard](https://training-and-development.herokuapp.com/account/dashboard/).
		* **Task 2:** Click on [Log-in](http://127.0.0.1:8000/account/login/), enter your username and password, and click on the "Log-in" button.
		* **Task 3:** Click on [edit your profile](http://127.0.0.1:8000/account/edit/).
		* **Task 4:** Update the Character Profile form and click on "Save changes" when done. A Django message pop-up provides feedback on whether the update is successful or not. Click on [Character Dashboard](http://127.0.0.1:8000/account/dashboard/).
	* **Use Case 001-005 - Change Password:** As a consumer I want to change my password.
		* **Task 1:** Access the character dashboard via the naviagation bar menu [Character Dashboard](https://training-and-development.herokuapp.com/account/dashboard/).
		* **Task 2:** Click on [Log-in](http://127.0.0.1:8000/account/login/), enter your username and password, and click on the "Log-in" button.
		* **Task 3:** Click on [change your password](http://127.0.0.1:8000/account/password_change/), enter your current password, your new password, your new password a second time, and click on the "Change" button.
		* **Task 4:** Click on the [Character Dashboard](http://127.0.0.1:8000/account/dashboard/) and [Logout](http://127.0.0.1:8000/account/logout/).
	* **Use Case 001-006 - Password Reset:** As a consumer I want to reset my password as I have forgotten my current password and want to gain access to my account.
		* **Task 1:** Access the character dashboard via the naviagation bar menu [Character Dashboard](https://training-and-development.herokuapp.com/account/dashboard/).
		* **Task 2:** Click on [Forgotten your password?](http://127.0.0.1:8000/account/password_reset/).
		* **Task 3:** Enter your e-mail address (same one used to register) and click on the "Send e-mail" button.
		* **Task 4:** Once you receive your password reset e-mail, click on the link to reset your password.
		* **Task 5:** Enter your new password, confirm your new password and click on the "Change my password" button.

---

* **User Story 002 (Admin):** As an administrator I want to create, read, update and delete database items from the admin view to maintain the site.
	* **Use Case 002-001 - Authentication and Authorization:** As an admin I want to manage users and groups on the site. - [Authentication and Authorization](http://127.0.0.1:8000/admin/auth/) CRUD functions for Groups (not currently ised) and Users. Using Django authorization. 
	* **Use Case 002-002 - Account:** As an admin I want to manage Character Profiles. - [Account](http://127.0.0.1:8000/admin/account/). Consumer updates to their Character Profile is managed here.
	* **Use Case 002-003 - Shop:** As an admin I want to manage the product categories and prodcuts provided to the Consumers. - [Shop](http://127.0.0.1:8000/admin/shop/).
	* **Use Case 002-002 - Orders:** As an admin I want to manage the orders placed by Consumers. - [Orders](http://127.0.0.1:8000/admin/orders/)

---

### Wireframes

[Wireframes for Desktops (Large) and Tablets (Medium), and Mobile (Small) - PDF](documentation/MS4%20Wireframes.pdf)

The wireframes cover Desktop and Tablet sized devices as one, as the design and look is the same for both. Mobile devices are similar, with the main difference being the hamburger-nav-bar instead of a full navigation bar, and the fact that most text and images flows to one column. I did this on purpose, to keep the style and layout both functional and simple, requiring less CSS "shenanigans".

Strategy Plane: User Needs & Site Objectives
Scope Plane: Specifications & Content Requirements
Structure Plane: Interaction Design & Information Architecture
Skeleton Plane: Information Design, Interface Design & Navigation Design
Surface Plane: Visual Design

![Section Divider: Title and Business](documentation/section%20divider.png)

## Features

A feature is some action that can be performed by a user of an application, or is some internal function of an application. The features support the User Experience mentioned above and are implemented based on the business goals, user stories and use cases.
 
### Existing Features
* **Django App - Home:** Home / Index Page provides an introduction to GaffCo Consulting, and overview of the courses and coaching sessions that are provided.
	* Navigation Bar / Hamburger-Nav-Bar (Materialize CSS 1.0.0)
		* Logo Link to Home / Index Page (Logo is my own)
		* Courses & Coaching Drop-Dowm (Materialize CSS 1.0.0) -> *Django App - Shop*
			* All Training (all categories) -> Carousel
			* Courses (category) -> Courses Carousel
			* Coaching (category) -> Coaching Carousel
	* Parallax - Mountain Success x 3 (Materialize CSS 1.0.0)
	* Banner / Tagline for Professional Training and Development
	* GaffCo Consulting description, course and coaching tabs with links and descriptions to courses and coaching sessions.
	* Fixed Footer
		* LinkedIn Profile Link
		* Copyright Notice
* **Django App - Shop:** All Training / Courses / Coaching Carousel.
	* Views of available courses and coaching sessions in a carouesel.
	* Carousel courses and coaching sessions are selectable to view in greater detail and are available to purchase.
	* Detailed view of course or coaching session.
	* Ability to select number of courses and coaching sessions and add to cart.
	* Submit cart -> *Django App - Cart*
* **Django App - Cart:** View and checkout course and coaching items in cart.
	* View cart contents, with image, title, number of the item, item price, total item price, and total price of all products.
	* Add additional number of items and update cart contents, updating item price and total item price, as well as the total price of all products.
	* Products can be removed with the remove button.
	* Consumer can continue shopping, add further products/items.
	* Consumer can checkout -> *Django App - Checkout*
* **Django App - Checkout:** Fill in the checkout form to place the order.
	* Checkout form to place the order and receive an e-mail confirmation -> *Django App - Payment*
* **Django App - Payment:** Fill in the credit-card details and click Pay to purchase the items.
	* Consumer can fill in the credit-card details to purchase the items ordered.
	* Consumer gets a payment done (success or failure) wiht a link to home -> *Django App - Home*
* **Django App - Account:** Consumer Authentication and Authorisation.
	* Consumer can register, login, edit character profile, change password, reset password (e-mail notification), and logout.
	* Consumer Dashboard access.

### Features Left to Implement
* **NEW - Django App - Order Rating and Comments:**
* **NEW - Django App - Courses:** Add online course content for some courses linked to YouTube videos.
* **NEW - Django App - Accreditation:** Create accrediation views, course diplomas, and success trees for consumers.
* **Existing - Django App - Account:** Add additional e-mail notifications.
* **Existing - Django App - Dashboard:** Improve Character Profile with additional details like a photo and courses purchased, and courses taken.
* **Existing - Django App - Payment:** Fill in payment details if consumer is authenticated and a character profile exists.

![Section Divider: Title and Business](documentation/section%20divider.png)

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

![Section Divider: Title and Business](documentation/section%20divider.png)

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
    self.driver.find_element(By.ID, "id_username").send_keys(os.environ.get("NEW_USER_USERNAME"))
    self.driver.find_element(By.ID, "id_first_name").send_keys(os.environ.get("NEW_USER_FIRST_NAME"))
    self.driver.find_element(By.ID, "id_email").send_keys(os.environ.get("NEW_USER_EMAIL"))
    self.driver.find_element(By.ID, "id_password").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.ID, "id_password2").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "log in").click()
    self.driver.find_element(By.ID, "id_username").send_keys(os.environ.get("NEW_USER_USERNAME"))
    self.driver.find_element(By.ID, "id_password").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
  def test_useCase003ViewandPurchaseCourseandCoachinganonymoususer(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.get("http://127.0.0.1:8000/shop/")
    self.driver.find_element(By.CSS_SELECTOR, ".active").click()
    self.driver.find_element(By.CSS_SELECTOR, ".select-dropdown:nth-child(1)").send_keys(Keys.UP)
    self.driver.find_element(By.CSS_SELECTOR, ".select-dropdown:nth-child(1)").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.get("http://127.0.0.1:8000/shop/courses/")
    self.driver.find_element(By.CSS_SELECTOR, ".active").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".select-dropdown:nth-child(1)").send_keys(Keys.DOWN)
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
    self.driver.find_element(By.ID, "id_first_name").send_keys(os.environ.get("PROFILE_FIRST_NAME"))
    self.driver.find_element(By.ID, "id_last_name").send_keys(os.environ.get("PROFILE_LAST_NAME"))
    self.driver.find_element(By.ID, "id_email").send_keys(os.environ.get("PROFILE_EMAIL"))
    self.driver.find_element(By.ID, "id_address").send_keys(os.environ.get("PROFILE_ADDRESS"))
    self.driver.find_element(By.ID, "id_postal_code").send_keys(os.environ.get("PROFILE_POST_CODE"))
    self.driver.find_element(By.ID, "id_city").send_keys(os.environ.get("PROFILE_CITY"))
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
    self.driver.find_element(By.ID, "id_username").send_keys(os.environ.get("NEW_USER_USERNAME"))
    self.driver.find_element(By.ID, "id_password").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "edit your profile").click()
    self.driver.find_element(By.ID, "id_last_name").send_keys(os.environ.get("PROFILE_LAST_NAME"))
    self.driver.find_element(By.ID, "id_address").send_keys(os.environ.get("PROFILE_ADDRESS"))
    self.driver.find_element(By.ID, "id_post_code").send_keys(os.environ.get("PROFILE_POST_CODE"))
    self.driver.find_element(By.ID, "id_city").send_keys(os.environ.get("PROFILE_CITY"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Character Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
  def test_useCase005ChangePassword(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#nav-mobile > li:nth-child(2) > .black-text").click()
    self.driver.find_element(By.ID, "id_username").send_keys(os.environ.get("NEW_USER_USERNAME"))
    self.driver.find_element(By.ID, "id_password").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "change your password").click()
    self.driver.find_element(By.ID, "id_old_password").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.ID, "id_new_password1").send_keys(os.environ.get("PASSWORD_CHANGE_PASSWORD"))
    self.driver.find_element(By.ID, "id_new_password2").send_keys(os.environ.get("PASSWORD_CHANGE_PASSWORD"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "Character Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "change your password").click()
    self.driver.find_element(By.ID, "id_old_password").send_keys(os.environ.get("PASSWORD_CHANGE_PASSWORD"))
    self.driver.find_element(By.ID, "id_new_password1").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.ID, "id_new_password2").send_keys(os.environ.get("NEW_USER_PASSWORD"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "Character Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
  def test_useCase006PasswordReset(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1680, 975)
    self.driver.find_element(By.CSS_SELECTOR, ".container > a:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#nav-mobile > li:nth-child(2) > .black-text").click()
    self.driver.find_element(By.LINK_TEXT, "Forgotten your password?").click()
    self.driver.find_element(By.ID, "id_email").send_keys(os.environ.get("NEW_USER_EMAIL"))
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
```


```
(.venv) gaff@Naoises-MacBook-Pro Training % pytest
======================================================================================================= test session starts =======================================================================================================
platform darwin -- Python 3.8.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/gaff/Dropbox/GaffCo/Repository/Training
collected 6 items                                                                                                                                                                                                                 

test_trainingBDDSuite.py ......                                                                                                                                                                                             [100%]

================================================================================================== 6 passed in 80.03s (0:01:20) ===================================================================================================
(.venv) gaff@Naoises-MacBook-Pro Training % 
```

![Section Divider: Title and Business](documentation/section%20divider.png)

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

![Section Divider: Title and Business](documentation/section%20divider.png)

## Credits

### Content
* Code Institute Boutique-Ado Walkthrough
* Code Institute June 2020 Hackathon - ElderCareSupreme
	* Code on GitHub: [Elder Care Supreme - master](https://github.com/NaoiseGaffney/ElderCareSupreme)
	* Website on Heroku: [Elder Care Supreme](https://elder-care-supreme.herokuapp.com/)
* YouTube Django Course: [Django E-Commerce Website by Dennis Ivy (Ivanov)](https://www.youtube.com/watch?v=_ELCMngbM0E&ab_channel=DennisIvy)
* Udemy Course: [Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/)
* [Materialize CSS 1.0.0](https://materializecss.com/)
* Django 3 Web Development Cookbook.
* First Milestone Project - Professional Training and Development
	* [Code on GitHub](https://github.com/NaoiseGaffney/Professional-Training-Development)
	* [Website on GitHub Pages](https://naoisegaffney.github.io/Professional-Training-Development/index.html)

### Media
* Google Font - [Raleway](https://fonts.googleapis.com/css?family=Raleway|&display=swap).
* Background Image on the Home / Index Page is: [Pixabay Free Images](https://cdn.pixabay.com/photo/2019/01/27/22/32/mountains-3959204_1280.jpg)
* All icons: [Material Design Icons](https://material.io/resources/icons/)
* All other logos and images are my own.

### Acknowledgements

* I received inspiration for this project from my first Code Institute Milestone Project, a Training and Development website. I have turned it into an e-commerce site, and will fork this to expand upon it further to turn it into a professional Training and Development Learning website.
* I clearly relied heavily upon the Boutique_Ado walkthrough, NetNinja, Udemy Courses, YouTube videos and several books to understand and apply the concepts for this project.
* My Code Institute mentor Spencer Barriball for keeping me sane throughout this coding journey.
* My wife, Fiona, for putting up with long days and late nights locked in the back garden Tea Room/Shed (man-cave).
* The Code Institute for giving me this opportunity to gain new knowledge and applicable job skills.