# Ante Gen GPT Fine Tuning Steps

Install dependencies with pipenv

Prepare data by calling, it will instruct you to do some stuff, just follow them
```
openai tools fine_tunes.prepare_data -f data.csv
```
+
Upload file
```
openai api files.create -f data_openai_prepared.jsonl -p fine-tune
```

Fine tune model, get the file id from the previous step, we use davinci here which is GPT-3 based
```
openai api fine_tunes.create -t file-L.... -m davinci
```

The stream can get interrupted, to follow the fine tune call
```
openai api fine_tunes.follow -i ft-F....

# you will see something like this
[2023-06-07 21:47:53] Created fine-tune: ft-.....
[2023-06-07 21:49:16] Fine-tune costs $1.79
[2023-06-07 21:49:16] Fine-tune enqueued. Queue number: 6
[2023-06-07 21:52:50] Fine-tune is in the queue. Queue number: 5
[2023-06-07 21:53:55] Fine-tune is in the queue. Queue number: 4
[2023-06-07 21:54:55] Fine-tune is in the queue. Queue number: 3
```

You can get the list of fine-tunes at
```
openai api fine_tunes.list
```

Then with the the id you can create completions with

```
openai api completions.create -m <model_id> -p prompt
```

Alternatively, you can call `python completion.py` and edit your prompt within the file.

# Notes

You cannot give OpenAI super long training examples as there are token limits. If too many data points exceed token limits, OpenAI will throw errors
```
[2023-06-07 21:43:06] Error: The majority of examples in the training file contain more than the 2048 tokens allowed for this model.
```