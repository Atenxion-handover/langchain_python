# `function_calling/mistral_function_calling.ipynb`

Notebook: `function_calling/mistral_function_calling.ipynb`

## What it does

Shows the “raw” tool/function calling loop using the Mistral client:

1. Define a function schema the model can call.
2. Send a prompt to the model and receive tool calls.
3. Execute the called function(s) in Python.
4. Append tool results back into the message list.
5. Re-invoke the model to produce a final answer grounded in tool outputs.

## Workflow (step-by-step)

1. **Import necessary modules**
   - Imports `mistralai` client utilities and loads keys via `helpers.config.Config`.
2. **Initiate Mistral AI Client**
   - Creates a `Mistral(...)` client instance using `MISTRAL_API_KEY`.
3. **Define Function Schema**
   - Defines the tool/function schema exposed to the model.
4. **Define Function**
   - Implements the Python function called by the tool call.
5. **Define Name to Function Mapping**
   - Builds a mapping from tool name → Python callable for dispatch.
6. **Prepare Prompt Template**
   - Creates the message list the model will see.
7. **Get Tool Response**
   - Calls the model to get tool calls.
8. **Invoke Function Calls and Append Tool Response To Messages**
   - Executes tool calls and appends tool results back into messages.
9. **Inovke LLM using Tool Response**
   - Calls the model again to generate the final answer.

## Notes

- Requires `MISTRAL_API_KEY`.

