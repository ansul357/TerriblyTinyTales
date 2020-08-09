# TerriblyTinyTales Assignment
Display the top N words and their frequency of occurrence in the frontend, in a tabular format.

# Components use:

Back-end: Used Python(Flask) for creation of Apis that gets data from file which is hosted on the server. Used re, urllib, request, jsonify modules.

Front-end: Used HTML, Bootstrap, and AngularJS framework. In angularJS called the flask API that is hosted on Heroku.

# Test Cases:
1.when user enters <=0 value or no value: submit button will not be active

2.when user enters >=325 value: alert message for value exceeded (no unique words more than 325)

3.when user enters value in the range: table generated with columns (no., word, frequency count) with N rows.
