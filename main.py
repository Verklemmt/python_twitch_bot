from bot import Bot
from config import load_config


def main():
    irc_token, client_id, nick, prefix, initial_channels = load_config()

    bot = Bot(irc_token, client_id, nick, prefix, initial_channels)
    bot.run()


if __name__ == "__main__":
    main()
