# Design Document - Group E

## 1. Problem statement
Our “Personal Finance Planning Application” aims at help users manage their income and expenses by keeping an active records of their entries and providing reasonable suggestions based on analysis of the records.

## 2. Use cases
Our target users are people who want to manage their money. 
Upon opening our program, users will either register or sign in with their account (email address) and password.
Once signed in, users will have a list of options of activities to choose from, as follows.

![User activities](https://github.com/INFO206-Fall2017/Info206_GroupE/blob/master/User%20activities.png)

## 3. Assumptions and constraints
Assumption: inputs are (a) integers(specific numbers or category number) 
		       (b) strings (for the “other” category of the entry part)
		       (c) a fake database of some fake users
<br/>Constraints: lack of knowledge as to how to visualize data, update database, etc.

## 4. Architecture:
All interactions, commands, and visualization will be executed in the Terminal window.

A main component of the program will be a dataframe where information of each user is stored. Thus every time the user logs in and would like to perform one of the listed actions (make a new entry, review expenses, visualize activities, and generate advice), the dataframe is either accessed, edited, or consulted.

An imaginary dataframe of users will be created using dictionaries, numpy arrays, and lists in Python. It will be indexed by timestamp in order for the program to be able to track expenses and incomes as a function of time– this would allow users to assess expenses over certain time periods. The dataframe will be developed using the pandas package in python, and will support data visualizations with graph-making libraries such as matplotlib, and seaborn. 

Classes in the program will generally assess the inputs/command by the user, and interacting with the dataframe correspondingly. 

While reviewing expenses, users may also be able to generate tabulated results. The dataframe supports this as the user demands would just require a subset to be displayed. A class will be built to allow for reviewing of expenses. Some of the attributes will allow for reviewing total expenses, categorical expenses and income, and only categorical expenses. Other attributes will allow the user to view target expense categories, and gain visibility into their highest expense categories. Some attributes will make use of numpy to find sums, averages, mins, and max to present actionable insights to our users

While inputting data, users will be able to change the dataframe in-place. New entries will be entered with their corresponding time-stamp. When choosing to input new data, the user will receive several prompts that will enable the program understand the path the entry must take, in order to place it in the right position in the dataframe. The will be several classes to depending on where the input is intended to be entered in the dataframe. 

Generating advice would require computations across columns in the dataframe in order to inform users about whether they are over or under budget in expense categories. We will create functions that automatically notify users in such scenarios. We may also create class objects that leverage interest of users, and define attributes that assess how they may use surpluses in their budgets to print suggestions and recommendations.

## 5. Implementation plan
Basically for all the features and functions, we will write them on our own based on some existed Python modules, but if there is any further reference needed, we will search and use it properly and cite the source.

For those features we would write:
* a. Review past expenses: we will need to add functions to read data in our csv, and print them out for users. Matching the inputted user login info and the stored row of data is also in this part of job.
* b. Make a new entry: we will write functions that accept users to simply input strings and integers to choose their options recording the new data of financing. Several steps for users result from several functions such as storing personal data, income / expenses amount, and setting specific budgets.
* c. Visualize my activities: This would be the last phase in all our features. We will still finish at least pie charts, line charts and bar graphs, and check if other visualization outputs are useful or needed.
* d. Give me some advice: for this part, we would need simple calculation with codes, but the more complicated part is to build up definition for finance planning.

All features are largely dependent on the structure of our ‘fake’ dataframe, and as such the classes and functions associated with the features can only be completed after the ‘fake’ dataframe is built. 

We estimate it would take 4-6 hours of coding to generate the fake dataframe. 
Once the fake dataframe is generated all features can be developed in parallel. We estimate that all of the four features, developed in parallel, will take a total of 6-7 days with 6 hours of coding per day.

Ayo will generate the fake dataframe, and Muxuan already drew a breakdown sheet to start our program: user login function (with verification and the main menu for users). Basically these are most in our part “a” feature.

Yu-Cheng and Hanyu will code the “b” part for users to input new financial data. We have income / expense segments at this stage, and for both of them, there are several sub-categories so we need subclass to run this feature completely.

For the above two parts, we set to finish them by Oct. 10. Right after then, as an interim phase, all of us will discuss with the definition of “d” part, finishing the simple codes of this part at the same time soon. For the final visualization part, we will collaboratively finish it by Oct. 15.

## 6. Test plan
For testing, it will be great directly running the program and inputting data as normal users do. Also, we would need some stored (fake) data in our database, and test it if we could call the existing data successfully.
We would employ unit tests to test the log-in feature using regular expression matching patterns.
