import os
import sys
import openai

question       = ' '.join(sys.argv[1:])

openai.api_key = os.getenv("OPENAI_API_KEY")

resp = openai.Completion.create(
  model             = "text-davinci-002",
  prompt            = question + '?',
  temperature       =   0,
  max_tokens        = 100,
  top_p             =   1,
  frequency_penalty = 0.0,
  presence_penalty  = 0.0,
  stop              =["?"]
)

print(resp["choices"][0]["text"])
