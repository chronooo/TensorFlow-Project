Instructions
--

(This probably shouldn't matter)
VENV: Python version 3.10.6

Main:
Inside the main folder you will find directories that seperate each part of the main project for this assignment. The report is appended to where each section ended.
Reports for main2,3,4 should all be located at the bottom of the respective file, with the previous iterations still there, the report for main1 should be below my data processing. 

Inside main3 and main4, you will find .h5 files labeled with a % number, those are the models that have reached my highest accuracy with the code that is currently in the jupyter notebook (the model code has not been modified since reaching that accuracy), if you decide to train the model again, it will save with main(iteration#)classif.h5, as to not overwrite the model that performed well.

Part 1,2,3:

Part 1:
As stated above, the model labeled 98.1% accuracy is the one that I trained with the current model code you see, if you decide to re-train it, it will save with the name from the assignment, as to not overwrite that model.

Part 2:
Inside this folder you will find two directories, one for the Partial model and one for the Complete model, the starter code is just there for reference. 
Each of them will have a corresponding model for the version it was. These models are not labeled with accuracy, as my complete model only reached 94% accuracy, so it did not meet the bonus grade requirement.

For this part of the assignment I modified predict_test, the changes are explained in the Complete report. 

The entirety of the report is appended to the bottom of the Complete notMNIST notebook in markdown format.

Part 3:
Same gist as above, my heart model reached 76.3% accuracy with the code you see for the model. If you decide to re-run the program it will save as CHD_Model.h5 to not over-write my current well performing model.




New dataset, housing prices in california

https://www.kaggle.com/datasets/kathuman/housing

I will be using the dataset on Housing Prices in California found on Kaggle with a creative Commons Public Domain License

"This dataset is based on data from the 1990 California Census, and incluides metrics such as the population, median income, and median housing proice for each block group in California.
Block groups are the smallest geographical unit for which the US Census Bureau publishes sample data., and each block typically has between 600 to 3000 people."

