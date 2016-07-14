import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@click.command()
@click.option('--name', default='Javier', help='your name')
@click.option('--repeat', default=1, help='how many times')
@click.argument('output', type=click.File('w'), default='-')
def say(name, repeat, output):
    for _ in range(repeat):
        click.echo('Hello %s!' % name, file=output)

if __name__ == "__main__":
    cli()
