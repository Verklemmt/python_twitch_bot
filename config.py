import json


def load_config():
    with open("./configs/twitch.json") as config_file:
        config = json.load(config_file)

    irc_token = config["irc_token"]
    client_id = config["client_id"]
    nick = config["nick"]
    prefix = config["prefix"]
    initial_channels = config["initial_channels"]

    return irc_token, client_id, nick, prefix, initial_channels
