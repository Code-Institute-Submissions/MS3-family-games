# Family Games

### [View the live project here.](https://family-games.herokuapp.com/)

![Mockup Generator](wireframes/am-i-responsive.png)


For my Data Centric Development Milestone Project I have created Family Games Heroku application. Application is designed for families who are tired of routine and need entertainment for long winter evenings without going out of their home.
 
## UX
 
This application focus on families with children. 

 ### User Stories

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

- As a user, I want easy navigation, so that I can easily find what I need.
- As a user, I want to find infomation about games and explanation how to play.
- As a user, I want to find information where to buy game that I like.
- As a user, I want to share games I like with other users.
- As a user, I want opportunity to edit any game if I find a mistake.
- As a user, I want to have my own account, where I can save those games that I like as a collection.
- As a user, I want to use a search bar before inserting new game to prevent repeating.
- As a user, I want to delete the game if I think it is inappropriate.
- As a user, I want to add a game that I'm currently selling to attract more buyers


### Wireframes
I used Balsamiq wireframes to design my project.

![Home Desktop](wireframes/HomeDesktop.png)
![Games Desktop](wireframes/GamesDesktop.png)
![Add Game Desktop](wireframes/AddGameDesktop.png)
![Home Mobile Device](wireframes/HomePhone.png)
![Games Mobile Device](wireframes/GamesPhone.png)
![Add Game Mobile Device](wireframes/AddGamePhone.png)

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

#### Home
- Has eye catching carousel type photo galery.
- Inspiring introduction.
- Shows 3 most recent games.

#### Games
- In this part you can find all added games in alphabetical order.
- Each game is placed inside card.
- On the front of the card user can see name of the game, game image and Buy Here button which leads straight to the shop where user can buy the game he/she likes.
- User can click on the card to see more information: game category, age range, number of players and game description. Also 2 buttons at the bottom: Edit and Delete.

 #### Add/Edit/Delete Game
- In this part user can fill the form with game details.
- Form has _Choose Category_, _Game Name_, _Age Range_, _Number Of Players_, _Link To Shop_, _Image URl_(which is prefilled with default URL) and _Description_.
- User can press _Add Game_ button to submit his form or press _Cancel_ button if changed his/her mind.
- Edit Game form is simular to Add Game form, but is prefilled with old game information which user can update.
- Delete button will delete game from app and Mongo DB and redirects user to Games page.


### Features Left to Implement
- Create Sign Up, Log In and Log Out features.
- Create user profile page where user can save and view chosen games.
- Create Search bar.
- Make _Link To Shop_ field optional, and remove _Buy Here_ button if that field is empty or link isn't correct.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com) - to simplify DOM manipulation.
- [JavaScript](https://www.javascript.com/) - to make application interactive.
- [HTML5](https://en.wikipedia.org/wiki/HTML#:~:text=Hypertext%20Markup%20Language%20(HTML)%20is,scripting%20languages%20such%20as%20JavaScript.) - to create and structure content of the app.
- [CSS](https://en.wikipedia.org/wiki/CSS) - to style application.
- [Python](https://www.python.org/) - to create the back-end function of the app.
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) - microframework for easier python app coding.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - templating language for Python to make code more readable.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) -  is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python.
- [MongoDB](https://www.mongodb.com/) - used MongoDB Atlas to store all games data.
- [GitPod](https://www.gitpod.io/) - to write code for my project.
- [Git Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) - to record changes made to my code.
- [GitHub]() - remote repository to commit and to push to staged changes.
- [Heroku]() - used Heroku to deploy my project.

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

- I received inspiration for this project from X
