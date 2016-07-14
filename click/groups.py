import click

@click.command()
def say():
    print('Say')

@click.command()
def sleep():
    print('Sleep')

@click.group()
def cli():
    pass

if __name__ == '__main__':
    cli()
