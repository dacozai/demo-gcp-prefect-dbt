from prefect import flow
from prefect_dbt.cli.commands import trigger_dbt_cli_command


def dbt(path: str, command: str = "dbt debug") -> None:
    trigger_dbt_cli_command.with_options(name=command)(
        command,
        project_dir=path,
        profiles_dir=path,
    )


@flow
def dbt_build(dbt_command: str = "dbt run"):
    repo = "dbt-jaffle-shop"
    dbt(repo, dbt_command)


if __name__ == "__main__":
    dbt_build()
