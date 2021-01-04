import typer
from ssg.site import site

def main(source="content", dest="dist"):
    
    config = {config:["source", "dest"]}
    Site(**config).build()


typer.run(main())