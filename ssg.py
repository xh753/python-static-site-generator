import typer
from ssg.site import Site

def main(source = "content", dest = "dist"):
    # print("Hello world!")
    config = {"source": source, "dest": dest}
    site = Site(**config)
    # print("Done")

typer.run(main)