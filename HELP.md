### AWS help command output.


```usage: prowler [-h] [--version] {aws,azure,gcp,kubernetes,dashboard} ... aws [-h] [--status {PASS,FAIL,MANUAL} [{PASS,FAIL,MANUAL} ...]]
                                                                             [--output-formats {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...]]
                                                                             [--output-filename [OUTPUT_FILENAME]]
                                                                             [--output-directory [OUTPUT_DIRECTORY]] [--verbose]
                                                                             [--ignore-exit-code-3] [--no-banner] [--unix-timestamp]
                                                                             [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                                                                             [--log-file [LOG_FILE]] [--only-logs] [--check CHECK [CHECK ...]]
                                                                             [--checks-file [CHECKS_FILE]] [--service SERVICE [SERVICE ...]]
                                                                             [--severity {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...]]
                                                                             [--compliance {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]]
                                                                             [--category CATEGORY [CATEGORY ...]]
                                                                             [--checks-folder [CHECKS_FOLDER]]
                                                                             [--excluded-check EXCLUDED_CHECK [EXCLUDED_CHECK ...]]
                                                                             [--excluded-service EXCLUDED_SERVICE [EXCLUDED_SERVICE ...]]
                                                                             [--list-checks | --list-checks-json | --list-services | --list-compliance | --list-compliance-requirements {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                                                                             | --list-categories | --list-fixer] [--mutelist-file [MUTELIST_FILE]]
                                                                             [--config-file [CONFIG_FILE]] [--fixer-config [FIXER_CONFIG]]
                                                                             [--custom-checks-metadata-file [CUSTOM_CHECKS_METADATA_FILE]]
                                                                             [--shodan [SHODAN_API_KEY]] [--slack] [--profile [PROFILE]]
                                                                             [--role [ROLE]] [--role-session-name [ROLE_SESSION_NAME]] [--mfa]
                                                                             [--session-duration [SESSION_DURATION]] [--external-id [EXTERNAL_ID]]
                                                                             [--region {us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} [{us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} ...]]
                                                                             [--organizations-role [ORGANIZATIONS_ROLE]] [--security-hub]
                                                                             [--skip-sh-update] [--send-sh-only-fails] [--quick-inventory]
                                                                             [--output-bucket [OUTPUT_BUCKET] | --output-bucket-no-assume
                                                                             [OUTPUT_BUCKET_NO_ASSUME]]
                                                                             [--resource-tag RESOURCE_TAG [RESOURCE_TAG ...] | --resource-arn
                                                                             RESOURCE_ARN [RESOURCE_ARN ...]]
                                                                             [--aws-retries-max-attempts [AWS_RETRIES_MAX_ATTEMPTS]]
                                                                             [--scan-unused-services] [--fixer]

options:
  -h, --help            show this help message and exit
  --check CHECK [CHECK ...], --checks CHECK [CHECK ...], -c CHECK [CHECK ...]
                        List of checks to be executed.
  --checks-file [CHECKS_FILE], -C [CHECKS_FILE]
                        JSON file containing the checks to be executed. See config/checklist_example.json
  --service SERVICE [SERVICE ...], --services SERVICE [SERVICE ...], -s SERVICE [SERVICE ...]
                        List of services to be executed.
  --compliance {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                        Compliance Framework to check against for. The format should be the following: framework_version_provider (e.g.:
                        cis_3.0_aws)
  --category CATEGORY [CATEGORY ...], --categories CATEGORY [CATEGORY ...]
                        List of categories to be executed.
  --list-checks, -l     List checks
  --list-checks-json    Output a list of checks in json format to use with --checks-file option
  --list-services       List covered services by given provider
  --list-compliance, --list-compliances
                        List all available compliance frameworks
  --list-compliance-requirements {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                        List requirements and checks per compliance framework
  --list-categories     List the available check's categories
  --list-fixer, --list-fixers, --list-remediations
                        List fixers available for the provider

Outputs:
  --status {PASS,FAIL,MANUAL} [{PASS,FAIL,MANUAL} ...]
                        Filter by the status of the findings ['PASS', 'FAIL', 'MANUAL']
  --output-formats {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...], --output-modes {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...], -M {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...]
                        Output modes, by default csv and json-oscf are saved. When using AWS Security Hub integration, json-asff output is also
                        saved.
  --output-filename [OUTPUT_FILENAME], -F [OUTPUT_FILENAME]
                        Custom output report name without the file extension, if not specified will use default output/prowler-output-ACCOUNT_NUM-
                        OUTPUT_DATE.format
  --output-directory [OUTPUT_DIRECTORY], -o [OUTPUT_DIRECTORY]
                        Custom output directory, by default the folder where Prowler is stored
  --verbose             Runs showing all checks executed and results
  --ignore-exit-code-3, -z
                        Failed checks do not trigger exit code 3
  --no-banner, -b       Hide Prowler banner
  --unix-timestamp      Set the output timestamp format as unix timestamps instead of iso format timestamps (default mode).

Logging:
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Select Log Level
  --log-file [LOG_FILE]
                        Set log file name
  --only-logs           Print only Prowler logs by the stdout. This option sets --no-banner.

Specify checks/services to run:
  --severity {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...], --severities {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...]
                        Severities to be executed ['critical', 'high', 'medium', 'low', 'informational']
  --checks-folder [CHECKS_FOLDER], -x [CHECKS_FOLDER]
                        Specify external directory with custom checks (each check must have a folder with the required files, see more in
                        https://docs.prowler.cloud/en/latest/tutorials/misc/#custom-checks).

Exclude checks/services to run:
  --excluded-check EXCLUDED_CHECK [EXCLUDED_CHECK ...], --excluded-checks EXCLUDED_CHECK [EXCLUDED_CHECK ...], -e EXCLUDED_CHECK [EXCLUDED_CHECK ...]
                        Checks to exclude
  --excluded-service EXCLUDED_SERVICE [EXCLUDED_SERVICE ...], --excluded-services EXCLUDED_SERVICE [EXCLUDED_SERVICE ...]
                        Services to exclude

Mutelist:
  --mutelist-file [MUTELIST_FILE], -w [MUTELIST_FILE]
                        Path for mutelist YAML file. See example prowler/config/<provider>_mutelist.yaml for reference and format. For AWS
                        provider, it also accepts AWS DynamoDB Table, Lambda ARNs or S3 URIs, see more in
                        https://docs.prowler.cloud/en/latest/tutorials/mutelist/

Configuration:
  --config-file [CONFIG_FILE]
                        Set configuration file path
  --fixer-config [FIXER_CONFIG]
                        Set configuration fixer file path

Custom Checks Metadata:
  --custom-checks-metadata-file [CUSTOM_CHECKS_METADATA_FILE]
                        Path for the custom checks metadata YAML file. See example prowler/config/custom_checks_metadata_example.yaml for
                        reference and format. See more in https://docs.prowler.cloud/en/latest/tutorials/custom-checks-metadata/

3rd Party Integrations:
  --shodan [SHODAN_API_KEY], -N [SHODAN_API_KEY]
                        Check if any public IPs in your Cloud environments are exposed in Shodan.
  --slack               Send a summary of the execution with a Slack APP in your channel. Environment variables SLACK_API_TOKEN and
                        SLACK_CHANNEL_NAME are required (see more in https://docs.prowler.cloud/en/latest/tutorials/integrations/#slack).

Authentication Modes:
  --profile [PROFILE], -p [PROFILE]
                        AWS profile to launch prowler with
  --role [ROLE], -R [ROLE]
                        ARN of the role to be assumed
  --role-session-name [ROLE_SESSION_NAME]
                        An identifier for the assumed role session. Defaults to ProwlerAssessmentSession
  --mfa                 IAM entity enforces MFA so you need to input the MFA ARN and the TOTP
  --session-duration [SESSION_DURATION], -T [SESSION_DURATION]
                        Assumed role session duration in seconds, must be between 900 and 43200. Default: 3600
  --external-id [EXTERNAL_ID], -I [EXTERNAL_ID]
                        External ID to be passed when assuming role

AWS Regions:
  --region {us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} [{us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} ...], --filter-region {us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} [{us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} ...], -f {us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} [{us-east-1,eu-south-1,ap-south-2,cn-northwest-1,eu-central-2,ap-east-1,eu-north-1,eu-central-1,ap-southeast-1,us-east-2,sa-east-1,us-west-2,ap-northeast-3,ca-west-1,eu-south-2,ca-central-1,il-central-1,eu-west-3,us-gov-west-1,ap-northeast-2,me-central-1,ap-northeast-1,us-gov-east-1,eu-west-2,af-south-1,cn-north-1,us-west-1,ap-southeast-2,ap-southeast-4,eu-west-1,me-south-1,ap-southeast-3,ap-southeast-5,ap-south-1} ...]
                        AWS region names to run Prowler against

AWS Organizations:
  --organizations-role [ORGANIZATIONS_ROLE], -O [ORGANIZATIONS_ROLE]
                        Specify AWS Organizations management role ARN to be assumed, to get Organization metadata

AWS Security Hub:
  --security-hub, -S    Send check output to AWS Security Hub and save json-asff outuput.
  --skip-sh-update      Skip updating previous findings of Prowler in Security Hub
  --send-sh-only-fails  Send only Prowler failed findings to SecurityHub

Quick Inventory:
  --quick-inventory, -i
                        Run Prowler Quick Inventory. The inventory will be stored in an output csv by default

AWS Outputs to S3:
  --output-bucket [OUTPUT_BUCKET], -B [OUTPUT_BUCKET]
                        Custom output bucket, requires -M <mode> and it can work also with -o flag.
  --output-bucket-no-assume [OUTPUT_BUCKET_NO_ASSUME], -D [OUTPUT_BUCKET_NO_ASSUME]
                        Same as -B but do not use the assumed role credentials to put objects to the bucket, instead uses the initial credentials.

AWS Based Scans:
  --resource-tag RESOURCE_TAG [RESOURCE_TAG ...], --resource-tags RESOURCE_TAG [RESOURCE_TAG ...]
                        Scan only resources with specific AWS Tags (Key=Value), e.g., Environment=dev Project=prowler
  --resource-arn RESOURCE_ARN [RESOURCE_ARN ...], --resource-arns RESOURCE_ARN [RESOURCE_ARN ...]
                        Scan only resources with specific AWS Resource ARNs, e.g., arn:aws:iam::012345678910:user/test arn:aws:ec2:us-
                        east-1:123456789012:vpc/vpc-12345678

Boto3 Config:
  --aws-retries-max-attempts [AWS_RETRIES_MAX_ATTEMPTS]
                        Set the maximum attemps for the Boto3 standard retrier config (Default: 3)

Scan Unused Services:
  --scan-unused-services
                        Scan unused services

Prowler Fixer:
  --fixer               Fix the failed findings that can be fixed by Prowler
```



