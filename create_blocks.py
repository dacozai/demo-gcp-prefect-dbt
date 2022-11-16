from prefect.infrastructure import KubernetesJob, KubernetesImagePullPolicy
from prefect.filesystems import GCS

PROJECT_ID = "PLEASE_FILL_ME"

if __name__ == "__main__":
    k8s_block = KubernetesJob(
        finished_job_ttl=300,
        image=f"gcr.io/{PROJECT_ID}/prefect_gcp_demo:latest",
        namespace="example",
        image_pull_policy=KubernetesImagePullPolicy.IF_NOT_PRESENT,
        service_account_name="prefect-demo",
    )

    try:
        k8s_block.save('kk')
    except Exception as e:
        print(f"the block is created -- {e}")

    gcs_block = GCS(bucket_path="for_eden_demo_prefect")
    try:
        gcs_block.save('demo')
    except Exception as e:
        print(f"the block is created -- {e}")
