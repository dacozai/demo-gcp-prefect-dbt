from prefect import flow, get_run_logger, task
from prefect.context import get_run_context


@task
def bar():
    logger = get_run_logger()
    task_run_name = get_run_context().task_run.name
    logger.info(f"👋 from {task_run_name}!")
    

@flow
def foo():
    # This can be as complicated as you like >:)
    bar()

    
if __name__ == "__main__":
    foo()
