import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

REPOSITORY = Path(__file__).resolve().parent


def launch():
    os.chdir(REPOSITORY)
    with TemporaryDirectory(prefix="mio-dungeons-") as directory:
        runtime = Path(directory)
        with ZipFile(REPOSITORY / "mio_dungeons.bundle") as bundle:
            bundle.extractall(runtime)
        sys.path.insert(0, str(runtime))
        from app.main import main, migration_config

        if sys.argv[1:] == ["--check"]:
            from alembic.script import ScriptDirectory

            from app.engine.scene_graph import assets_info, load_content, scene_index
            from app.settings import Config

            content = load_content()
            scenes = len(scene_index(content))
            assets = len(dict(assets_info(content)))
            migrations = ScriptDirectory.from_config(migration_config()).get_heads()
            if not migrations:
                raise RuntimeError("No Alembic migrations found")
            if not Config().prompt_file.is_file():
                raise RuntimeError("Gemini prompt not found")
            print(f"Mio Dungeons | {scenes} scenes | {assets} assets | migration {', '.join(migrations)}")
            return

        main()


if __name__ == "__main__":
    launch()
