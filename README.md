Conversation Django App

A sample app that manages conversations between users and operators.

The app is deployed on heroku and the exposed endpoints can be found in the postman collection.
https://www.getpostman.com/collections/8d83b42aedeb3dc3b5f6

The chat payload supports variable formatting. Examples - 
1. Hello. This is {{ operator.name }}. How can I help you?
2. Sure {{ user.name }}. Here is your code {{ store.discount_code }}


The chats are stored in the Chat table with status "New". A periodic job runs every hour and collects eligible chats 
based on the following criteria and sends them to the user.
1. Chat cannot be outside 09:00 am - 20:00 pm time interval for that specific user's timezone.
2. Only 90 chats can be sent in an hour
3. Chat with status "New"