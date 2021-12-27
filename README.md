# expense-tracker ---> In this python django project, we will create an expense tracker that will take details of our expenses. While filling the signup form a person
                       will also need to fill in the details about the income and the amount he/she wants to save. Some people earn on a daily basis, so their income can
                       also be added on a regular basis. Details of expenses will be shown in the form of a pie chart on a weekly, monthly, and yearly basis. Installation 
                       of django is a must to start with the Expense Tracker project.

# Project File Structure -->1. Install django framework
                            2. Create a project and an app
                            3. Models.py
                            4. Admin.py
                            5. Urls.py
                            6. Views.py
 # 1. Install django framework:
                              To begin with the project, you need to install django on your system. To install django, write the following command on cmd or terminal window.
   2. Create a project and an app:
                              We will create a new project named ExpenseTracker and an app to start the project. Write the following command on the terminal window.
   3. Models.py ->
               Database connectivity is done with the help of models.py. Create the following models in models.py file in the app of your project
   4. Admin.py --> It will help register the tables in the database.
   5. urls.py --> code explanation : These are the names of the urls that we can access. If we try to access urls other than these, it will give an error.

                                     a. path(): It is used to route the url with the functions views in your app folder.

                                     b. include(): An element is returned by it, to include that element in urlpatterns.
    6. views.py --> Code Explanation:
                    a. Render: It returns the Httpresponse object and combines the template with the dictionary that is mentioned in it.
                    b. HttpResponse: It displays a text response to the user.
                    c. Redirect: It redirects the user to the specified url.
                    d. Messages: It helps to store and display messages to the user on the screen.
                    e. Authenticate: It verifies the user.
                    f. User: This model handles authentication as well as authorization.
                    g. Session: It helps the user to access only their data. Without sessions, every user’s data will be displayed to the user.
    7. Login and Index function:- code explain --->               
                                  home() is a function that allows the user to access the dashboard once the user is logged in. index() function contains the backend of the dashboard page.

                                   a. filter(): Queryset is filtered by filter().

                                   b. get(): Single unique object can be obtained with get().

                                   c. order_by(): It orders the queryset. 
     8. d. Updating Profile:-- profile_update() function performs the backend of the edit profile form. User.objects.get() gets all the information 
                                of the user then all the updated information is saved again. This function is performed by save().                              

     9 . Signup, Login, and Logout :-- handlesignup() function handles the backend of signup form. Uname, fname, lname, email , pass1, pass2, income, savings and profession
                                                    will store the information of the form in these variables.Various conditions are there to sign up . The username should be
                                                    unique, pass1 and pass 2 should be the same and also the length of the username should be maximum 15 characters.
                                                    handlelogin() handles the backend of the login page. If the information entered by the user is correct, the user will
                                                    be redirected to the dashboard. handleLogout() handles the backend of logout.

                                                   a. error(): This function gives the error message on the screen if a condition is not satisfied.

                                                   b. len():This function returns the length of the string, array, dictionary etc.

                                                   
                                                   c. success():If a condition is satisfied, it displays the message that is specified in the parentheses.
      summery -->  We have successfully created the expense tracker project in python                                         
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
