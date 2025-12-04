[![Build Status](https://v3.travis-ci.com/DRAutomation/dra-python-sdk.svg?token=Z799xXryYYPor3yyJxEs&branch=main)](https://v3.travis.ibm.com/DRAutomation/dra-python-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
# IBM Cloud DrAutomation Python SDK

Python client library to interact with various [IBM Cloud DrAutomation services APIs](https://cloud.ibm.com/docs/dr-automation-powervs).

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
  * [Environment Configuration](#environment-configuration)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud DrAutomation services Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Module Name | Imported Class Name
--- | ---| ---
[DrAutomation Service](https://test.cloud.ibm.com/apidocs/dr-automation-powervs) | dra_python_sdk.dr_automation_service_v1 | DrAutomationServiceV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.9 or above.

## Installation

To install, use `pip`:

```bash
python -m pip install --upgrade dra_python_sdk
```

Then in your code, you can import the appropriate service like this:
```
from dra_python_sdk.dr_automation_service_v1 import *
```
where `dr_automation_service_v1` is the service's module name from the table above

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

### Environment Configuration

The SDK can be configured using environment variables. Here's an example configuration:

```bash
# Service URL (for development/testing)
export DR_AUTOMATION_SERVICE_URL=https://power-dra.cloud.ibm.com

# Authentication type
export DR_AUTOMATION_SERVICE_AUTH_TYPE=bearerToken

# Bearer token for authentication
export DR_AUTOMATION_SERVICE_BEARER_TOKEN=eyJraWQiOiIyMDE5MD......
```

**Note:** The bearer token shown above is an example. For production use:
- Use the actual service endpoint URL 
- Generate your own valid IAM bearer token

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/dra-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.com/IBM/dra-python-sdk/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.com/IBM/dra-python-sdk/LICENSE).

#
