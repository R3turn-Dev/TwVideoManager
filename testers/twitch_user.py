from twitch import TwitchClient

from TwVideoManager.twitch.models import User

client = TwitchClient(client_id="8bz5vv13bu9w5kss68oflvzz3z3ge6",
                      oauth_token="nx1fnslbpp90escls1hx8wyzsrkbur")

# Get user from login
user = User.from_login("eunhaklee", client)
print(user)

me = client.users.get()
print(me)
user = User.from_user(me)
print(user)

ssoju = User.from_login("im_ssoju", client)
watcher = user.make_watcher(ssoju)
print(watcher)


# Get user from login
user = User.from_login("bebaldbot", client)
print(user)

ssoju = User.from_login("im_ssoju", client)
watcher = user.make_watcher(ssoju)
print(watcher)