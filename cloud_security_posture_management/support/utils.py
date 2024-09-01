import sys
import json
import uuid
import subprocess
from cloud_security_posture_management.core.logger import logger
from cloud_security_posture_management.support.enums import CloudProvider


def setup_credentials(
    cred_file_path: str,
    cloud_provider: str,
):
    """Function that setup cloud credentials

    Args:
        cred_file_path (str): Path of cloud cred file

    Returns:
        None
    """

    credentials = {}
    with open(cred_file_path, "r") as fp:
        credentials = json.load(fp, strict=False)

        logger.info(f"Credentials loaded successfully from {cred_file_path}")

    if not credentials:
        logger.error(f"Credentials not found in {cred_file_path}")
        sys.exit(1)

    if cloud_provider == CloudProvider.AWS.value:
        profile = uuid.uuid4().hex
        aws_access_key = credentials.get(
            "AWSACCESSKEY",
            "",
        )
        aws_secret_access_key = credentials.get(
            "AWSSECRETACCESSKEY",
            "",
        )
        aws_region_detail = credentials.get(
            "AWSREGION",
            "",
        )
        if aws_access_key and aws_secret_access_key and aws_region_detail:
            aws_access = f"aws --profile {profile} configure set aws_access_key_id {aws_access_key}"
            aws_secret = f"aws --profile {profile} configure set aws_secret_access_key {aws_secret_access_key}"
            aws_region = (
                f"aws --profile {profile} configure set region {aws_region_detail}"
            )
            response = subprocess.run(
                aws_access,
                shell=True,
                check=True,
            )
            if response.returncode != 0:
                logger.error("AWS credentials not found")
                sys.exit(1)
            response = subprocess.run(
                aws_secret,
                shell=True,
                check=True,
            )
            if response.returncode != 0:
                logger.error("AWS credentials not found")
                sys.exit(1)
            response = subprocess.run(
                aws_region,
                shell=True,
                check=True,
            )
            if response.returncode != 0:
                logger.error("AWS credentials not found")
                sys.exit(1)
            return profile

        else:
            logger.error("AWS credentials not found")
            sys.exit(1)

    elif cloud_provider == CloudProvider.GCP.value:
        gcp_credentials_file = credentials.get(
            "GCP_CREDENTIALS_FILE",
            "",
        )
        if gcp_credentials_file:
            return None

        else:
            logger.error("GCP credentials not found")
            sys.exit(1)

    elif cloud_provider == CloudProvider.AZURE.value:
        azure_client_id = credentials.get(
            "AZURE_CLIENT_ID",
            "",
        )
        azure_tenant_id = credentials.get(
            "AZURE_TENANT_ID",
            "",
        )
        azure_client_secret = credentials.get(
            "AZURE_CLIENT_SECRET",
            "",
        )
        azure_region = credentials.get(
            "AZURE_REGION",
            "",
        )
        if azure_client_id and azure_tenant_id and azure_client_secret and azure_region:
            export_cmd = f'export AZURE_CLIENT_ID="{azure_client_id}" && export AZURE_TENANT_ID="{azure_tenant_id}" && export AZURE_CLIENT_SECRET="{azure_client_secret}"'
            response = subprocess.run(
                export_cmd,
                shell=True,
                check=True,
            )
            if response.returncode != 0:
                logger.error("Azure credentials not found")
                sys.exit(1)
            return azure_region

        else:
            logger.error("Azure credentials not found")
            sys.exit(1)

    elif cloud_provider == CloudProvider.KUBERNETES.value:
        credentials = credentials.get("kubernetes")
        logger.error("Kubernetes not supported yet")
        sys.exit(1)

    else:
        logger.error("Cloud provider not supported")
        sys.exit(1)

    return None
