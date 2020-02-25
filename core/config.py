import configparser

import discord


class SECTION:
    class BOT:
        @staticmethod
        def __str__(self):
            'Bot'

        COMMAND_PREFIX = "command_prefix"
        CASE_SENITIVE = "case_sensitive"


class SECRETS:
    @staticmethod
    def __str__(self):
        return 'secrets.ini'

    class DISCORD:
        @staticmethod
        def __str__(self):
            return 'Discord'

        SECRET = 'client_secret'
        TOKEN = 'token'


class ConfigManager:
    def __init__(self, configuration_path):
        self.configPath = configuration_path
        self.config = configparser.RawConfigParser()
        self.secret = configparser.RawConfigParser()
        with open(f"{self.configPath}/core.cfg") as configFile:
            self.secret.read_file(configFile)
        with open(f"{self.configPath}/secrets.ini") as secretsFile:
            self.secret.read_file(secretsFile)

    def newInstance(self, botClass):
        return botClass(
            command_prefix=self.config.get(
                section=SECTION.BOT,
                option=SECTION.BOT.COMMAND_PREFIX,
                fallback='$'
            ),
            case_insensitive=not(self.config.getboolean(
                section=SECTION.BOT,
                option=SECTION.BOT.CASE_SENITIVE,
                fallback=False)
            )
        )

    def token(self):
        return self.secret.get(
            section='Discord',
            option='token'
        )
