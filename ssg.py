import typer
from ssg.site import Site

def main(source = "content", dest = "dist"):
    #print("Starting")
    config = {"source": source, "dest": dest}
    site = Site(**config).build()
    #print("Done")

typer.run(main)