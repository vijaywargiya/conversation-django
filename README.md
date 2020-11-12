Conversation Django App

A sample app that manages conversations between users and operators.

The app is deployed on heroku and the exposed endpoints can be found in the postman collection.
https://www.getpostman.com/collections/8d83b42aedeb3dc3b5f6

The chat payload supports variable formatting. Examples - 
1. Hello. This is {{ operator.name }}. How can I help you?
2. Sure {{ user.name }}. Here is your code {{ store.discount_code }}
