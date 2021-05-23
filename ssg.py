import typer
from ssg.site import Site


def main(source="content",dest="dest"):
    config ={
        "Source":source,
        "dest": dest
    }

    Site(**config).build()


main(typer.run())

