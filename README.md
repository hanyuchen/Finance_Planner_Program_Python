# Finance Planner Program
## Muxuan Lyu, Hanyu Chen, Yu-Cheng Lin, Ayo Animashaun
##### Nowadays, people own more and spend more on daily necessities and on various other items, making it difficult for them to have a control over their personal finance. After a brief survey, we found that very few people know where their money goes, and even few actually take actions to better manage their money. Thus, our team plan to design a personal finance planning application to help users manage their personal finance. 
---
The application does the following: 
1. Allows for data entry, and categorizes spending into subcategories

2. Constructs periodic graphs of spending habits

3. Provides more fancy graphs

4. Generates suggestions

## Architecture:
All interactions, commands, and visualization will be executed in the Terminal window.

A main component of the program will be a dataframe where information of each user is stored. Thus every time the user logs in and would like to perform one of the listed actions (make a new entry, review expenses, visualize activities, and generate advice), the dataframe is either accessed, edited, or consulted.

An imaginary dataframe of users will be created using dictionaries, numpy arrays, and lists in Python. It will be indexed by timestamp in order for the program to be able to track expenses and incomes as a function of time– this would allow users to assess expenses over certain time periods. The dataframe will be developed using the pandas package in python, and will support data visualizations with graph-making libraries such as matplotlib, and seaborn. 

Classes in the program will generally assess the inputs/command by the user, and interacting with the dataframe correspondingly. 

While reviewing expenses, users may also be able to generate tabulated results. The dataframe supports this as the user demands would just require a subset to be displayed. A class will be built to allow for reviewing of expenses. Some of the attributes will allow for reviewing total expenses, categorical expenses and income, and only categorical expenses. Other attributes will allow the user to view target expense categories, and gain visibility into their highest expense categories. Some attributes will make use of numpy to find sums, averages, mins, and max to present actionable insights to our users

While inputting data, users will be able to change the dataframe in-place. New entries will be entered with their corresponding time-stamp. When choosing to input new data, the user will receive several prompts that will enable the program understand the path the entry must take, in order to place it in the right position in the dataframe. The will be several classes to depending on where the input is intended to be entered in the dataframe. 

Generating advice would require computations across columns in the dataframe in order to inform users about whether they are over or under budget in expense categories. We will create functions that automatically notify users in such scenarios. We may also create class objects that leverage interest of users, and define attributes that assess how they may use surpluses in their budgets to print suggestions and recommendations.
