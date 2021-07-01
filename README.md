[日本語のREADME](README_ja.md)
# notion-fetch

## What is this?

This is a sample code to fetch (query) the database and get the page information contained in it by quering the API of [Notion](https://www.notion.so). It also includes sample code to write the retrieved page information to [Pixe.la](https://pixe.la/ja) and Slack.

It is intended to be used to record the frequency of page creation in Notion in Pixe.la.
It is designed to be run in the AWS Lambda environment, but it can also be run on your own machine (Mac).

## Usage

## Preparation
To use the Notion API, prepare the **Notion access token**, the target **database ID**, and the **user ID** if you want to filter pages by user ID, and set them in lines 6, 7, and 8 of the source code.

If you want to export to Pixe.la, prepare the **URL** of the target graph and **access token** of Pixe.la, and set them in lines 10 and 11 of the source code.

If you want to export to Slack, prepare the **Slack webhook URL** and **target channel**, and set them in lines 13 and 14.


### Actual usage
If you want to use it with AWS Lambda, comment out or uncomment the lambda_handler function from line 85.
In the version on git, Notion is accessed and the result is printed, so comment it out and enable line 90 or 91 instead.

If you want to use it on the command line, edit the lines from line 98 as you see fit.
