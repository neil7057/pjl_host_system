# leos_oreos_shop
![Mockup]()

**Author Neil Allen**

## Leo's Oreo Emporium

An E-commerce website to pay homage to my son's love of the biscuits themselves and everything Oreo. Built using a django framework; data structures follow those employed in similar applications with additions for enhanced functionality/complexity. 

[View the live project here.]()

# Table of Contents

1. [Project Inception and Planning](#project-inception-and-planning)
2. [Overview](#overview)
3. [User Experience (UX)](#user-experience-ux)
    *   [User stories](#user-stories)
        *   [First Time Visitor Goals](#first-time-visitor-goals)
        *   [Returning Visitor Goals](#returning-visitor-goals)
        *   [Frequent User Goals](#frequent-user-goals)
    *   [Design](#design)
        *   [Colour Scheme](#colour-scheme)
        *   [Typography](#typography)
        *   [Imagery](#imagery)
        *  [Design Considerations](#design-considerations)
    *   [Database Design](#database-design)
        *   [Table Struture](#table-structure)
        *   [Diagram](#diagram)
    *   [Wireframes](#wireframes)
        *   [Base Template](#base)
        *   [Home](#home)
            

    *   [Structure](#structure)
4. [Features](#features)
5. [Pages](#pages)
    *   
    *   [Site Features](#site-features)
6. [Technologies Used](#technologies-used)
    *   [Development Environment](#development-environment)
    *   [Languages Used](#languages-used)
    *   [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
7. [Testing](#testing)
    *   [HTML](#html)
    *   [CSS](#css)
    *   [JavaScript](#javascript)
    *   [pep8](#pep8)
    *   [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
        *   [First Time Visitor Goals](#first-time-visitor-goals-1)
        *   [Returning Visitor Goals](#returning-visitor-goals-1)
        *   [Frequent User Goals](#frequent-user-goals-1)
    *   [Responsiveness](#responsiveness)
    *   [Accessibility](#accessibility)
    *   [Screen Reader](#screen-reader)
    *   [Lighthouse Testing](#lighthouse-testing)
    *   [Functional Testing](#functional-testing)
        *   [Navigation Links](#navigation-links)
        *   [Testing Approach](#testing-approach)
        *   [Test Accounts](#test-accounts)
        *  
        *   [Footer Contact Information](#footer-contact-information)
    *   [Further Testing](#further-testing)
    *   [Bugs and Fixes](#bugs-and-fixes)
    *   [Known Bugs](#known-bugs)
    *   [Future Releases](#future-releases)
8. [Deployment](#deployment)
    *   [Version control](#version-control)
    *   [Github Pages](#github-pages)
    *   [Deployments to Github Pages](#deployment-to-github-pages)
    *   [Clone the repository locally](#clone-the-repository-code-locally)
    *   [Heroku](#heroku)
    *   [App Deployment](#app-deployment-to-heroku)
9. [Credits](#credits)
    *   [Code](#code)
    *   [Content](#content)
    *   [Media](#media)
    *   [Acknowledgements](#acknowledgements)

## Project Inception and Planning

## Overview

The website is a 

visitors/shoppers

Logged in users can l.

Administrators can 

Administrators can 

## User Experience (UX)

-   ### User stories

- #### As a first time user I want to:
    -    Immediately understand the main purpose and use of the site
    -    Be able easily navigate through the page
    -    Be able search for the products on the page
    -    Contact the company with any queries
    -    Buy products without registration
    -    See the reviews left by other users
    -    Be able use the page on any devices and screen sizes
    -    Login/create an user account

- #### As a registered user I want to:
    -   Have access to my profile page
    -   Be able to leave the reviews for purchased products
    -   See my order history
    -   Be able to update and save my personal info
    -   Be able to change my password
    -   Make purchase with my delivery info always filled

- #### As an admin I want to:
    -   Be able to add, edit and delete products
    -   View and manage customer reviews
    -   Delete customer review if not appropriate
    -   Have easy access to admin controls

-   ### Design
    -   #### Colour Scheme
        -   I've used 
        
    -   #### Typography
        -   The fonts chosen are 
 
    -   #### Imagery
        -   There is a 

    -   #### Design Considerations
        -   The site is built with
     
        -   Colours are 

        -   The heads

        -   The site is responsive with menus and text resized for smaller screens. 

        -   Menu navigation is consistent across all pages and screen sizes and is central to each page. Menus change according to login and admin status.

        -   Menu button 

        -   Administrators

        -   Error and confirmation 

        -   Logged in users get to see 

-   ### Database Design
-   #### Table Structure
    *   A 
    *   A 
    *   A 
    *   A 
    *   A 
    *   A .

-   #### Diagram
    <details><summary>Data Structure</summary>
    <img src="">

-   ### Wireframes   
    
-   #### Base
    <details><summary>Index - Home</summary>
    <img src="leos_oreos\docs\images\wireframes\index.html.png">
    </details>

-   #### Products
    <details><summary>All products</summary>
    <img src="leos_oreos\docs\images\wireframes\all-products.png">
    </details>

-   #### Details
    <details><summary>Product Detail</summary>
    <img src="leos_oreos\docs\images\wireframes\product-detail.png">
    </details>

-   #### Category
    <details><summary>Products - Selected by Category</summary>
    <img src="leos_oreos\docs\images\wireframes\products-selectedby-category.png">
    </details>

-   #### Shopping Cart
    <details><summary>Shopping Cart</summary>
    <img src="leos_oreos\docs\images\wireframes\shopping-cart.png">
    </details>

-   #### Checkout
    <details><summary>Checkout</summary>
    <img src="leos_oreos\docs\images\wireframes\checkout.png">
    </details>

-   #### Checkout Success
    <details><summary>Checkout Success</summary>
    <img src="leos_oreos\docs\images\wireframes\checkout-success.png">
    </details>

-   
 
-   ### **Structure**

    The structure of the site 

    Visitors can view 

    Functions serve:
    -   Sign Up
    -   Login and out
    -   
    -   Search facility

    The site is templated a

    Social media links 
    
## Features

-   Responsive on all device sizes down to 280px - the industry standard minimum screen width.

## Pages
### Landing Page
-   Landing page image   
    *   The first page is the index or home page.
    *   For visitors, 
    *   For users, 
    *   This will help to immediately show the visitor/user what the website is about. 

    <details><summary>Landing Page - Visitor</summary>
    <img src="beachhuts/static/docs/readme_images/screens/home-logged-out.png">
    </details>
    <br>
    
### Search Results Page

-   <details><summary>Search Page</summary>
    <img src=".png">
    </details>


### Site Features

* Responsive design - content scales from 280px to Large Desktop. Some content is hidden at smaller resolutions to maintain user experience.
* Top Menu navbar remains consistent with a secondary Menu bar that responds to user status.
* There is a Top of the Page scrolling button on each page. 
* The main landing 

## Technologies Used

### Development Environment
-   The site was developed in a virtual VSC desktop environment.

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://docs.python.org/3/)


### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.2.1:](https://getbootstrap.com/docs/4.6.2/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Menu items in the navbar as well as the Social Media icons in the footer to add the 'grow' transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Baskerville Libre' and 'Open Sans' fonts into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Used for icons on social links and drop down menus.
1. [jQuery:](https://jquery.com/)
    - jQuery is used to make the navbar responsive and provide additional coding flexibility. specifically used with the emailJS service, modal and other processing.
1. [Select2:](https://select2.org/)
   - Select2 was used for styling the dropdown to allow multiple selections without CMD/CTRL or Shift.
1. [GitHub:](https://github.com/)
   - GitHub is used to store the project's code after being pushed from the development environment.
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](#wireframes) during the design process.
1. [Jest:](https://jestjs.io/)
   - Jest was used to test the Javascript used.
1. [SQLAlchemy:](https://docs.sqlalchemy.org/en/20/)
   - SQLAlchemy was used to communicate between the database and the frontend
1. [DBDiagram:](https://dbdiagram.io/home)
   - Used to document database model.
1. [Django:](https://www.djangoproject.com/)
   - django. 
1. [StackOverflow:](https://stackoverflow.com/)
    - Used for code snippets and tutorials. Invaluable.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the website to ensure there were no syntax errors in the project.

### HTML

This was carried out periodically as each page was created and amended and then finally checked again when pages were deemed complete and error free.

-   HTML pages are built from a common template (base.html) so cannot be directly scanned by url. Testing was achieved by viewing and copying page source into the validator.

-   Due to the nature of the iterative processing within some pages, errors are generated referring to duplicate IDs. Theses are not genuine errors.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
 
    <details><summary>Home Page</summary>
    <img src="/ws-home.png">
    </details>
    <details><summary>About Page</summary>
    <img src="/ws-about.png">
    </details>
    
    </details>
    <details><summary>Search Results Page</summary>
    <img src="/ws-search-results.png">
    </details>
    <details><summary>Sign Up Page</summary>
    <img src=".png">
    </details>
    
### CSS

This was checked periodically as each page was created and CSS code added and amended. A final check was carried out when all other testing had been satisfactorily completed.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

    <details><summary>style.css</summary>
    <img src="/ws-style-css-check.png">
    </details>

### JavaScript

This was checked periodically as each page was created and js code added and amended. A final check was carried out when all other testing had been satisfactorily completed.

-   [jshint JavaScript Validator](https://jshint.com/)

    <details><summary>Main JS - scripts.js</summary>
    <img src="/jshint-scripts-js.jpg">
    </details>

### PeP8

This was checked each time substantial changes were made to PY files. A final check was carried out when all other testing had been satisfactorily completed.

-   [PeP8 Python Linter](https://pep8ci.herokuapp.com)

    <details><summary>init.py</summary>
    <img src="/static/docs/testing/pep8-init.png">
    </details>
    <br>
    <details><summary>env.py</summary>
    <img src="/static/docs/testing/pep8-env.png">
    </details>
    <br>
    <details><summary>models.py</summary>
    <img src="/static/docs/testing/pep8-models.png">
    </details>
    <br>
    <details><summary>routes.py</summary>
    <img src="/static/docs/testing/pep8-routes.png">
    </details>

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals
  
    1. As a First Time Visitor, 
        
        1. The 

        2. There 

        3. There 


    2. As a First Time Visitor, 

        1. The Home page l

        2. The most 
        
        3. There is a search facility on the header of each page.

    3. As a First Time Visitor,
       
        1. A link to signup is clearly displayed in the header menu and also in the 

        2. Once signed up, 
        
        3. Once logged in, 

-   #### Returning Visitor Goals

    1. As a Returning Visitor, 
       
        1. The login button i
        
        2. The 
        
        3. There is a search facility to find 

    2. As a Returning Visitor, 

        1. The latest
        
        2. Each page m

    3. As a Returning Visitor, 
       
        1. Once logged in, 
        
        2. There is a search facility to 

-   #### Frequent User Goals

    1. As a Frequent User, 

        1. There is a 
        
        2. The search 

    2. As a Frequent User, 

        1. Once logged in, 
        
        2. The User 
        
        3. The User c
        
        4. Users can 

    3. As a Frequent User, 

        1. Users can 
        
        2. Users can
        
        3. Users can 
        
### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 280px and upwards as defined in [WCAG 2.1 Reflow criteria for responsive design](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html) on the following browsers:
- Chrome    (123.0.6312.106).
- Edge      (123.0.2420.81).
- Firefox   (124.0.2).
- Safari    (17.4).
- Opera     (109.0.5097.24).

Steps to test:

1. Open browser and navigate to:
    - https://xxxxxxxxxxxxx.herokuapp.com/
2. Open the developer tools (right click and inspect).
3. Set to responsive and decrease width in stages to 280px.
4. Set the zoom to 50%.
5. Click and drag the responsive window to maximum width, noting transitions at breakpoints.
6. Rotate and test for portrait to landscape transition.

Results:

Website is responsive on all screen sizes and no images are pixelated or stretched.
No horizontal scroll is present.
No elements overlap.
Text resizes as expected at breakpoints.
Some content is hidden where it would clutter smaller screens.

Website was also opened on the following devices and no responsive issues were seen:

- iPhone X, 12, 14.
- Apple iPad 12.9.
- Fujitsu 15.4in laptop.
- Hp 22in desktop.

### Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development
and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs.

- Color contrasts meet a minimum ratio as specified in
  [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html).    

- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user.

- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions.

- All non-textual content has alternative text or titles so descriptions are read out to screen readers.

- HTML page lang attribute has been set.

- Aria properties have been implemented correctly.

- WCAG 2.1 Coding best practices being followed.

- Hyperlink text colour has been adjusted to adhere to contrast guidelines.

Results:

Pages that display lists of Posts and comments use the same formatting and colour schemes so it isn't strictly necessary to check all pages with identical contrast and colour components.
-   WCAG results:

    <details><summary>Home Page</summary>
    <img src="/static/docs/testing/wcag-home.png">
    </details>
    <br>
    <details><summary>About Page</summary>
    <img src="b/static/docs/testing/wcag-about.png">
    </details>
    <br>
    
    <br>
    <details><summary>Search Results Page</summary>
    <img src="/static/docs/testing/wcag-search-results.png">
    </details>
    <br>
    
   

Manual tests were also performed to ensure the website was as accessible as possible.

### Screen Reader

Screen reader testing was performed using NVDA software from [NV Access](https://www.nvaccess.org/).
This confirmed that:

-   All text is readable.
-   All images have accurate, useful text descriptions.

### Lighthouse Testing
-   The create comment page is a modal and part of submit thread, so testing of that page covers both scenarios.   

    <details><summary>Home Page</summary>
    <img src="/static/docs/testing/ws-light-home.png">
    </details>
    <br> 
    <details><summary>About Page</summary>
    <img src="/static/docs/testing/ws-light-about.png">
    </details>
    <br>
   

### Functional Testing

- #### Navigation Links

    Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design.

    This was done by clicking on the navigation links on each page on a desktop, laptop, tablet and mobile device.

    Additionally, Adminstrator and basic user accounts were created to check that correct menu options were presented and enhanced functionality restricted to Administrator privileged accounts. 

    Modals and forms display as expected. Edit/Delete functions are correctly restricted to the appropritae owner and user account class. 'Cancel' buttons work as expected.

    Links on all pages navigated to the correct pages as expeccted. External content opens in a new page.

-   #### Testing Approach

    Basic functions were tested with minimal validation. Navigation tested before working code was added. Each function, such as Edit was tested and then replicated to other record types. 

    Minor errors were logged and development continued until a function was constructed then the error list was revisited.

    Functionality was tested against individual user permissions and then against additional users.

    URLs for management functions and access to specific records were copied and attempted access from unauthorised accounts or when logged out to test security.

    Data was checked on screen, and referential integrity checked via psql to ensure cascade deletion was working correctly, record relationships were being linked to the correct owner and no orphaned records were being created. 

    Create:

    -   User Account/login
    -   
        
    Read:

    -   User Profile - Own
    -   

    Update:

    -   User Profile - Own
    -   
   
    Delete:  
    
    -   User Profiles - Admin
    -  

-   #### Test Accounts:
-   The folowing user accounts were created via the signup function rather than direct sql input to test the signup functionality:

    -   Admin:
        *   Username: 
        *   Password: 

    -   Users:
        *   Username: 
        *   Password: 12345678

       
        *   Username: 
        *   Password: 12345678 

        
        *   Username: 
        *   Password: 12345678 


-   #### Sign Up Testing
    -   The cursor is automatically positioned at the start of the first input field.

    -   Accounts are created with a unique ID and posted to the database correctly. Each field is correctly validated and the account cannot be created until all fields are populated with the correct minimum and maximum values.

    -   Email address must be unique and the database is checked for duplicates. Password is checked to ensure it has been entered correctly.

    -   Errors are presented as a Flash message below the sub menu and hero image. 

-   #### Log In Testing
    -   The cursor is automatically positioned at the start of the first input field.

    -   Email address and password are validated against the database.

    -   Errors are presented as a Flash message below the sub menu and hero image. 

-   ####  Testing
    -   . 

    -  

 -  ####  Testing
    -   

    -   
-   ####  Testing

    -   

 -  ####  Testing
    -   
-   ####  Testing
 
    -   
-   #### M Testing

    -   

-   ####  Testing

    -   
-   #### Search Function Testing

    -   

-   ####  Testing

    -   

-   #### Links Testing

    Testing was performed to:

    -   Open each hyperlink on each page and check that it is a valid URL and opens in a new page.
    -   Checked on desktop, tablet and mobile.
    -   Footer Social Media Icons / Links

    Testing was performed:
    -   On the Font Awesome Social Media icons in the footer to ensure that each one opened in a new tab and that each one had a 'grow' hover effect.

    -   Each item opened a new tab when clicked as expected and correct hover effect was present.

-   #### Footer Contact Information

    -   The 'go to' link reacts when hovered over.

### Further Testing

*   

### Bugs and Fixes

*  Link to top button not active in footer.
    -   added z-index to bring to front.

*   env.py not working for storing secret keys
    -   used python dotenv and created root .env file
    
*   Webhook not working with new secret key
    -   stripe test keys had also changed in admin

*   Stripe payments not being recorded
    -   Public key had changed in admin interface. .env updated with new key info.

*   makemigrations fails after django_countries install with error on 'pkg-resources'
    -   found solution online. install 'setuptools'

*   django countries fails to integrate with 'len' error
    -   online solution to replace syntax in order model
    -   choices=CountryField().choices + [('', 'Select Country')]

*   django allauth templates not inheriting from base.html on V 65.4.1
    -   manually added 'extend root base.html' to allauth base.html


-   WCAG contrast issues.
    - 

### Known Bugs

*   

### Future Releases
*   Ideas for future development could include:
    -   

## Deployment

### Version Control

The site was created using the Visual Studio code editor and pushed to the remote repository on GitHub: ‘leos_oreos_project’.

The following git commands were used throughout development to push code to the remote repository:

```git add <file>``` 
    - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”```
    - This command was used to commit changes to the local repository queue ready for the final step.

```git push origin main``` 
    - This command was used to push all committed code to the remote repository on github.

### Clone the Repository Code Locally

*   Navigate to the GitHub Repository you want to clone to use locally:

    - Click on the code drop down button.
    - Click on HTTPS.
    - Copy the repository link to the clipboard.
    - Open your IDE of choice (git must be installed for the next steps).
    - Type git clone copied-git-url into the IDE terminal.

The project will now have been cloned on your local machine for use.

### Heroku

The project was deployed to Heroku using the following steps:

### App Deployment to Heroku

*   You will need to deploy the application using Heroku.

1. Create a requirements.txt file:
    -   Type ``` pip3 freeze --local > requirements.txt ``` in theGitpod CLI.
    -   This shoudl be added to the .gitignore file.
2. Create a Procfile:
    -    Type ```echo web: python app.py > Procfile```.
    -    Open it and remove any spurious lines. It should have a singular line and commence with a capital P.
3. Add and commit these files to Github.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables
  - IP : 0.0.0.0
  - PORT : 5000
  - DATABASE_URL : This is the location of your production database.
  - SECRET_KEY : Your secret key
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right:
  - Select run console.
  - Enter ```python3``` to access the python intepreter.
  - Enter:
    - ```From  import app, db```
    - ```app.app-context().push()```
    - ```db.create_all()```
    - You can then exit the console with ```exit()```

## Credits

### Code

*   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction):
    -   Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

*   [jQuery:](https://jquery.com/): 
    -   jQuery is used to make the JavaScript code more succinct and simplify some processing.

### Content

*   All content was written by the developer with a great deal of assistance from youtube tutorials and stack overflow.

*   Mostly trial and error and getting one function working and then replicating it.

*  

### Media

*   Free background removal on various images using [photoroom](https://www.photoroom.com/tools/background-remover). 

*   The main background image is a standard Microsoft image. Other images are copyright free.

*   Free mockup generator using [Multi Device Website Mockup](https://techsini.com/multi-mockup/).

### Acknowledgements

*   My Mentor for his continuous helpful feedback and support. His industry experience is noticeable in his insighteful guidance. 

*   I can't overestimate the value of Stackoverflow resources at their website and on Youtube.

*   The whole community of developers who freely advise and share their knowledge via blogs, videos and web comments.

*   Tutor support at Code Institute for their support.

*   Tutor support at City of Bristol College for continued support and motivation.