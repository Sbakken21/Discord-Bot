import os

# imgur api variables
client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')

# blacklist words variables
blacklist_word = os.environ.get('blacklist_word')
react_words = os.environ.get('react_words')
response = os.environ.get('response')

#ban list words
ban_words = os.environ.get('ban_words')
response_ban = os.environ.get('response_ban')

# Dio commands
dio_pasta = os.environ.get("dio_pasta")
dio_desc = os.environ.get("dio_desc")
dio_img = os.environ.get("dio_img")
dio_pizza = os.environ.get("dio_pizza")

# Imgur Albums
albums = os.environ.get('albums')

# Discord
token = os.environ.get('token')

# Database
database = os.environ.get("database")
user = os.environ.get("user")
password = os.environ.get("password")
host = os.environ.get("host")
port = os.environ.get("port")