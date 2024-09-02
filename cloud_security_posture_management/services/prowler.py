import os
import sys
import json
import uuid
import traceback
from cloud_security_posture_management.core.logger import logger
from cloud_security_posture_management.core.models import Response
from cloud_security_posture_management.support.utils import setup_credentials
from cloud_security_posture_management.support.enums import (
    STDInput,
    CloudProvider,
    MixedTypeEnum,
    ResponseMessage,
)


def run(
    cred_file_path: str,
    cloud_provider: str,
) -> Response:
    resp = Response()
    data = None
    file_dir = os.path.join(
        os.path.join(
            os.getcwd(),
            MixedTypeEnum.TMP.value,
        ),
    )
    file_name = str(uuid.uuid4())
    file = os.path.join(
        os.path.join(
            file_dir,
            str(f"{file_name}.ocsf.json"),
        ),
    )
    try:
        response = setup_credentials(
            cred_file_path=cred_file_path,
            cloud_provider=cloud_provider,
        )

        if cloud_provider == CloudProvider.AWS.value:
            os.system(
                STDInput.PROWLER_AWS.value.format(
                    profile=response,
                    output=file_name,
                    output_dir=file_dir,
                )
            )
        elif cloud_provider == CloudProvider.GCP.value:
            os.system(
                STDInput.PROWLER_GCP.value.format(
                    cred_file=cred_file_path,
                    output=file_name,
                    output_dir=file_dir,
                )
            )
        elif cloud_provider == CloudProvider.AZURE.value:
            os.system(
                STDInput.PROWLER_AZURE.value.format(
                    region=response,
                    output=file_name,
                    output_dir=file_dir,
                )
            )
        else:
            logger.error(f"{cloud_provider} not supported")
            sys.exit(1)

        with open(file, "r") as fp:
            data = json.load(fp, strict=False)
        if data:
            resp.success = MixedTypeEnum.SUCCESS.value
            resp.data = data
    except Exception as err:
        resp.message = ResponseMessage.PROWLER_MSG.value
        logger.error(err)
        logger.debug(traceback.format_exc())

    return resp
