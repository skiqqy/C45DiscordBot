# C45DiscordBot
Proprietary™ (that's a joke btw) c45 discord bot.

[![Build Status](https://travis-ci.com/Skippy404/C45DiscordBot.svg?branch=master)](https://travis-ci.com/Skippy404/C45DiscordBot)

## Using the bot
To use the bot, go [here](https://discordapp.com/oauth2/authorize?client_id=694185053156016178&scope=bot&permissions=8)
and add it to your server.

Once added on the server, the command prefix is '>', example of using the bot.
````
>help
````

## Getting Started

### Configuration

Under `resources` one will find `config.default.yml`. This currently holds a template for 
the bot's configurations. Copy `config.default.yml` as a file called `config.yml` and
add all configuration settings. This is done due to the sensitive nature of these settings.

One important setting is to add one's secret token which can be generated 
[here](https://discordapp.com/developers/applications). This is set under `token.secret` in
`resources/config.yml` (the file you just created).

If you dont, the bot will not work, if you dont know how to create a token,
please go read up about Discord bot tokens.

### Running

All dependencies can be found under `resources/requirements.txt`. The following convenience script
will install all Python dependencies required (Python3/Unix):
```bash
./install.sh
```

Once the bot is configured and all dependencies are installed, one can run it using:
```bash
./run.sh
```

All unit tests can be started with:
```bash
./test.sh
```

### Notes

The bot prints output to stdout with regards to what it is doing
