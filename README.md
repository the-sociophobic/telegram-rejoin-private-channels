# telegram-rejoin-private-channels

If you are subscribed to 500+ channels, Telegram will silently unsubscribe you from the old ones. If it were private channels with you as admin and the only subscriber, you will not be able to rejoin them. They will not be shown in the search. Channel name on reposts won't be clickable. Same with group chats. If they are private and you were the only admin, noone can put you back, because there are be no admins! Pavel Durov is f\*cking genius!

Fortunatelly, you can find and rejoin lost channels and groups with this script. Definetelly works for channels and groups created by you. Not tested for others.



1. Go to https://my.telegram.org → API development tools
2. Register your app and replace api_id and api_hash in the script
3. Run script for the 1st time. Enter your Telegram credentials to the console
4. Open Telegram App. Telegram official will ask you in private chat to Data export request. Allow it
5. Run script for the 2nd time. It will create channels.txt
6. Look for the channels and groups you want to rejoin. Copy their ids into ids = \[\]
7. Run script for the 3rd time
8. Check Telegram App. If chats didn't appear on the main screen, try search them
