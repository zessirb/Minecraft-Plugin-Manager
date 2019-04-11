import argparse

from commands.init import Init
from commands.install import Install


parent_parser = argparse.ArgumentParser(description='Manage Minecraft versions and plugins')
parent_subparser = parent_parser.add_subparsers(dest='command')

init_parser = parent_subparser.add_parser('init', help='Initialize a Minecraft server')
init_parser.add_argument('type', choices=['vanilla', 'spongevanilla'], help='The type of Minecraft server you want to init')
init_parser.add_argument('--version', help='Define the launcher version that will be downloaded')

install_parser = parent_subparser.add_parser('install', help='Install a plugin into the mods folder')
install_parser.add_argument('plugin', help='The path to the plugin or the direct URL')

args = parent_parser.parse_args()


if args.command == 'init':
    init_command = Init(args.type, args.version)
    print('Fetching ' + args.type + ' versions URL...')
    jar_url = init_command.get_version_url()
    print('Downloading installer...')
    init_command.download_jar(jar_url)
    print('Signing EULA...')
    init_command.sign_eula()
    print('Initializing the server...')
    init_command.execute_jar()

if args.command == 'install':
    install_command = Install(args.plugin)
    print('Downloading plugin...')
    install_command.download_plugin()
