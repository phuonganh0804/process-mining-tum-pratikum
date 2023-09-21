## Process Mining with Alpha Algorithm and Heuristic Miner

## Project's Objectives

Implement a webservice to provide process discovery results in a light-weight form in order to facilitate the analysis of process execution data for non-technical experts. The webservice should take a XES file as input and depict the results of a process discovery algorithm.

Understand and successfully implement alpha algorithm to execute the process mining. Additional algorithm(s) implemented here is heuristic miner.

## Structure Overview

The project is structured into two main part including backend and frontend implementations.

The back-end processes the http request and analyzes the input with either alpha algorithm or heuristic miner depending on the request. In case of successful upload, it then responds with a process visualization in form of a PDF file. Alpha algorithm visualize the result with a petri net. Heuristic miner outputs a causal matrix and heuristic net.

The backend folder has two sub-folders, each of which dedicates to the implementation of either alpha algorithm or heuristic miner including test cases for unit testing. There is also a flask app to analyze request from client and send back response.

The front-end implements the user interface and sends request to server. It handles the design of the interactive webpage that allows user to submit one file at a time and get back the result in case of success. Otherwise, there is error alert.

The frontend folder consists of several sub-folder to store files and images for the purpose of design and interaction with end-user.

The input file is stored in/backend/static/uploads. The output is automatically located in the home directory.

## Implementation Details

Python 3.11.4 is currently used. All the dependencies and additional python packages can be found in requirements.txt. To install run pip install -r requirements.txt

The backend uses Flask framework to receives and send back Http response.

The frontend uses Javascript, Html, CSS and React library to send Http request.

In your terminal, do as follows:

1. git clone the project
2. pip install -r requirements.txt
3. cd frontend
4. npm install react-scripts
5. npm start

After a few seconds, the web app will be opened on your browser at http://localhost:3000/.

6. run app.py

go back to http://localhost:3000/ to interact with the web app.

Note: Once installed, the app can be executed without steps 1, 2 and 4.
