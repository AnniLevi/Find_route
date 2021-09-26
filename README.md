# Find Route

Site for finding a route between specified cities.

Representation of cities in the form of vertices of a directed graph. 
Search for routes between the vertices of the graph by traversing the graph in depth (Depth-first search).

Used Python (Django), HTML, CSS, Bootstrap.
Deployed on Heroku.
____

#### Cities
Implemented adding, editing, deleting cities and page-by-page viewing of all available cities. 
The city has a name.

#### Trains
Implemented adding, editing, deleting a train, and page-by-page viewing of all available trains. 
The train has a unique code (name), route start (city), route end (city) and travel time in conventional units. 
There can be several trains from one point to another, but they must differ in travel time.

#### Routes
The user selects the starting and ending point of the route, and also indicates the maximum travel time. 
Also, the user can add as many intermediate cities as he wants, through which the route should run. 
The routes suitable for the conditions are unloaded on the page. 
Each route should have a button that allows the user to save this route by giving it a name.
Route output is sorted by lowest travel time. 
That is, the route with the shortest travel time is displayed first. 
The description of the route contains information about where and from where this route leads, travel time, 
and also contains a list of all trains that are on this route, indicating the train number, from where, where, 
and travel time. 
If there are no routes that satisfy the search, a message is displayed.
A separate page with routes view has been implemented. 
The route can only be saved, viewed and deleted. The user cannot edit the saved route.

Only registered users have access to adding / editing trains / cities, as well as deleting any records.
Registration and authorization of users has been implemented.

The code is covered in tests.