# Betsson Group Customer Service Automation

## Index

1. [Introduction](#introduction)
2. [Required Tools](#required-tools)
3. [Getting Started](#getting-started)
4. [Execution and Outputs](#execution-and-outputs)
   - 4.1 [Execution](#execution)
   - 4.2 [Outputs](#outputs)
   - 4.3 [Logs](#outputs)

## Introduction

Some introductions...

## Required Tools

| #   | Tool                                                                                                              | Version | Description                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------- |
| 1   | [UI Path](https://docs.uipath.com/studio/standalone/2022.10/user-guide/install-studio)                            | LTS     |                                                                                                                         |
| 2   | [Python](https://www.python.org/downloads/release/python-31011/)                                                  | 3.10.11 |                                                                                                                         |
| 3   | [pip](https://pip.pypa.io/en/stable/installation/)                                                                | 24.3.1  |                                                                                                                         |
| 4   | GSuite                                                                                                            |         | You can follow the guide [here](https://support.google.com/cloud/answer/6158849?hl=en) to setup your OAuth credentials. |
| 5   | [.NET](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-5.0.17-windows-x64-installer) | 5.0.17  |                                                                                                                         |
| 6   | Miscrosoft Power BI                                                                                               |         | You can download it from [here](https://www.microsoft.com/en-us/download/details.aspx?id=58494).                        |
| 7   | OpenAI API                                                                                                        |         | Create an account on OpenAI and get your API key. [Guide](https://platform.openai.com/api-keys)                         |

## Getting Started

1. Clone this repository to you desired path.

   ```shell
   git clone http://github.com/sai-ka-land/nahi-kahada-hota.git
   ```

2. Install python dependencies.

   ```shell
   pip install -r requirements.txt
   ```

3. Install required packages for UI Path.

   - Open Project main.xaml in UI Path Studio.
   - Go to `Manage Packages > All Packages`.
   - Search for required packages and check for correct version.

   | Package Name                   | Version         |
   | ------------------------------ | --------------- |
   | UiPath.Excel.Activities        | 2.25.1-preview  |
   | UiPath.GSuite.Activities       | 2.8.23          |
   | UiPath.Mail.Activities         | 1.24.12         |
   | UiPath.Python.Activities       | 1.6.0           |
   | UiPath.System.Activities       | 24.10.7         |
   | UiPath.UIAutomation.Activities | 24.12.4-preview |

4. Update the `./Data/config.xlsx` file and ensure to replace following keys.

   | Key               | Value                                          |
   | ----------------- | ---------------------------------------------- |
   | OpenaiAPI         | <OPEN_AI_API_KEY>                              |
   | GmailClientID     | <GOOGLE_CLIENT_ID>                             |
   | GmailClientSecret | <GOOGLE_CLIENT_SECRET>                         |
   | PythonLibrary     | C:\path\to\your\python\python310\python310.dll |
   | PythonAppPath     | C:\path\to\your\python\python310               |

   > Other keys are preconfigured and no need to update them.

## Execution and Outputs

### Execution

1. Open `main.xaml` in UIPath Studio.
2. Go To `Design` tab and click on `Run` button.
3. Wait until the automation process is completed.

### Outputs

| Output Path                       | Description                                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| ./Data/CustomerData.xlsx          | Extracted Customer Data                                                                                              |
| ./Data/ValidatedCustomerData.xlsx | Validated Customer Data (email and name)                                                                             |
| ./Data/AICustomerData.xlsx        | AI generated subcategories for issues                                                                                |
| ./Data/Dashboard.pbix             | Data Visualization Dashboard (Specify absolute data source path in Power BI for `./Data/ValidatedCustomerData.xlsx`) |

### Logs

| Log Path                                                                 | Description                                                         |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| ./log/DataScrappingStatusLog.csv                                         | Event log for each event per customer.                              |
| ./log/ExecutionLog.txt                                                   | Custom runtime execution log for unknown excpetions in each module. |
| C:\Users\saikumarvadlani\AppData\Local\UiPath\Logs\<DATE\_>Execution.txt | Default Exicution logs for UI Path Studio.                          |
