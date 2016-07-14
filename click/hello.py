import click

@click.command()
@click.option('--name', default='Javier')
@click.argument('output', type=click.File('w'), default='-')
def cli(name, output):
    click.echo('Hello %s' % name, file=output)

if __name__ == '__main__':
    cli()
