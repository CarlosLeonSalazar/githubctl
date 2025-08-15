import os
from enum import Enum

import typer
import jmespath
from typing_extensions import Annotated
from dotenv import load_dotenv
from rich import print


from .github import get_all_user_repositories
from .utils import print_beauty
from .options import OutputOption

if os.path.isfile(".env"):
    load_dotenv()

# crear instancia app de typer
app = typer.Typer()

# crear intancia para manejar los repositorios
repo_app = typer.Typer()

# Añadir la instancia repo_app a app como "repo"
app.add_typer(repo_app, name="repo")


# Crear un comando de repo_app con alias "list"
@repo_app.command(name="list", help="list user repository")
def list_repos(user : Annotated [str, typer.Option(..., '--user', "-u", help="github user name")],
               output : Annotated [OutputOption, typer.Option('--output', '-o', help='output format: json, csv, table')] = OutputOption.table,
               query : Annotated[str, typer.Option('--query', '-q', help='query with jmespath')]=None):
    
    # Llamada a función para obtener todos los repositrorios
    repo = get_all_user_repositories(username=user)
    if query:
        repo = jmespath.search(query, repo)
    
    print_beauty(list_of_dict=repo, output=output)


if __name__=="__main__":
    app()
    # Ejecutar python main.py repo list --user=nombre_usuario