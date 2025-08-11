import os
import typer
from dotenv import load_dotenv
from rich import print
from github import get_all_user_repositories

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
def list_repos(user : str = typer.Option(..., '--user', "-u", help="github user name")):
    """Función para listar los repositorios de un usuario
    
    Args:
        user:
            - str
            - required"""
    
    # Llamada a función para obtener todos los repositrorios
    repo = get_all_user_repositories(username=user)
    print(repo)


if __name__=="__main__":
    app()
    # Ejecutar python main.py repo list --user=CarlosLeonSalazar