from restic.config import restic_bin
from restic.internal import command_executor


def run(bash_completion_path=None,
        man_directory=None,
        zsh_completion_path=None):
    cmd = [restic_bin, 'generate']

    if bash_completion_path is not None:
        cmd.extend(['--bash-completion', bash_completion_path])

    if man_directory is not None:
        cmd.extend(['--man', man_directory])

    if zsh_completion_path is not None:
        cmd.extend(['--zsh-completion', zsh_completion_path])

    return command_executor.execute(cmd)