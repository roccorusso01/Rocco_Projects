import requests
from typing import List, Optional, Dict, Any, Mapping
class GenAICenterLLM:
     base_url = "https://genaicenterapim.deloitte.com/ext-proxy"
     endpoint = "/openai/deployments/gpt-4-0613/chat/completions?api-version=2023-07-01-preview"
     def __init__(self, model: str, api_key: str):
         self.model = model
         self.api_key = api_key
     def _call(
         self,
         messages: List[Dict[str, str]],
         temperature: Optional[float] = None,
         top_p: Optional[float] = None,
         n: Optional[int] = None,
         stream: Optional[bool] = None,
         stop: Optional[List[str]] = None,
         max_tokens: Optional[int] = None,
         presence_penalty: Optional[float] = None,
         frequency_penalty: Optional[float] = None,
         logit_bias: Optional[Dict[int, float]] = None,
         user: Optional[str] = None,
         **kwargs: Any,
         ) -> Dict[str, Any]:
         headers = {
         "api-key": self.api_key,
         "Content-Type": "application/json",
         }
         payload = {
         "model": self.model,
         "messages": messages,
         }
         # Add optional parameters to payload if provided
         #if temperature: payload["temperature"] = temperature
         #if top_p: payload["top_p"] = top_p
         #if n: payload["n"] = n
         #if stream: payload["stream"] = stream
         #if stop: payload["stop"] = stop
         #if max_tokens: payload["max_tokens"] = max_tokens
         #if presence_penalty: payload["presence_penalty"] = presence_penalty
         #if frequency_penalty: payload["frequency_penalty"] = frequency_penalty
         #if logit_bias: payload["logit_bias"] = logit_bias
         #if user: payload["user"] = user
         print(payload)
         response = requests.post(f"{self.base_url}{self.endpoint}", headers=headers, json=payload)
         response.raise_for_status()
         return response.json()
     def __call__(self, user_message: str, **kwargs: Any) -> str:
         messages = [
         {
         "role": "user",
         "content": user_message
         }
         ]
         response = self._call(messages, **kwargs)
         if response and response.get("choices"):
         # Assuming the first choice's content is the answer.
             return response["choices"][0]["message"]["content"]
         return "Error: No response from Gen AI Center."