### Azure help command output.


```
usage: prowler [-h] [--version] {aws,azure,gcp,kubernetes,dashboard} ... azure [-h]
                                                                               [--status {PASS,FAIL,MANUAL} [{PASS,FAIL,MANUAL} ...]]
                                                                               [--output-formats {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...]]
                                                                               [--output-filename [OUTPUT_FILENAME]]
                                                                               [--output-directory [OUTPUT_DIRECTORY]]
                                                                               [--verbose] [--ignore-exit-code-3]
                                                                               [--no-banner] [--unix-timestamp]
                                                                               [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                                                                               [--log-file [LOG_FILE]] [--only-logs]
                                                                               [--check CHECK [CHECK ...]]
                                                                               [--checks-file [CHECKS_FILE]]
                                                                               [--service SERVICE [SERVICE ...]]
                                                                               [--severity {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...]]
                                                                               [--compliance {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]]
                                                                               [--category CATEGORY [CATEGORY ...]]
                                                                               [--checks-folder [CHECKS_FOLDER]]
                                                                               [--excluded-check EXCLUDED_CHECK [EXCLUDED_CHECK ...]]
                                                                               [--excluded-service EXCLUDED_SERVICE [EXCLUDED_SERVICE ...]]
                                                                               [--list-checks | --list-checks-json | --list-services | --list-compliance | --list-compliance-requirements {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                                                                               | --list-categories | --list-fixer]
                                                                               [--mutelist-file [MUTELIST_FILE]]
                                                                               [--config-file [CONFIG_FILE]]
                                                                               [--fixer-config [FIXER_CONFIG]]
                                                                               [--custom-checks-metadata-file [CUSTOM_CHECKS_METADATA_FILE]]
                                                                               [--shodan [SHODAN_API_KEY]] [--slack]
                                                                               [--az-cli-auth | --sp-env-auth | --browser-auth | --managed-identity-auth]
                                                                               [--subscription-id SUBSCRIPTION_ID [SUBSCRIPTION_ID ...]]
                                                                               [--tenant-id [TENANT_ID]]
                                                                               [--azure-region [AZURE_REGION]]

options:
  -h, --help            show this help message and exit
  --check CHECK [CHECK ...], --checks CHECK [CHECK ...], -c CHECK [CHECK ...]
                        List of checks to be executed.
  --checks-file [CHECKS_FILE], -C [CHECKS_FILE]
                        JSON file containing the checks to be executed. See config/checklist_example.json
  --service SERVICE [SERVICE ...], --services SERVICE [SERVICE ...], -s SERVICE [SERVICE ...]
                        List of services to be executed.
  --compliance {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                        Compliance Framework to check against for. The format should be the following:
                        framework_version_provider (e.g.: cis_3.0_aws)
  --category CATEGORY [CATEGORY ...], --categories CATEGORY [CATEGORY ...]
                        List of categories to be executed.
  --list-checks, -l     List checks
  --list-checks-json    Output a list of checks in json format to use with --checks-file option
  --list-services       List covered services by given provider
  --list-compliance, --list-compliances
                        List all available compliance frameworks
  --list-compliance-requirements {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                        List requirements and checks per compliance framework
  --list-categories     List the available check's categories
  --list-fixer, --list-fixers, --list-remediations
                        List fixers available for the provider
  --tenant-id [TENANT_ID]
                        Azure Tenant ID to be used with --browser-auth option

Outputs:
  --status {PASS,FAIL,MANUAL} [{PASS,FAIL,MANUAL} ...]
                        Filter by the status of the findings ['PASS', 'FAIL', 'MANUAL']
  --output-formats {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...], --output-modes {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...], -M {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...]
                        Output modes, by default csv and json-oscf are saved. When using AWS Security Hub integration,
                        json-asff output is also saved.
  --output-filename [OUTPUT_FILENAME], -F [OUTPUT_FILENAME]
                        Custom output report name without the file extension, if not specified will use default
                        output/prowler-output-ACCOUNT_NUM-OUTPUT_DATE.format
  --output-directory [OUTPUT_DIRECTORY], -o [OUTPUT_DIRECTORY]
                        Custom output directory, by default the folder where Prowler is stored
  --verbose             Runs showing all checks executed and results
  --ignore-exit-code-3, -z
                        Failed checks do not trigger exit code 3
  --no-banner, -b       Hide Prowler banner
  --unix-timestamp      Set the output timestamp format as unix timestamps instead of iso format timestamps (default mode).

Logging:
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Select Log Level
  --log-file [LOG_FILE]
                        Set log file name
  --only-logs           Print only Prowler logs by the stdout. This option sets --no-banner.

Specify checks/services to run:
  --severity {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...], --severities {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...]
                        Severities to be executed ['critical', 'high', 'medium', 'low', 'informational']
  --checks-folder [CHECKS_FOLDER], -x [CHECKS_FOLDER]
                        Specify external directory with custom checks (each check must have a folder with the required
                        files, see more in https://docs.prowler.cloud/en/latest/tutorials/misc/#custom-checks).

Exclude checks/services to run:
  --excluded-check EXCLUDED_CHECK [EXCLUDED_CHECK ...], --excluded-checks EXCLUDED_CHECK [EXCLUDED_CHECK ...], -e EXCLUDED_CHECK [EXCLUDED_CHECK ...]
                        Checks to exclude
  --excluded-service EXCLUDED_SERVICE [EXCLUDED_SERVICE ...], --excluded-services EXCLUDED_SERVICE [EXCLUDED_SERVICE ...]
                        Services to exclude

Mutelist:
  --mutelist-file [MUTELIST_FILE], -w [MUTELIST_FILE]
                        Path for mutelist YAML file. See example prowler/config/<provider>_mutelist.yaml for reference and
                        format. For AWS provider, it also accepts AWS DynamoDB Table, Lambda ARNs or S3 URIs, see more in
                        https://docs.prowler.cloud/en/latest/tutorials/mutelist/

Configuration:
  --config-file [CONFIG_FILE]
                        Set configuration file path
  --fixer-config [FIXER_CONFIG]
                        Set configuration fixer file path

Custom Checks Metadata:
  --custom-checks-metadata-file [CUSTOM_CHECKS_METADATA_FILE]
                        Path for the custom checks metadata YAML file. See example
                        prowler/config/custom_checks_metadata_example.yaml for reference and format. See more in
                        https://docs.prowler.cloud/en/latest/tutorials/custom-checks-metadata/

3rd Party Integrations:
  --shodan [SHODAN_API_KEY], -N [SHODAN_API_KEY]
                        Check if any public IPs in your Cloud environments are exposed in Shodan.
  --slack               Send a summary of the execution with a Slack APP in your channel. Environment variables
                        SLACK_API_TOKEN and SLACK_CHANNEL_NAME are required (see more in
                        https://docs.prowler.cloud/en/latest/tutorials/integrations/#slack).

Authentication Modes:
  --az-cli-auth         Use Azure CLI credentials to log in against Azure
  --sp-env-auth         Use Service Principal environment variables authentication to log in against Azure
  --browser-auth        Use browser authentication to log in against Azure, --tenant-id is required for this option
  --managed-identity-auth
                        Use managed identity authentication to log in against Azure

Subscriptions:
  --subscription-id SUBSCRIPTION_ID [SUBSCRIPTION_ID ...], --subscription-ids SUBSCRIPTION_ID [SUBSCRIPTION_ID ...]
                        Azure Subscription IDs to be scanned by Prowler

Regions:
  --azure-region [AZURE_REGION]
                        Azure region from `az cloud list --output table`, by default AzureCloud
```


