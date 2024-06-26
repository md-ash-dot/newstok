# NEWSTOK NEWS WEBSITE
[NEWSTOK NEWS WEBSITE](https://github.com/md-ash-dot/newstok)

NewsTok is a user-centric news-sharing platform designed with a thoughtful approach to address the diverse needs of its audience. The website's intuitive navigation ensures seamless exploration, allowing users to easily access articles, submit content, and engage in collaborative activities. With a clean and responsive design, NewsTok encourages active participation through features like voting, commenting, and testimonials. Admin capabilities include managing articles, comments, and testimonials via a user-friendly dashboard. The platform's commitment to a dynamic user experience is evident in its design thinking principles and use of technologies like Django, Bootstrap, and Cloudinary. NewsTok strives to create a vibrant community where users can not only consume news but actively contribute to the dialogue.

![Responsive mockup](/images_readme/responsive.png)

## USER EXPERIENCE

### USER GOALS

- Understand the purpose of the website on landing on it.
- Easily navigate around the website.
- View published articles on the home page.
- Visit an article's detail page to view its content.
- Select a category, so they can view the articles of the selected category.
- Find and visit all the social media sites by opening them in a different tab.
- Visit the About page to read the website owner's about content.
- Fill out a form to send a collaboration request.
- Visit the testimonials page to read published testimonials.
- Fill out a testimonial form and submit it.
- Register for an account to log in to the website.
- Log in and log out from the website.
- Visit the New article page to read the guidelines for submitting an article.
- As a logged-in user, submit a new article.
- On opening an article, up-vote or down-vote on it.
- View the vote score of an article.
- Comment on an article after opening it.
- Edit a comment and delete a comment.
- Visit the user profile page to see the logged-in user's article posts.
- View all the comments posted by the logged-in user.
- Edit and delete comments from the user profile page.

### DESIGN

NewsTok is a thoughtfully crafted website that embodies the principles of design thinking, placing a strong emphasis on addressing users' needs and challenges. By adopting an empathetic approach, and learning from the content provided by Code Institute, I have gained a deep understanding of users' perspectives, ensuring that the platform is intuitive and user-friendly. The website not only serves as a repository for news articles but also actively involves users in the content creation process. Through features like user registration, collaboration requests, article submissions, commenting, and voting, NewsTok empowers its community to actively engage with the platform. The incorporation of a testimonial section further fosters a sense of connection, allowing users to share their experiences and feedback. NewsTok's design thinking approach is evident in its commitment to providing a seamless and enriching user experience, encouraging collaboration and participation in the dynamic world of news sharing. 

#### TYPOGRAPHY

The font families used are Roboto and Lato. It aims to strike a balance between playful and clear communication, contributing to a user-friendly interface that aligns with the website's goal of making it accessible to users of all ages.
 
### WIREFRAMES

Wireframes were designed using Lucidcharts's online wireframe tool.
![Wire frames](/images_readme/wireframe.jpeg)
 
## FEATURES

### EXISTING USER FEATURES

- **NAVIGATION**

  - The navigation is very simple and easy.
  - The content of the website is presented on the navigation bar making it very easy for users to navigate.
  - The logo also acts as the home page button.
  - The categories can be accessed from a drop-down menu.
  - The users can log in or register by clicking on the buttons on the navigation bar.
  - After logging in the Register and login buttons are hidden.
  - Logged-in users will be able to access the profile and submit new article buttons.
  - The About and Testimonial buttons are displayed on the right side of the navigation bar.
  - The footer holds the copyright information and links to all the social media pages.
![Navigation bar](/images_readme/nav-desktop.png)
![Navigation bar mobile](/images_readme/nav-mobile.png)

- **HOME PAGE**

  - The landing page displays engaging headlines and visuals showcasing a selection of articles, drawing visitors into the platform's content.
  - A clear call to action encouraging users to register, sign up, or log in to access personalized features and contribute their content.
  - A dynamic and visually appealing news feed displaying the latest and trending articles, keeping the landing page fresh and current.
  - The navigation bar makes it easy for users to quickly decide on what they want to do on the website.
  - The articles with their pictures, titles and information like author, excerpt and created dates, make it easy for users to pick one and dive right in.
![Landing page](/images_readme/responsive-desktop.png)

- **ARTICLE DETAIL VIEW**

  - The detailed view of each article can be accessed by clicking on it. 
  - The article's picture is uploaded or the default placeholder image is displayed on the top, making the page look more lively.
  - The title, author and created on date are displayed alongside the article's image. Giving the user all the information they need before proceeding down to the article.
  - The content is featured below the image. The article's content can be styled by the admin before publishing it.
  - If the article is the user's own article they can see the buttons: Delete Article and edit article.
  - They can click on delete to delete the article or they can click on edit and edit the article form and submit for approval.
  - A message stating Log in to vote is displayed under the content, prompting users to log in and vote.
  - The Voting section can be found right below the article's content, so users can share their view of the article at the click of a button
  - Users can click on the up-vote or down-vote button and also see the vote's score.
  - The logged-in as, with the user's name is displayed on the top of the voting section.
  - A share button is displayed right underneath the voting section. Alongside a message prompting the user to click on it to share the article.
  - A message stating the Link to this article copied to the clipboard and ready to SHARE! is displayed if the button is clicked.
  - A comment count is displayed on top of the comment section, showing the total number of comments on the article.
  - Below the approved comments are displayed, and a message prompts users to log in to comment.
  - In the case of logged-in users all their pending comments are also seen in this section.
  - The user's comments also display an edit and delete button for each of their comments.
  - The text area for a new comment is displayed for the logged-in users right beside the comments.
![Article detail view](/images_readme/detail%20view.png)
![Article detail view](/images_readme/article%20buttons.png)
![Article detail view](/images_readme/vote.png)
![Article detail view](/images_readme/comment.png)



- **REGISTER PAGE**

  - The register page displays a message to sign up or to log in if the user already holds an account, along with a link to sign in.
  - The account registration form can be found right below to message.
  - The registration form has username, email, password and password(again) fields.
  - The information about password conditions can be found next to the password field.
  - the users can click on the signup button to submit the form and register.
  ![Register page](/images_readme/register.png)

- **LOGIN PAGE**

  - The login page displays a message, welcoming the user to log in if they would like to comment, vote, and submit a new article or to sign up if they don't already have an account.
  - The login form can be seen right below the message.
  - The forms hold the username, password and remember me fields with a button to sign to the user's account.
![Login page](/images_readme/login.png)

- **LOGOUT PAGE**

  - The logout page can be found on the navigation bar for logged-in users.
  - A warning message asking the user if they are sure they want to sign out is seen,
  - They can proceed to click on sign out to log out of their account.
![Logout page](/images_readme/logout.png)

- **PROFILE PAGE**

  - The profile page can be accessed by clicking on the profile button by logged-in users on the navigation bar.
  - On clicking they are taken to a page which displays a message, my posts, below which all the article posts of the logged-in user are displayed, in a similar manner to the home page.
  - The users can delete their posts by clicking delete or click on edit to take them to the article form where they can edit and submit for approval.
  - The users can find a go to your comments button on the top of the page.
  - On clicking on the go to your comments button, they are taken to a page with a message saying my comments, and also a go to your posts button on the top of the page, if they wish to go back to their posts.
  - The user's comments are displayed along with the title of the article to which the particular comment belongs, the unapproved comments are greyed out like in the article detail view.
  - The users can click on edit or the title to take them to the article and edit their comments.
  - They can delete their comment by clicking on the delete button, and reading and accepting the warning message that pops up.
![My posts page](/images_readme/profile%20posts.png)
![My posts page](/images_readme/my_posts.png)
![My comments page](/images_readme/profile%20comments.png)

- **NEW ARTICLE PAGE**

  - The new article page can be accessed by clicking on the submit new article page button on the navigation bar.
  - The new article pages display a message welcoming the user, below which the guidelines and submission process are explained in a few simple points.
  - The user can then proceed to fill out the new article form with the title, category and content fields provided.
  - The filled-out form can be submitted using the submit button after filling out the new article form.
![New article guidelines](/images_readme/article%20guideline.png)
![New article form](/images_readme/article%20form.png)
![Update article form](/images_readme/update_article.png)

- **ABOUT PAGE**

  - The About page shows an image uploaded by the admin.
  - The About text can be found right next to the image, which speaks about the platform and the creator of the platform.
  - The Let's Collaborate form can be found right beneath it.
  - The collaborate form has name, email and message fields along with a button to submit the collaboration request.
![About page](/images_readme/about.png)
![About form](/images_readme/about%20form.png)

- **TESTIMONIALS PAGE**

  - The testimonial page can be accessed by clicking on the navigation button on the right.
  - The users can see the testimonials in cards similar to the articles on the home page.
  - The name, testimonial and star rating can be seen in each of the cards on the testimonial page.
  - A new testimonial button sits on the top of the page.
![Testimonials page](/images_readme/testimonials.png)

- **NEW TESTIMONIAL PAGE**

  - The new testimonial page can be accessed by clicking on the new testimonial button on the testimonial page.
  - A message is displayed for the users inviting them to share their testimonials.
  - A new testimonial form can be found below with name, email, testimonial and Rating fields.
  - The users can fill the form out and use the submit button and send their testimonials to us.
![New Testimonial form](/images_readme/testimonial%20form%20.png)

- **THE FOOTER**

  - The footer displays the copyright message, along with a follow us message with all the social media icons.
  - By clicking on the icons, the user is taken to the respective social media site in a new tab on the browser.
![Footer](/images_readme/footer.png)

### EXISTING ADMIN FEATURES

![Admin panel](/images_readme/django-admin-panel.png)
- **ABOUT**

  - The About section in the admin panel can be used to access the about and collaboration requests content.
  - The About page content can be updated using the title, image and content fields. The content can also be styled.
  - Collaboration requests can be reviewed and marked as read.
  

- **NEWS**

  - The news section in the admin panel can be used to access the articles and comments content, posted by the admin and users.
  - The article content can be updated using the title, slug, category, author, image and content, status, excerpt and approved fields. The content can also be styled.
  - User's comments can be reviewed and marked as approved.
  - For the articles, there is a search field, and filters such as by status, approved and created on.
  - For the comments, there is a search field, and filters such as by approved and created on.

- **TESTIMONIAL**

  - The testimonial section in the admin panel can be used to access the testimonials content, posted by the users.
  - The testimonial content can be reviewed and marked as published to publish them. The content can also be styled.
  - There is a search field, and filters such as by status and created on.


### FEATURES LEFT TO IMPLEMENT

- An image slideshow on the homepage using Bootstrap carousel to show featured news articles.
- A search field to the navigation bar to be able to search content, author etc.
- Search fields inside the user profile posts and comments sections.
- Image upload option to the new article form.
- Option to save drafts as user for new articles.
- More categories for the news articles to be categorised in.
- Sort articles on the homepage using a sort filter for users.
- Add up-vote and down-vote buttons right under each article card on the home page, so articles can be sorted according to votes.
- Add up-vote and down-vote functions to comments.
- Report button to report an article or comment to admin, add detail to report by selecting options or filling out a report form.
- An event calendar displaying upcoming events to collaborate on topics in person. Booking system to reserve a seat for the event.
- Display maps using API to show event locations.

### MVT
 
- **MODEL VIEW TEMPLATE**
 - Models, views and templates have been used to design this Django project.

- **MODELS ERD**
  - ERDs Entity relationship diagrams were used to plan each model used in the project.
  - These ERDs helped in understanding the model and relationships better from the start, making it easier to plan.
![Models ERD](/images_readme/NewsTok%20ERD.jpeg)

### TECHNOLOGIES USED
- DJANGO 
- BOOTSTRAP
- MVT - MODEL VIEW TEMPLATE
- Front end CRUD (Create Read Update Delete)
- HTML
- CSS
- JAVASCRIPT
- PYTHON 
- CLOUDINARY
- DJANGO ALLAUTH
- ELEPHANTSQL - PostgreSQL
- HEROKU 

### RESPONSIVE DESIGN

The website uses a responsive design for users to enjoy it across devices. The website maintains a well-laid-out structure without changing the function and feel on different devices like mobiles, tablets, and desktops. This was done by using the bootstrap framework, which uses a mobile-first approach.

- DESKTOP (Macbook)
  
![Responsive desktop](/images_readme/lighthouse_desktop.png)

- TABLET (iPad mini)
  
![Responsive tablet](/images_readme/responsive-tablet.png)

- MOBILE (Galaxy S8+)
  
![Responsive mobile](/images_readme/responsive-mobile.png)

## MANUAL TESTING

### GENERAL
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| Website works on different browsers such as Google Chrome, Microsoft Edge, Mozilla Firefox, Safari, and Samsung Internet. | Tested the website on all mentioned browsers. | The website acted as normally and it worked on all browsers. | No fix needed. |
| Website uses responsive design and functions well on all standard screen sizes. | Used the dev tools device toolbar on the browser to test on different screen sizes. | The website displayed and functioned correctly on all tested screen sizes. | No fix needed. |
| All text on the website is readable and easy to understand. | Manually checked all text content on the website. | The text is readable and easy to understand. | No fix needed. |

### HOME PAGE
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** HOME and LOGO on click should load the default home page. | HOME and LOGO buttons clicked from other pages. | The home page loaded on click from all other pages. | No fix needed. |
| Articles when published should be displayed in the home page. | Set article's status to published and draft. | Articles are displayed when it is published and are not displayed when status is set to draft. | No fix needed. |
| Articles should display their image, category, title, date of posting and excerpt. | An article with all fields changed was published. | All articles displayed their image, category, title, date of posting and excerpt. | No fix needed. |
| **BUTTON** NEXT and PREV on click should take you to the next and previous page. | NEXT and PREV buttons clicked to change the page. | The pages changed on click. | No fix needed. |
| **BUTTON** NEXT and PREV should only appear when needed | Page with only one page of articles was published and more articles were added and visited the next and previous page. | The NEXT button only displayed when there more than one page. The PREV button only displayed when there was a previous page. | No fix needed. |
| Pages should display the current page. | Articles added and changed the page. | The current page and total number of pages was displayed. | No fix needed. |
| **STATUS** LOGGED IN should be displayed on the top. | Logged in and out as user. | LOGGED IN status was displayed with message "You are not logged in"/"You are logged in as *username*" | No fix needed. |

### CATEGORIES PAGES 
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** CATEGORIES on click should display all categories. | CATEGORIES button clicked. | CATEGORIES button on click displayed a drop down menu with all categories. | No fix needed. |
| **BUTTON** GENERAL, BUSINESS, SCIENCE, TECHNOLOGY on click should open page with respective articles. | GENERAL, BUSINESS, SCIENCE, TECHNOLOGY buttons clicked. | On click of all category list buttons respective articles displayed. | No fix needed. |

### AUTHENTICATION
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** REGISTER on click should load sign up page. | REGISTER button clicked. | REGISTER button on click loaded the sign up page. | No fix needed. |
| **BUTTON** REGISTER and LOGIN buttons should be hidden after sign in. | Signed in and signed out as a user. | REGISTER and LOGIN buttons was hidden after sign in. | No fix needed. |
| **BUTTON** LOGOUT, MY PROFILE, SUBMIT NEW ARTICLE buttons should appear only for logged in users. | Signed in and signed out as a user. | LOGOUT, MY PROFILE, SUBMIT NEW ARTICLE buttons appeared only for logged in users. | No fix needed. |
| **BUTTON** LOGIN on click should load sign in page. | LOGIN button clicked. | LOGIN button on click loaded the sign up page. | No fix needed. |
| **BUTTON** LOGOUT on click should load sign out page. | LOGOUT button clicked. | LOGOUT button on click loaded the sign out page. | No fix needed. |
| **BUTTON** SIGNOUT on click should log user out and display message. | SIGNOUT button was clicked on signout page. | SIGNOUT button on click logged user out and displayed message "You have signed out." | No fix needed. |
| **FORM** SIGN UP should take valid username, email, password and password again. The **BUTTON** SIGN UP should submit the form and register user. | All fields filled with valid and inavlid inputs and SIGN UP button clicked. | Form requested valid inputs and form was successfully sent and registered user. | No fix needed. |
| **FORM** SIGN IN should take valid username , password and remember me checkbox. The **BUTTON** SIGN IN should submit the form and log in the user and display message. | SIGN IN form was filled, remember me box was checked and logged in as user. | Form requested valid inputs, remember me box triggered save password and form was successfully sent and logged in the user and displayed message. "Successfully signed in as "username" | No fix needed. |
| **LINK** SIGN IN and SIGN UP on the register and login page on click should open the respective pages. | SIGN IN and SIGN UP links clicked. | SIGN IN and SIGN UP links on click opened respective pages. | No fix needed. |

### PROFILE PAGE
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** MY PROFILE on click should open the profile page. | MY PROFILE button clicked. | MY PROFILE button on click opened the profile page. | No fix needed. |
| **BUTTON** GO TO YOUR COMMENTS on click should open user comments page. | GO TO YOUR COMMENTS button clicked. | GO TO YOUR COMMENTS button on click opened user comments page. | No fix needed. |
| **BUTTON** GO TO YOUR POSTS on click should open user posts page. | GO TO YOUR POSTS button clicked. | GO TO YOUR POSTS button on click opened user posts page. | No fix needed. |
| **BUTTON** DELETE and EDIT should be grayed out for unapproved articles and comments. | Added approved and unapproved articles. | DELETE and EDIT buttons grayed out, changes colour with hover for unapproved articles and comments. | No fix needed. |
| Unapproved articles and comments text should be grayed out and should display a message. | Added approved and unapproved articles. | Text grayed out for unapproved articles and comments and message "This article/comment is awaiting approval" displayed. | No fix needed. |
| **BUTTON** DELETE under articles/comments on click should ask for confirmation to delete. | DELETE button clicked. | On click a modal was opened asking for confirmation with DELETE and CLOSE buttons | No fix needed. |
| **BUTTON** DELETE and CLOSE in modal on click should close the modal or confirm deletion and display message. | DELETE and CLOSE buttons clicked. | CLOSE button on click closed modal. DELETE button on click deleted article/comment and displayed message "Article/Comment deleted". | No fix needed. |
| **BUTTON** EDIT under articles/comments on click should open page for editing. | EDIT buttons clicked. | EDIT button on click opened pages for editing. | No fix needed. |

### ARTICLE DETAIL PAGE
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** ARTCLE TITLE in the home and my posts page on click should open respective articles. | ARTCLE TITLE buttons clicked on home and my posts page. |  ARTCLE TITLE buttons on click opened respective article detail pages. | No fix needed. |
| **STATUS** LOGGED IN should be displayed under the article content to vote. | Logged in and out as user. | LOGGED IN status was displayed with message "Log in to vote"/"VOTE: Logged in as *username*" | No fix needed. |
| **BUTTON** UPVOTE and DOWNVOTE on click should register a vote or remove a vote. | UPVOTE and DOWNVOTE buttons clicked. | UPVOTE and DOWNVOTE buttons registered and removed vote. | No fix needed. |
| **COUNTER** SCORE should change number in a incremeents of each vote. | Upvoted and downvoted. | SCORE counter changed number in a incremeents of each vote and displayed the score. | No fix needed. |
| **BUTTON** SHARE on click should copy link to the current article and display message. | SHARE button clicked. | SHARE button on click copied current page link to clipboard and changed message "Click SHARE to copy article link to clipboard." to "Link to this article copied to clipboard and ready to SHARE!" | No fix needed. |
| **COUNTER** COMMENTS should display number of approved comments. | Added comments with status approved and not approved. | COMMENTS counter displayed the number of approved comments. | No fix needed. |
| **BUTTON** DELETE under comments on click should ask for confirmation to delete. | DELETE button clicked. | On click a modal was opened asking for confirmation with DELETE and CLOSE buttons | No fix needed. |
| **BUTTON** DELETE and CLOSE in modal on click should close the modal or confirm deletion and display message. | DELETE and CLOSE buttons clicked. | CLOSE button on click closed modal. DELETE button on click deleted comment and displayed message "Comment deleted". | No fix needed. |
| **BUTTON** EDIT under comments on click should pre-populate the comment form body for editing and change button text to update. | EDIT buttons clicked. | EDIT button on click pre-populated the comment form body for editing and change button text from submit to update. | No fix needed. |
| **FORM** COMMENT should take valid body content. The **BUTTON** SUBMIT/UPDATE should submit the form and show message. | Comment body content filled with valid and inavlid inputs and SUBMIT/UPDATE button clicked. | Form requested valid inputs and form was successfully sent and displayed message. "Your comment has been submitted for approval" | No fix needed. |
| Comments should be displayed with Name, time, and content. | Comments posted. | Comments displayed Name, time, and content. | No fix needed. |
| Unapproved comments of logged in user should show with message and grayed out. | Posted unapproved comments. | logged in user's unapproved comments displayed with message "This comment is awaiting approval" and grayed out. | No fix needed. |

### TESTIMONIALS PAGE
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** TESTIMONIALS on click should open Testimonial page. | TESTIMONIAL button clicked. | TESTIMONIAL button on click opened the testimonial page. | No fix needed. |
| **BUTTON** NEW TESTIMONIAL on click should open new testimonial form. | NEW TESTIMONIAL button clicked. | NEW TESTIMONIAL button on cicked opned new testiminial form. | No fix needed. |
| **FORM** NEW TESTIMONIAL should take valid name, email, testimonial and rating. The **BUTTON** SUBMIT should submit the form and display message. | All fields filled with valid and inavlid inputs and SUBMIT button clicked. | Form requested valid inputs and form was successfully sent and displayed message "Your testimonial form has been submitted". | No fix needed. |
| Testimonial page should display all approved testimonials with name, testimonial and ratings. | Add approved and unapproved testimonials. | Only approved testimonials with name, testimonial and ratings were displayed. | No fix needed. |

### ABOUT PAGE
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** ABOUT on click should open About page. | ABOUT button clicked. | ABOUT button on click opened the about page. | No fix needed. |
| **FORM** COLLABORATE should take valid name, email, and message. The **BUTTON** SUBMIT should submit the form and display message. | All fields filled with valid and inavlid inputs and SUBMIT button clicked. | Form requested valid inputs and form was successfully sent and displayed message "Collaboration request received! I endeavour to respond within 2 working days.". | No fix needed. |
| About page should display a title, picture, updated on and content submitted by admin. | Upload picture, update title and content on Admin panel. | The about page displayed the title, picture, updated on and content submitted by admin. | No fix needed. |

### NEW ARTICLE PAGE
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| **BUTTON** SUBMIT NEW ARTICLE on click should open new article page. | SUBMIT NEW ARTICLE button clicked. | SUBMIT NEW ARTICLE button on click opened the new article page. | No fix needed. |
| **FORM** ARTICLE should take valid title, category and content. The **BUTTON** SUBMIT should submit the form and display message. | All fields filled with valid and inavlid inputs and SUBMIT button clicked. | Form requested valid inputs and form was successfully sent and displayed message "Article submited successfully and is awaiting approval.". | No fix needed. |
| Submit article page should display guidlines and submission process. | Opened submit article page. | Submit article page displays all guidelines and submission process. | No fix needed. |

### FOOTER
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| Footer should be displayed on all pages at the bottom. | Visit all pages. | Footer displayed on all pages at the bottom. | No fix needed. |
| **LINKS** SOCIAL MEDIA on click should open respective sites and in a seperate tab. | SOCIAL MEDIA links clicked. | SOCIAL MEDIA links on click opened respective sites and in seperate tabs. | No fix needed. |

### ADMIN PANEL
| **Expected** | **Testing** | **Result** | **Fix** |
|--------------|-------------|------------|---------|
| Log in as admin/superuser. | User admin/superuser credentials to log in. | Log in to Admin panel as admin/superuser. | No fix needed. |
| ABOUT section should take a title, image, content, summernote editor and update the about page on save. | Added title, image, content with summernote editor. | The about admin panel section added, edited and saved all fields. | No fix needed. |
| COLLABORATE REQUESTS should take the form with inputs, email, message and recieve it for review and mark to read. | Colloborate form was filled and sent. | All fields were shown on admin panel and was marked read. | No fix needed. |
| ARTICLES section should show title, slug, category, author, image uploader, content, ecerpt, votes, voted users, approved check box and status for published and draft. | Submitted article form, updated fields and approved, published. Edited article through form and checked status and approval. | Article form on submission was sent to Admin and on filling fields and publishing article was published. O  editing through article form, form status was changed to draft and unapproved. | No fix needed. |
| COMMENTS section should take comment form content and show article, author, body, approval staus. | Comments were posted and edited. | On comment form submission admin panel showed all fields and on approval comments were visible. On editing comment approval status was changed. | No fix needed. |
| TESTIMONIALS section shoukld take form name, email, testimonial, rating, status. | Testimonial form was filled and sent. | On form submission, all fields were sent to admin panel and on changing status testimonial was published. | No fix needed. |
| All admin features should function properly. | All sections of admin panel and features were used. | All admin panel sections and it's  features functioned properly. | No fix needed. |


### VALIDATOR TESTING

- CI Python Linter 

  - No major errors were found except for the E501 line too long ,when passing through the official [CI Python Linter](https://pep8ci.herokuapp.com/)
  - Line too long errors were not corrected, due to time constraints and fear of breaking the code.

- HTML

  - No major errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
  - In article detail views CSS: font-optical-sizing: Property font-optical-sizing doesn't exist was returned.
  - In testomonials page CSS: white-space-collapse: Property white-space-collapse doesn't exist was returned.
  - These were probably created from the rich text in the admin panel and were not corrected, due to time constraints and in fear of breaking the code.

- CSS

  - No errors were found when passing through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/)

![css Validator](/images_readme/css-validator.png)

- JSHint

  - No major errors were found except for " " is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz), when passing through the official [JSHint code quality tool](https://jshint.com/)

- ACCESSIBILITY
  
  - The colours and fonts used are easy to read and checked using lighthouse in dev tools for mobile and desktop.
  - Lighthouse desktop.

![Accessibility score](/images_readme/lighthouse_desktop.png)

 - Lighthouse mobile.

![Accessibility score](/images_readme/lighthouse-mobile.png)

## BUGS

### SOLVED BUGS

- Model category TypeError: 'tuple' object is not callable

  - Fix: There was a missing comma

- Add check to see if the user is authenticated in the comment delete model

  - Fix: if comment.author == request.user and request.user.is_authenticated:

- In news views.py there was a vulnerability

  - Fix: add request.user.is_authenticated

- IntegrityError at /article duplicate key value violates unique constraint "news_article_slug_key" DETAIL:  Key (slug)=() already exists.

  - Fix: from django.utils.text import slugify article.slug = slugify(article.title)

- IntegrityError at /this-is-a-title/upvote/new row for relation "news_article" violates check constraint" news_article_upvotes_check" DETAIL:  Failing row contains (23, this is a title, this-is-a-title, this is content, 2024-02-22 22:26:16.62371+00, 1, 1, , 2024-02-22 22:35:21.743062+00, image/upload/placeholder, 0, 0, -1).

  - Fix: Inside voting + and - were placed wrong and .add was supposed to be .remove

- CommandError: 'profile' conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name.

  - Fix: name profile couldn't be used to create the app so user_profile was used instead.

- Comment delete modal and article delete modal would show up at the same time and content in modal was mixed.

  - Fix: Change button class names and arialabel names to different ones for comment and article buttons.

- content submitted on the admin panel and displayed on the front end displayed in HTML format with p tags etc.
  
  - Fix: {% autoescape off %} {% endautoescape %} was used.

- If title had quotes the button wouldn't work

  - Fix: Add escapejs filter to title.

- Delete buttons on deployed site did not work.

  - Fix: Collect static files using python manage.py collectstatic


## DEPLOYMENT

### GITPOD IDE
- This site was deployed using Gitpod IDE for development. The steps used to deploy are:
  - Open GitHub repo with the Gitpod IDE.
  - Run command in terminal: python3 manage.py runserver
  - Open port 8000 as a preview or in a browser tab.
  - Copy paste the hostname between the square brackets of ALLOWED_HOSTS in the newstok/settings.py file, and saved it.
  - Run command in terminal again: python3 manage.py runserver

### HEROKU
- This site was deployed using Heroku. The steps used to deploy are:
  - Navigate to the Heroku dashboard and create a new app with a unique name in a region close to you.
  - In the new app’s settings tab, ensure the Config Var DISABLE_COLLECTSTATIC key has a value of 1.
  - Use pip3 to install gunicorn~=20.1 and freeze it to the requirements.txt file.
  - In the Procfile, add a command using gunicorn and newstok wsgi file to start the webserver.
  - In the newstok/settings.py file, set the DEBUG constant to False and append the '.herokuapp.com' hostname to the ALLOWED_HOSTS list.
  - Git add, commit and push the code to the GitHub repo.
  - In the new app’s Deploy tab, search for the GitHub repo and connect it to the Heroku app. Manually deploy the main branch of this GitHub repo.
  - In the new app’s resources tab, ensure you are using an eco dyno and delete any Postgres database Add-on.
  - Click Open app to open the webpage.

The live link to the deployed website can be found here - [NEWSTOK](https://newstok-b91fa7faca2a.herokuapp.com/)

## CREDITS

### CODE

- The Bootstrap Resume project, I Think Therefore I Blog codestar project done by Code Institute has been the code that was used to learn how to build this website.
- The codestar project code has been used as the base and reference for building the NewsTok project. - [codestar](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/4565659a34d648b8b8edd063c3182180/)
- bootstrap documentation was used for bootstrap research and references. [bootstrap docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- Django documentation was used for Django research and references. [django docs](https://docs.djangoproject.com/en/5.0/)
- w3schools was used for general code concept searches. [w3schools](https://www.w3schools.com/)
- mdn web docs_ was used for general code concept searches. [mdn web docs_](https://developer.mozilla.org/en-US/)


### MEDIA
- Fonts used on the website. - [google fonts](https://fonts.google.com/) 
- Fonts used on the website. - [font awesome](https://fontawesome.com/)
- css used on the website. - [bootstrap](https://getbootstrap.com/)
- Wireframes were created using Lucidchart's online wireframe maker. - [lucid chart](https://www.lucidchart.com/pages)
- ERD models were also created using the Lucidchart's online ERD maker. - [lucid chart](https://www.lucidchart.com/pages)
- Images used on the website. - [pexels](https://www.pexels.com/)
- The logo used on the website was generated using IconGeneratorAI [icongeneratorai](https://www.icongeneratorai.com/)

### PROJECT SUPPORT
- I would like to thank my mentors Rohit Sharma and Akshat Garg from Code Institute for his support, guidance, and help in planning and building this project.
- I would like to thank all the Code Institute tutors for their support, guidance, and help in solving code issues, debugging, and solving all technical issues faced in building this project.
- I would like to thank Code Institute for providing me with the necessary lessons and resources to help me build my skills to build this project.