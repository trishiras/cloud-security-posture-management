from enum import Enum


class MixedTypeEnum(Enum):
    # Boolean constants
    SUCCESS = True

    # String constants
    OUTPUT = "output"
    TMP = "tmp"


class CloudProvider(Enum):
    AWS = "aws"
    GCP = "gcp"
    AZURE = "azure"
    KUBERNETES = "kubernetes"


class ResponseMessage(Enum):
    PROWLER_MSG = "Prowler did not return any response"


class STDInput(Enum):
    # AWS Default region is `us-east-1`
    # Azure region from `az cloud list --output table`, by default AzureCloud
    PROWLER_AWS = "prowler aws --profile {profile} --output-formats json-ocsf --output-filename {output} --output-directory {output_dir} --verbose --log-file"
    PROWLER_AZURE = "prowler azure --sp-env-auth --output-formats json-ocsf --azure-region {region} --output-filename {output} --output-directory {output_dir} --verbose --log-file"
    PROWLER_GCP = "prowler gcp --credentials-file {cred_file} --output-formats json-ocsf --output-filename {output} --output-directory {output_dir} --verbose --log-file"
