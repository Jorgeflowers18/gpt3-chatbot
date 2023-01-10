set OPENAI_API_KEY=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
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 002

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 003
openai api fine_tunes.create -t train-data_prepared.jsonl -m davinci

openai api completions.create -m davinci:ft-liid-utpl-2022-12-17-13-35-30 -p "PROMPT"



