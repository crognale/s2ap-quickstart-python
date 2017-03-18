Python Quick Start Sample for Wallet Object API Copyright (C) 2013 Google Inc.

wallet-objects-quickstart-Python
==============================

This sample demonstrates integration of the basic components of the Wallet Objects API.  Review the [quickstart guide](https://developers.google.com/commerce/wallet/objects/quickstart-python) to run the sample.

This sample showcases several aspects of the API
* Creation of Wallet Classes and Wallet Objects
* Save to Wallet insertion of classes and objects
* The Web Service API

## Creation of Wallet Classes and Objects
The code for creation of classes and objects can be found in the offer.py and loyalty.py files.  Each Wallet Object type, such as loyalty, is broken out into its own file.  Classes are inserted using the WobInsertServlet.

## Save to Wallet insertion of Classes and Objects
Save to Wallet is handled on both the client and server. The index.html file is the landing page for the application and includes app.js. The app.js file makes a request to jwt/ to generate Wallet Object type-specific JWTs. The app.js inserts the appropriate g:wallet tags and the Save to Wallet JavaScript after all of the JWTs are generated. 

## Webservice API
The Webservice API handler is the handleWebService function in main.py. This function handles Webservice requests, generates Loyalty Objects converts Loyalty Objects to JWTs, and responds with the JWT. You can configure your discoverable to point to the URL handled by this function.

[![Analytics](https://ga-beacon.appspot.com/UA-46956809-1/walletobjects-quickstart-python/README.md)](https://github.com/igrigorik/ga-beacon)
