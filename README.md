# C45DiscordBot

Proprietary™ (that's a joke btw) c45 discord bot. The bot is currently running
in a docker container on a raspberrypi 3b.

[![Build Status](https://travis-ci.com/Skippy404/C45DiscordBot.svg?branch=master)](https://travis-ci.com/Skippy404/C45DiscordBot)

## Using the bot

To use the bot, go [here](https://discordapp.com/oauth2/authorize?client_id=694185053156016178&scope=bot&permissions=8)
and add it to your server.

Once added on the server, the command prefix is '/', example of using the bot.

```
/help
```

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

Important, when running the bot with your token, you must add this *unique* bot
to your discord server using this link:
````
https://discordapp.com/oauth2/authorize?client_id=YOUR_BOT_ID_HERE&scope=bot&permissions=8)
````
You obtain 'YOUR\_BOT\_ID\_HERE' at the same place where you created your token.

All dependencies can be found under `resources/requirements.txt`. The following convenience script
will install all Python dependencies required (Python3/Unix):

```bash
./c45bot compile
```

Once the bot is configured and all dependencies are installed, one can run it using:

```bash
./c45bot start
```

All unit tests can be started with:

```bash
./c45bot test
```

#### Module usage

Modules must be placed under `src/mods/` and also configured in the configuration file.

### Notes

The bot prints output to stdout with regards to what it is doing
