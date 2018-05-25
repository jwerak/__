#!/usr/bin/env python

from cocktail import serve_drink, drinks

import os
import time
import re
from slackclient import SlackClient


def main():
    token = get_token()
    client = SlackClient(token)
    executor = CommandExecutor()

    if client.rtm_connect(with_team_state=False):
        print('BoozeBot connected and running!')
        bot_id = client.api_call('auth.test')['user_id']
        while True:
            command, channel = parse_bot_commands(client.rtm_read(), bot_id)
            if command:
                handle_command(command, channel, client, executor)
            time.sleep(1)
    else:
        print('Connection failed.')


class CommandExecutor(object):
    def __init__(self):
        self.commands = {'read_menu': self.read_menu, 'serve': self.serve, 'help': self.help}

    def handle_command(self, command):
        response = ''
        cmd_list = command.split(' ')
        cmd = cmd_list[0]
        cmd_args = []

        if len(cmd_list) > 1:
            cmd_args = cmd_list[1:]

        if cmd in self.commands:
            response += self.commands[cmd](cmd_args)
        else:
            response += 'Sorry I don\'t understand the command: {0}.'.format(
                command)
            response += self.help()

        return response

    def serve(self, name):
        drink_name = name[0]
        serve_drink(drink_name)
        return 'Your {0} is ready, enjoy!'.format(drink_name)

    def read_menu(self, name):
        response = 'You can order one of these drinks:\r\n'
        receipts = drinks()

        return response + '\r\n'.join(receipts.keys())


    def help(self):
        response = 'Currently I support the following commands:\r\n'

        for command in self.commands:
            response += command + '\r\n'

        return response


def parse_bot_commands(slack_events, bot_id):
    for event in slack_events:
        if event['type'] == 'message' and 'subtype' not in event:
            user_id, message = parse_direct_mention(event['text'])
            print(event)
            if user_id == bot_id:
                return message, event['channel']
    return None, None


def parse_direct_mention(message_text):
    matches = re.search('^<@(|[WU].+?)>(.*)', message_text)
    if matches:
        return matches.group(1), matches.group(2).strip()
    return None, None


def handle_command(command, channel, slack_client, executor):
    response = executor.handle_command(command)
    slack_client.api_call(
        "chat.postMessage", channel=channel,
        text=response or 'no comprendo ingles')


def get_token():
    slack_bot_token = os.environ.get('SLACK_BOT_TOKEN')
    if slack_bot_token is None:
        print('BoozeBot needs api token in SLACK_BOT_TOKEN env variable.')
    return slack_bot_token


if __name__ == '__main__':
    main()
