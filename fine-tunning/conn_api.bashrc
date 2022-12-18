set OPENAI_API_KEY=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

openai api fine_tunes.create -t train-data_prepared.jsonl -m davinci

openai api completions.create -m davinci:ft-liid-utpl-2022-12-17-13-35-30 -p "PROMPT"



