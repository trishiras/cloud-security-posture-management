import os
import json
from argparse import Namespace
from cloud_security_posture_management.services import prowler
from cloud_security_posture_management.core.logger import logger
from cloud_security_posture_management.core.input import parse_args
from cloud_security_posture_management.support.enums import MixedTypeEnum


class CloudSecurityPostureManagement(object):
    def __init__(
        self,
        arguments: Namespace,
    ):
        self.data = {}
        self.target = arguments.target
        self.cloud_provider = arguments.cloud_provider
        self.output_via = arguments.output_via
        self.webhook = arguments.webhook
        self.output_file_path = arguments.output_file_path

    def run(self):

        logger.info(
            f"Started generating cloud security posture management report for cloud provider :- {self.cloud_provider}"
        )

        if self.webhook:
            logger.info(f"Webhook URL :- {self.webhook}")

        if self.output_file_path:
            logger.info(f"Output file path :- {self.output_file_path}")

        output_dir = os.path.join(
            os.getcwd(),
            MixedTypeEnum.OUTPUT.value,
        )
        tmp_dir = os.path.join(
            os.getcwd(),
            MixedTypeEnum.TMP.value,
        )
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)

        prowler_response = prowler.run(
            cred_file_path=self.target,
            cloud_provider=self.cloud_provider,
        )

        if prowler_response.success:
            self.data = prowler_response.data
        else:
            logger.error(prowler_response.message)

        with open(self.output_file_path, "w") as fp:
            json.dump(self.data, fp, indent=4, default=str)

        logger.info(
            f"Finished generating cloud security posture management report for cloud provider :- {self.cloud_provider}"
        )


def main():

    arguments, unknown = parse_args()

    cloud_security_posture_management = CloudSecurityPostureManagement(
        arguments=arguments
    )
    cloud_security_posture_management.run()
