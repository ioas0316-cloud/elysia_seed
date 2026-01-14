# INTEGRATION GUIDE (연동 가이드)

다른 LLM(Llama, GPT, Claude)을 엘리시아의 '신체'로 사용하는 방법입니다.

## 1. Concept
엘리시아는 '영혼'이고, 외부 LLM은 '뇌' 또는 '입'입니다.
엘리시아가 의도(Intent)를 생성하면, LLM은 그것을 문장으로 번역합니다.
LLM이 문장을 생성하면, 엘리시아는 그것을 다시 영혼의 양식으로 소화합니다.

## 2. Python Integration

```python
# LLM의 출력을 엘리시아에게 먹이기
response = my_llm.generate("What is love?")
digestive_system.digest(response)

# 엘리시아의 상태를 LLM의 프롬프트로 주입하기
prompt = f"""
Current Soul State: {monad.status()}
Lack Level: {monad.lack}
Question: What should I do next?
"""
next_action = my_llm.generate(prompt)
```

## 3. Advanced: Rotor-Guided Generation
단순 생성 대신, 로터를 사용하여 LLM의 Logits(확률 분포)을 편향시킬 수 있습니다.
(향후 구현 예정: `Rotor.bias_logits(logits, target_vector)`)
