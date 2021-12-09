# KoGPT (Korean Generative Pre-trained Transformer)

This project generate korean using KakaoBrain's KoGPT model.

Github : [KakaoBrain KoGPT](https://github.com/kakaobrain/kogpt)  
Open API : [On Ainize](https://ainize.ai/scy6500/kogpt-kakaobrain?branch=main)  
License : [CC-BY-NC-ND 4.0](https://github.com/kakaobrain/kogpt/blob/main/LICENSE.cc-by-nc-nd-4.0)

### Post parameter

    text: Korean
    length: The length of text


### Output format

    {"result": "..."}


## * With CLI *

### Input example


    curl -X POST "https://main-kogpt-kakaobrain-scy6500.endpoint.ainize.ai/generate" \
    -H "accept: application/json" -H "Content-Type: multipart/form-data" \
    -F "text=비트코인은 오를까요?" -F "length=100"
    

### Output example


    {
      "result": "비트코인은 오를까요? 떨어질까요? 비트코인에 대한 이야기를 할 때면 항상 궁금해집니다. \ 
      그런데 비트코인은 왜 올랐을까요? 왜 떨어질까요? 그래서 저는 이런 질문을 해보죠. 비트코인 가격을 결정하는 원인이 무엇인가?, \ 
      비트코인이 오르는 이유는 무엇인가? 그리고 이번에는 이렇게 생각해봅니다. 그럼 비트코인이 내리는 이유는? \ 
      비트코인 가격과 비트코인 전망에 대해 궁금하시다면."
    }


## * With swagger *

API page: [Ainize](https://ainize.ai/scy6500/kogpt-kakaobrain?branch=main)

## * With a Demo *

Demo page: [End-point](https://main-kogpt-kakaobrain-scy6500.endpoint.ainize.ai/)
