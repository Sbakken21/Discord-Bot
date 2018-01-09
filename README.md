# JojoBot
 A python discord bot using discord.py. This bot is used to manage a Discord server.
 
 ## Features
 * Uses imgur API to compile various albums into a list and parses a random image on command
 * Create a list of names and notes stored on a postgreSQL DB

## Getting Started
### Prerequisites
This script uses python 3.6
Use the included `requirements.txt` to install the necessary libraries.
```
pip install -r requirements.txt
```
### Variable configuration
**Note:** this variable configuration is for local deployment. When used in production/with environment variables this file does not need to be altered. 
 
In `jojobot.example.cfg`:
* set `token` to the token obtained from discord. This can be found at https://discordapp.com/developers/applications/me
* set `id` to the ID given from the imgur API
* set `secret` to the secret given from the imgur API

After setting all variables save `jojobot.example.cfg` as `jojobot.cfg`

### Deploy
This bot is currently deployed using Heroku. The variables for local development are accessed using `dev.py` with `jojobot.cfg`. The file that manages the production variables is `prod.py`, these variables are designed to be used with a virtual environment.
#### How to deploy to Heroku
* Create `runtime.txt`:
```
python-3.6.1
```
* Instructions for using the heroku CLI to deploy the app can be found here: https://devcenter.heroku.com/articles/heroku-cli
* Adjust the variables in the heroku settings to use the environment variables.
