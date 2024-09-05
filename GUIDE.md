## Guide for Cloud Security Posture Management (CSPM) Tool

This guide provides detailed instructions on how to build, run, and use the Cloud Security Posture Management (CSPM) Tool designed to continuously monitor, detect, and remediate misconfigurations and compliance issues across cloud environments.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Building the Docker Image](#building-the-docker-image)
4. [Running the Docker Container](#running-the-docker-container)
5. [Tool Usage](#tool-usage)
6. [Troubleshooting](#troubleshooting)
7. [Additional Information](#additional-information)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker
- Git (optional, for cloning the repository)

## Project Structure

```
cloud_security_posture_management/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── GUIDE.md
├── README.md
├── requirements.txt
├── setup.py
|
└── cloud_security_posture_management/
    ├── __init__.py
    ├── __version__.py
    ├── main.py
    |
    ├── core/
    |   ├── __init__.py
    |   ├── input.py
    |   ├── logger.py
    |   └── models.py
    |
    ├── service/
    |   ├── __init__.py
    |   └── prowler.py
    |
    └── support/
        ├── __init__.py
        ├── enums.py
        └── utils.py
```

## Building the Docker Image

1. Open a terminal and navigate to the project directory:

   ```bash
   cd path/to/cloud-security-posture-management
   ```

2. Build the Docker image using the following command:

   ```bash
   sudo docker build --no-cache . -f Dockerfile -t cloud-security-posture-management:latest
   ```

   This command builds a Docker image named cloud-security-posture-management based on the instructions in the Dockerfile.

## Running the Docker Container

To run the Static Application Security Testing Tool inside a Docker container, use the following command structure:

```bash
sudo docker run --dns 8.8.8.8 --rm -it -v $(pwd)/output:/output -v /path/to/cloud/creds:/creds cloud-security-posture-management:latest [arguments]
```

Replace `[arguments]` with the actual arguments for the tool.

### Explanation of Docker run options:

- `--rm`: Automatically remove the container when it exits.
- `-it`: Run container in interactive mode.
- `-v $(pwd)/output:/output`: Mount the local `output` directory to `/output` in the container.
- `-v /path/to/cloud/creds:/creds`: Mount the directory containing cloud credentials to /creds in the container.
- `cloud-security-posture-management:latest`: The name of the Docker image to run.

## Tool Usage

The Cloud Security Posture Management Tool accepts several command-line arguments:

- `-t, --target`: (Required) Path to cloud credential file.
- `-cp, --cloud-provider`: (Required) Specify cloud provider: "aws", "gcp", "azure", or "kubernetes".
- `-ov, --output-via`: (Required) Specify output method: "file" or "webhook".
- `-w, --webhook`: Webhook URL (required if output_via is "webhook").
- `-o, --output`: File path for output (required if output_via is "file").
- `-l, --log`: Log level (DEBUG or ERROR, default is DEBUG).

### Example Commands:

1. Scan AWS environment and output to a file:
   ```bash
   sudo docker run --rm -it --dns 8.8.8.8 -v $(pwd)/output:/output -v /path/to/aws/creds:/creds cloud-security-posture-management:latest -t /creds/aws_credentials.json -cp aws -ov file -o /output/aws_results.json
   ```

2. Scan Azure environment and send results to a webhook:
   ```bash
   sudo docker run --rm -it --dns 8.8.8.8 -v /path/to/azure/creds:/creds cloud-security-posture-management:latest -t /creds/azure_credentials.json -cp azure -ov webhook -w https://your-webhook-url.com
   ```


Note: When using file output or cred directories, you need to mount volumes to access the results or scan creds from your host machine.

## Troubleshooting

1. **Permission Issues**: If you encounter permission problems when writing to mounted volumes, you may need to adjust the permissions or use a named volume.

2. **Network Issues**: Ensure your Docker network settings allow the container to access the target network or webhook URL.

3. **Missing Requirements**: If the build fails due to missing requirements, check that your `requirements.txt` file is up to date and includes all necessary dependencies.

4. **Cloud Provider Authentication:** Ensure that the provided cloud credentials are valid and have the necessary permissions for scanning.


## Additional Information

- The tool uses Python 3.12 as specified in the Dockerfile.
- The CSPM Tool integrates Prowler for cloud security assessments. Prowler commands are used internally for different cloud providers:

   - AWS: ```prowler aws --profile {profile} --output-formats json-ocsf --output-filename {output} --output-directory {output_dir} --verbose --log-file```
   - Azure: ```prowler azure --sp-env-auth --output-formats json-ocsf --azure-region {region} --output-filename {output} --output-directory {output_dir} --verbose --log-file```
   - GCP: ```prowler gcp --credentials-file {cred_file} --output-formats json-ocsf --output-filename {output} --output-directory {output_dir} --verbose --log-file```


## Key Features

**Continuous Monitoring**: Automatically scans your cloud environment for security risks.
**Policy-Driven Assessments**: Evaluates cloud resources against industry standards (CIS, NIST, GDPR).
**Multi-Cloud Support**: Compatible with AWS, Azure, and Google Cloud.
**Risk Prioritization**: Classifies vulnerabilities based on severity.
**Automated Remediation**: Offers options to fix identified misconfigurations.


### PROWLER HELP COMMAND OUTPUT
- [HELP.md](HELP.md) - A detailed prowler `[provide]` --help  command response.

For more information or to report issues, please refer to the project's documentation or repository.