### GCP help command output.


```
usage: prowler [-h] [--version] {aws,azure,gcp,kubernetes,dashboard} ... gcp [-h] [--status {PASS,FAIL,MANUAL} [{PASS,FAIL,MANUAL} ...]]
                                                                             [--output-formats {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...]]
                                                                             [--output-filename [OUTPUT_FILENAME]] [--output-directory [OUTPUT_DIRECTORY]]
                                                                             [--verbose] [--ignore-exit-code-3] [--no-banner] [--unix-timestamp]
                                                                             [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--log-file [LOG_FILE]]
                                                                             [--only-logs] [--check CHECK [CHECK ...]] [--checks-file [CHECKS_FILE]]
                                                                             [--service SERVICE [SERVICE ...]]
                                                                             [--severity {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...]]
                                                                             [--compliance {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]]
                                                                             [--category CATEGORY [CATEGORY ...]] [--checks-folder [CHECKS_FOLDER]]
                                                                             [--excluded-check EXCLUDED_CHECK [EXCLUDED_CHECK ...]]
                                                                             [--excluded-service EXCLUDED_SERVICE [EXCLUDED_SERVICE ...]]
                                                                             [--list-checks | --list-checks-json | --list-services | --list-compliance | --list-compliance-requirements {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                                                                             | --list-categories | --list-fixer] [--mutelist-file [MUTELIST_FILE]]
                                                                             [--config-file [CONFIG_FILE]] [--fixer-config [FIXER_CONFIG]]
                                                                             [--custom-checks-metadata-file [CUSTOM_CHECKS_METADATA_FILE]]
                                                                             [--shodan [SHODAN_API_KEY]] [--slack] [--credentials-file [FILE_PATH] |
                                                                             --impersonate-service-account [SERVICE_ACCOUNT]]
                                                                             [--project-id PROJECT_ID [PROJECT_ID ...]]
                                                                             [--excluded-project-id EXCLUDED_PROJECT_ID [EXCLUDED_PROJECT_ID ...]]
                                                                             [--list-project-id]

options:
  -h, --help            show this help message and exit
  --check CHECK [CHECK ...], --checks CHECK [CHECK ...], -c CHECK [CHECK ...]
                        List of checks to be executed.
  --checks-file [CHECKS_FILE], -C [CHECKS_FILE]
                        JSON file containing the checks to be executed. See config/checklist_example.json
  --service SERVICE [SERVICE ...], --services SERVICE [SERVICE ...], -s SERVICE [SERVICE ...]
                        List of services to be executed.
  --compliance {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                        Compliance Framework to check against for. The format should be the following: framework_version_provider (e.g.: cis_3.0_aws)
  --category CATEGORY [CATEGORY ...], --categories CATEGORY [CATEGORY ...]
                        List of categories to be executed.
  --list-checks, -l     List checks
  --list-checks-json    Output a list of checks in json format to use with --checks-file option
  --list-services       List covered services by given provider
  --list-compliance, --list-compliances
                        List all available compliance frameworks
  --list-compliance-requirements {aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} [{aws_audit_manager_control_tower_guardrails_aws,soc2_aws,iso27001_2013_aws,fedramp_moderate_revision_4_aws,kisa_isms_p_2023_korean_aws,fedramp_low_revision_4_aws,rbi_cyber_security_framework_aws,nist_csf_1.1_aws,gxp_eu_annex_11_aws,gdpr_aws,ffiec_aws,cis_2.0_aws,cis_1.5_aws,cis_1.4_aws,aws_well_architected_framework_reliability_pillar_aws,nist_800_171_revision_2_aws,cis_3.0_aws,pci_3.2.1_aws,ens_rd2022_aws,nist_800_53_revision_5_aws,aws_well_architected_framework_security_pillar_aws,hipaa_aws,kisa_isms_p_2023_aws,aws_foundational_security_best_practices_aws,cisa_aws,aws_foundational_technical_review_aws,nist_800_53_revision_4_aws,gxp_21_cfr_part_11_aws,mitre_attack_aws,aws_account_security_onboarding_aws,mitre_attack_gcp,cis_2.0_gcp,mitre_attack_azure,cis_2.0_azure,cis_2.1_azure,cis_1.8_kubernetes} ...]
                        List requirements and checks per compliance framework
  --list-categories     List the available check's categories
  --list-fixer, --list-fixers, --list-remediations
                        List fixers available for the provider

Outputs:
  --status {PASS,FAIL,MANUAL} [{PASS,FAIL,MANUAL} ...]
                        Filter by the status of the findings ['PASS', 'FAIL', 'MANUAL']
  --output-formats {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...], --output-modes {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...], -M {csv,json-asff,json-ocsf,html} [{csv,json-asff,json-ocsf,html} ...]
                        Output modes, by default csv and json-oscf are saved. When using AWS Security Hub integration, json-asff output is also saved.
  --output-filename [OUTPUT_FILENAME], -F [OUTPUT_FILENAME]
                        Custom output report name without the file extension, if not specified will use default output/prowler-output-ACCOUNT_NUM-
                        OUTPUT_DATE.format
  --output-directory [OUTPUT_DIRECTORY], -o [OUTPUT_DIRECTORY]
                        Custom output directory, by default the folder where Prowler is stored
  --verbose             Runs showing all checks executed and results
  --ignore-exit-code-3, -z
                        Failed checks do not trigger exit code 3
  --no-banner, -b       Hide Prowler banner
  --unix-timestamp      Set the output timestamp format as unix timestamps instead of iso format timestamps (default mode).

Logging:
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Select Log Level
  --log-file [LOG_FILE]
                        Set log file name
  --only-logs           Print only Prowler logs by the stdout. This option sets --no-banner.

Specify checks/services to run:
  --severity {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...], --severities {critical,high,medium,low,informational} [{critical,high,medium,low,informational} ...]
                        Severities to be executed ['critical', 'high', 'medium', 'low', 'informational']
  --checks-folder [CHECKS_FOLDER], -x [CHECKS_FOLDER]
                        Specify external directory with custom checks (each check must have a folder with the required files, see more in
                        https://docs.prowler.cloud/en/latest/tutorials/misc/#custom-checks).

Exclude checks/services to run:
  --excluded-check EXCLUDED_CHECK [EXCLUDED_CHECK ...], --excluded-checks EXCLUDED_CHECK [EXCLUDED_CHECK ...], -e EXCLUDED_CHECK [EXCLUDED_CHECK ...]
                        Checks to exclude
  --excluded-service EXCLUDED_SERVICE [EXCLUDED_SERVICE ...], --excluded-services EXCLUDED_SERVICE [EXCLUDED_SERVICE ...]
                        Services to exclude

Mutelist:
  --mutelist-file [MUTELIST_FILE], -w [MUTELIST_FILE]
                        Path for mutelist YAML file. See example prowler/config/<provider>_mutelist.yaml for reference and format. For AWS provider, it also
                        accepts AWS DynamoDB Table, Lambda ARNs or S3 URIs, see more in https://docs.prowler.cloud/en/latest/tutorials/mutelist/

Configuration:
  --config-file [CONFIG_FILE]
                        Set configuration file path
  --fixer-config [FIXER_CONFIG]
                        Set configuration fixer file path

Custom Checks Metadata:
  --custom-checks-metadata-file [CUSTOM_CHECKS_METADATA_FILE]
                        Path for the custom checks metadata YAML file. See example prowler/config/custom_checks_metadata_example.yaml for reference and format. See
                        more in https://docs.prowler.cloud/en/latest/tutorials/custom-checks-metadata/

3rd Party Integrations:
  --shodan [SHODAN_API_KEY], -N [SHODAN_API_KEY]
                        Check if any public IPs in your Cloud environments are exposed in Shodan.
  --slack               Send a summary of the execution with a Slack APP in your channel. Environment variables SLACK_API_TOKEN and SLACK_CHANNEL_NAME are required
                        (see more in https://docs.prowler.cloud/en/latest/tutorials/integrations/#slack).

Authentication Modes:
  --credentials-file [FILE_PATH]
                        Authenticate using a Google Service Account Application Credentials JSON file
  --impersonate-service-account [SERVICE_ACCOUNT]
                        Impersonate a Google Service Account

Projects:
  --project-id PROJECT_ID [PROJECT_ID ...], --project-ids PROJECT_ID [PROJECT_ID ...]
                        GCP Project IDs to be scanned by Prowler
  --excluded-project-id EXCLUDED_PROJECT_ID [EXCLUDED_PROJECT_ID ...], --excluded-project-ids EXCLUDED_PROJECT_ID [EXCLUDED_PROJECT_ID ...]
                        Excluded GCP Project IDs to be scanned by Prowler
  --list-project-id, --list-project-ids
                        List available project IDs in Google Cloud which can be scanned by Prowler
```