import time 
from queue import Queue, Empty
from threading import Thread
import torch
import json
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

print("model loading...")

# Model & Tokenizer loading
tokenizer = AutoTokenizer.from_pretrained('./KoGPT6B-ryan1.5b-float16')
model = AutoModelForCausalLM.from_pretrained(
'./KoGPT6B-ryan1.5b-float16', torch_dtype='auto', low_cpu_mem_usage=True
)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

requests_queue = Queue()    # request queue.
BATCH_SIZE = 4              # max request size.
CHECK_INTERVAL = 0.1

print("complete model loading")


def handle_requests_by_batch():
    while True:
        request_batch = []

        while not (len(request_batch) >= BATCH_SIZE):
            try:
                request_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
            except Empty:
                continue

            for requests in request_batch:
                try:
                    requests["output"] = make_text(requests['input'][0], requests['input'][1])

                except Exception as e:
                    requests["output"] = e


handler = Thread(target=handle_requests_by_batch).start()


def make_text(text, length):
    try:
	result = dict()
	tokens = tokenizer.encode(text, return_tensors='pt').to(device=device, non_blocking=True)
  	gen_tokens = model.generate(tokens, do_sample=True, temperature=0.8, max_length=length)
  	generated = tokenizer.batch_decode(gen_tokens)[0]
	result['result'] = generated

        return result

    except Exception as e:
        print('Error occur in script generating!', e)
        return jsonify({'Error': e}), 500


@app.route('/generate', methods=['POST'])
def generate():

    if requests_queue.qsize() > BATCH_SIZE:
        return jsonify({'Error': 'Too Many Requests. Please try again later'}), 429

    try:
        args = []
        text = request.form['text']
        length = int(request.form.get('length', 100))

        args.append(text)
        args.append(length)

    except Exception as e:
        return jsonify({'Error': 'Invalid request'}), 500

    req = {'input': args}
    requests_queue.put(req)

    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)

    return json.dumps(req['output'], ensure_ascii=False)


@app.route('/healthz', methods=["GET"])
def health_check():
    return "Health", 200


@app.route('/')
def main():
    return render_template('main.html'), 200


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
