# AI Model Management Platform

## What this project does
This project is a small Python app that helps a person choose an AI model and estimate how much it might cost to use.

Think of it like a menu at a restaurant:
- You pick a model (like GPT, Claude, or Gemini)
- You choose how many "tokens" you want to use
- The app calculates the estimated cost
- It shows the result in a friendly format

This is a beginner-friendly example of how software can manage AI tools, pricing, and simple user input.

## Why this is useful
AI tools are not all the same. Some are cheaper, some are more expensive, and some are built by different companies.

This app lets you:
- see the available models
- compare providers
- estimate cost before sending a request
- learn how a small app can manage AI services

## How it works (in simple words)
When you run the program:
1. It prints the app name
2. It lists the available AI models
3. It asks you to choose one
4. It asks how many tokens you want to use
5. It calculates the estimated cost
6. It prints the result

A token is like a small chunk of text. AI models read and write in tokens, so the more text, the more work the model does.

## Project files and what they do

### main.py
This is the main script that starts the app.

It does things like:
- show the app title
- create a ModelManager object
- list the models
- ask the user for input
- show the result

### model_manager.py
This file is the brain of the app.

It:
- loads all the models from the config
- stores them in a dictionary
- lets us list available models
- finds the model the user picked
- calculates the estimated cost
- returns the result to the user

### models.py
This file defines an AIModel class.

A class is like a blueprint. It says:
- each model has a name
- each model has a provider
- each model has a price
- each model can calculate its cost

The cost is calculated with a simple formula:

price = (tokens / 1000) * model_price

So if a model costs $0.002 per 1000 tokens and you use 500 tokens:
- 500 / 1000 = 0.5
- 0.5 * 0.002 = 0.001

That means the estimated cost is $0.001.

### config.py
This file holds the configuration data.

It contains:
- the app name
- the list of AI models
- each provider name
- the price per 1000 tokens

### logger.py
This file helps the app keep track of what happens.

It creates logs in a folder called `logs`.

Logs are like a diary for the software. They help developers check:
- if something worked
- if there was an error
- what happened during a request

## A simple code walkthrough
Here is the most important part of the app:

```python
manager = ModelManager()

for model in manager.list_models():
    print("-", model)
```

This means:
- create a ModelManager
- ask it to list all models
- print each one on the screen

Then the app asks the user to choose a model:

```python
model_name = input("\nSelect model: ")
```

This is a way for the app to get input from the user.

Then it does:

```python
response = manager.process_request(model_name, tokens)
```

This tells the app to do the work:
- find the selected model
- calculate the cost
- prepare a result dictionary

## Example output
```text
=============================================
AI Model Management Platform
=============================================

Available Models:
- gpt
- claude
- gemini

Select model: gpt
Enter token count: 500

Request Result
------------------------------
model: gpt
provider: OpenAI
tokens: 500
estimated_cost: 0.001
status: success
```

## How to run it
Make sure you are in the project folder, then run:

```bash
python main.py
```

If you are using Python 3, you may need:

```bash
python3 main.py
```

## What a 15-year-old should take away
This project is a tiny example of how real software can:
- manage AI services
- compare options
- calculate prices
- use basic Python programming

It is not a huge AI system, but it shows the idea behind bigger apps used in the real world.

## Small coding lesson
You can think of the code like this:
- variables store information
- functions do jobs
- classes create a template for objects
- loops repeat actions
- input lets the user talk to the program
- output shows the result

That is the basic building blocks of many programs.

## Final idea
This app is a simple beginner project that teaches how to build an AI-related tool using Python. It is a great starting point for learning:
- Python
- classes and objects
- user input
- calculations
- logging
- AI model management

If you can understand this project, you are already learning the same ideas used in many real software tools.
