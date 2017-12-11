import configparser

config = configparser.ConfigParser()
config.read('jojobot.cfg')

# imgur api variables
client_id = config.get('imgur', 'id')
client_secret = config.get('imgur', 'secret')

# blacklist words variable
blacklist_word = config.get("filter", "joke_word")
react_words = config.get("filter", "react_words")
response = config.get("filter", "response")

# Dio commands
dio_pasta = config.get("command", "dio_pasta")
dio_desc = config.get("command", "dio_desc")
dio_img = config.get("command", "dio_img")
dio_pizza = config.get("command", "dio_pizza")

# Imgur Albums
albums = config.get("imgur", "albums")

# Discord
token = config.get("discord","token")

# Database
database = config.get("database", "database")
user = config.get("database", "user")
password = config.get("database", "password")
host = config.get("database", "host")
port = config.get("database", "port")