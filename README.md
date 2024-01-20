# RAG over code using langchain

## TODO

- [x] setup simple RAG in notebook (according to tutorial)
- [ ] potentially use chainlit to package it nicely?

## Sources

- https://python.langchain.com/docs/use_cases/code_understanding
- https://python.langchain.com/docs/integrations/llms/llamacpp
  - as LLM? local llamacpp is recommended by https://docs.privategpt.dev/installation
  - as model maybe code llama? see https://github.com/ggerganov/llama.cpp/issues/2766
- https://github.com/imartinez/privateGPT
  - all-in-one, but not sure
    - how performant
    - whether multiple documents can be added
    - how well suited for code (langchain uses a special splitter)

## Run llama.cpp directly (get ~28 t/s)

```bash
# code llama performed horribly!
export MODEL="/Users/cgebbe/git/_private/code_rag_application/codellama-7b.Q4_K_M.gguf"

# magicoder doesn't seem to be supported by cpp unfortunately :/
export MODEL="/Users/cgebbe/git/_private/code_rag_application/models/magicoder-s-ds-6.7b.Q4_K_M.gguf"

# deepseek coder performed already pretty nicely. Maybe similarly as GPT-3.5, not sure.
export MODEL="/Users/cgebbe/git/_private/code_rag_application/models/deepseek-coder-6.7b-instruct.Q4_K_M.gguf"


./main -m $MODEL --color --instruct
# taken from some github comment
./main -m $MODEL --color --instruct --temp 0.8 --top_k 40 --top_p 0.95 --ctx_size 2048 --n_predict -1 --keep -1 -i -r "USER:" -p "You are a helpful assistant. USER: prompt goes here ASSISTANT:"
```

## Run llama-cpp-python

https://llama-cpp-python.readthedocs.io/en/latest/install/macos/

```bash
python -m llama_cpp.server --model=$MODEL --n_gpu_layers=-1 --instruct
```

## Benchmark times

https://github.com/ggerganov/llama.cpp/discussions/4167

I currently get ~27 t/s eval time with my M1MaxPro

## Benchmark quality

- https://evalplus.github.io/leaderboard.html
