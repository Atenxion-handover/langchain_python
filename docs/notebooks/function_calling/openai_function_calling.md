# `function_calling/openai_function_calling.ipynb`

Notebook: `function_calling/openai_function_calling.ipynb`

## What it does

Shows the “raw” tool/function calling loop using the OpenAI Python client:

1. Define a function schema the model can call.
2. Send a prompt to the model and receive tool calls.
3. Execute the called function(s) in Python.
4. Append tool results to the message list.
5. Re-invoke the model to produce a final answer grounded in the tool outputs.

## Workflow (step-by-step)

1. **Import necessary modules**
   - Imports the OpenAI client and loads keys via `helpers.config.Config`.
2. **Initiate Open AI Client**
   - Creates an `OpenAI(...)` client instance.
3. **Define Function Schema**
   - Defines the JSON schema for the function call signature (name + parameters).
4. **Define Function**
   - Implements the actual Python function that will be called.
5. **Prepare Prompt Template**
   - Assembles the messages sent to the model.
6. **Get Tool Response**
   - Calls the model to get a response that may include tool calls.
7. **Invoke Function Calls and Append Tool Response To Messages**
   - Executes tool calls, then appends results into the message list as tool messages.
8. **Inovke LLM using Tool Response**
   - Calls the model again using the augmented messages to get the final natural-language answer.

## Notes

- Requires `OPENAI_API_KEY`.

