from subprocess import run


def test_help(capfd, datadir):
    run(f'python {datadir/"multiword_args.py"} say -h', shell=True)

    output = capfd.readouterr().out

    assert 'words-to-say' in output
    assert '-t, --to-upper' in output

def test_say(capfd, datadir):
    words_to_say = 'hello world'

    run(f'python {datadir/"multiword_args.py"} say "{words_to_say}"', shell=True)

    output = capfd.readouterr().out

    assert words_to_say in output

def test_say(capfd, datadir):
    words_to_say = 'hello world'

    run(f'python {datadir/"multiword_args.py"} say "{words_to_say}" --to-upper', shell=True)

    output = capfd.readouterr().out

    assert words_to_say.upper() in output