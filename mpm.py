import argparse


parent_parser = argparse.ArgumentParser(description='Manage Minecraft versions and plugins')
parent_subparser = parent_parser.add_subparsers(dest='command')

init_parser = parent_subparser.add_parser('init', help='Initialize a Minecraft server')
init_parser.add_argument('type', choices=['vanilla', 'sponge'], help='The type of Minecraft server you want to init')

args = parent_parser.parse_args()


if args.command == 'init':
    print('hello world')
