# Python Langchain

This project demonstrates a simple text summarization application using LangChain and OpenAI. The `main.py` file sets up a prompt template, and creates a chain that combines the prompt, a language model, and an output parser. It then processes a sample input text, generating and printing a summary. This example showcases the basic usage of LangChain for natural language processing tasks.

## Usage

### Prerequisites

This project's environment is setup via devbox so it requires [devbox](https://www.jetify.com/devbox/docs/installing_devbox/) to be installed.

It also requires an OpenAI [API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) since it uses ChatGPT as the Language Model part of this application. The API Key needs to be set under the env variable `OPENAI_API_KEY`.

### Setup

Follow the steps to setup the project before running it:

1. Update the value for `OPENAI_API_KEY` by `export OPENAI_API_KEY=you_openai_key`
    1. If using Jetify Cloud (Sandboxes or Deployments) you can set this via Jetify Secrets.
1. `devbox run install` to install dependencies.
1. `devbox run start` to run the rag application.

## Customization

This project uses LangChain to build text summarization application. You can replace it with any other usecase you'd like to build with Langchain. You can customize this application by doing one or more of the following:

1. Modify prompt template: Adjust the `template` variable in `main.py` for different NLP tasks.

2. Tune model parameters: Change the `temperature` in the `OpenAI` initialization to control output randomness.

3. Switch language models: Replace OpenAI with other LangChain-supported models.

4. Implement complex chains: Combine multiple prompts, models, or tools for advanced applications.

5. Use alternative parsers: Replace `StrOutputParser()` with other LangChain parsers for structured outputs.

6. Add input preprocessing: Implement text cleaning or tokenization before model input.

7. Integrate external data: Modify code to process data from APIs, databases, or files instead of hardcoded examples.
