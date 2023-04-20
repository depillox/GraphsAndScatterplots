#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 129
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Titanic dataframe. Working with frequency graphs and scatterplots
#Citations:
#Anything else that's relevant:
import pandas as pd
import matplotlib.pyplot as plt

def dataFrameWork():
    titanic=pd.read_csv('train.csv')
    # Data Info
#    print(titanic.head())
#    print(titanic.columns)
#    print(titanic.info())
#    print(titanic.describe())
#    print(titanic['Sex'].head())
    
#Compute and print the counts of each different value in titanic.Survived
    unique_value_counts = titanic['Survived'].value_counts()
    print(unique_value_counts)



# Get the value counts for the 'Survived' column
    unique_value_counts = titanic['Survived'].value_counts()
    
    # Set up the plot
    fig, ax = plt.subplots()
    ax.bar(unique_value_counts.index, unique_value_counts.values, width=0.4)
    
    # Set the x-ticks to be the strings 'Survived' and 'Not Survived'
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Not Survived', 'Survived'])
    
    # Add the count values as text labels above each bar
    for i, v in enumerate(unique_value_counts.values):
        ax.text(i, v+10, str(v), ha='center')
    
    # Set the y-axis label to 'Count'
    ax.set_ylabel('Count')
    
    # Set the plot title
    ax.set_title('Survival Count')

    # Show the plot
    plt.show()

#I want a scatterplot with column "Survived" and "Fare"
    plt.scatter(titanic['Survived'], titanic['Fare'])
    plt.xlabel('Survived')
    plt.ylabel('Fare')
    plt.title('Survived vs Fare')
    plt.show()
    