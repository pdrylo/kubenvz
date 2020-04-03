#!/usr/bin/env python
import argparse
from commands import list_local, list_remote, install, use, uninstall
from sys import exit
from config import VERSION


def print_version():
    print(VERSION)


def add_commands_params(argument_parser):
    commands = argument_parser.add_subparsers(title='commands', dest='commands')
    commands.required = True

    # list
    list_cmd_parser = commands.add_parser('list', help='List Versions')

    list_cmds = list_cmd_parser.add_subparsers(dest='location')
    list_cmds.required = True

    list_local_cmd = list_cmds.add_parser('local', help='List Local Versions')
    list_local_cmd.set_defaults(func=list_local)

    list_remote_cmd = list_cmds.add_parser('remote', help='List Remote Versions')
    list_remote_cmd.set_defaults(func=list_remote)

    # Install
    install_cmd_parser = commands.add_parser('install',
                                             help='Install specific version or version defined in .kubenvz-version file')

    install_cmd_parser.add_argument('version', type=str, help='Version to install', nargs="?", default="")
    install_cmd_parser.add_argument('-f', action='store_true')
    install_cmd_parser.set_defaults(func=install)

    # Uninstall
    uninstall_cmd_parser = commands.add_parser('uninstall', help='Uninstall specific version')
    uninstall_cmd_parser.add_argument('version', type=str, help='Version to install', nargs="?", default="")
    uninstall_cmd_parser.set_defaults(func=uninstall)

    # Use
    use_cmd_parser = commands.add_parser('use', help='Use program version')
    use_cmd_parser.add_argument('version', type=str, help='Version to use', nargs="?", default="")
    use_cmd_parser.set_defaults(func=use)


class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        exit(1)


parser = Parser(description='Manage kubectl, kustomize and helm versions v0.4.0')
parser.add_argument('-V', '--version', action='store_true', dest='print_version')

# Create subparsers for kubectl, kustomize, helm i helmfile commands
programs = parser.add_subparsers(title='program', dest='program')

# Parsers
kubectl = programs.add_parser('kubectl')
kustomize = programs.add_parser('kustomize')
helm = programs.add_parser('helm')
helmfile = programs.add_parser('helmfile')

# Parser specific arguments
kubectl.add_argument('-C', '--classic', action='store_true', dest='classic_repository',
                     help='Use classic kubernetes repository instead of kubectl one')

add_commands_params(kubectl)
add_commands_params(kustomize)
add_commands_params(helm)
add_commands_params(helmfile)

args = parser.parse_args()

try:
    if args.print_version:
        print_version()
    else:
        args.func(args)
except AttributeError:
    parser.print_help()
    parser.exit(0)
