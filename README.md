## Process Mining with Alpha Algorithm and Heuristic Miner

## Project's Objectives

Implement a webservice to provide process discovery results in a light-weight form in order to facilitate the analysis of process execution data for non-technical experts. The webservice should take a XES file as input and depict the results of a process discovery algorithm.

Understand and successfully implement alpha algorithm to execute the process mining. Additional algorithm(s) implemented here is heuristic miner.

## Implementation Details

Python 3.11.4 is currently used. All the dependencies and additional python packages can be found in requirements.txt.

Server side: uses Flask framework to receive Http request and send back Http response.

Client side: uses Javascript, Html, CSS and React library / Flask framework to send Http request and interact with users.

In your terminal, do as follows:

1. git clone the project
2. pip install -r requirements.txt

Two ways to run the Program:

3. Using Flask framework:

- 3.1. run app.py
- 3.2. navigate to http://127.0.0.1:5000/api/upload to upload file.

4. Using React library:

- 4.1. cd frontend
- 4.2. npm install react-scripts
- 4.3. npm start

  After a few seconds, the web app will be opened on your browser at http://localhost:3000/.

- 4.4. run app.py

  go back to http://localhost:3000/ to interact with the web app.

  Note: Once installed, the app can be executed without steps 1, 2 and 4.2.
