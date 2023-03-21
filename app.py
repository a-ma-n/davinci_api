from flask import Flask,request
import openai

def get_result(key,input_prompt):
  openai.api_key=key
  response = openai.Completion.create(model="text-davinci-003", prompt=input_prompt, temperature=0, max_tokens=60)
  return response['choices'][0]['text'] 

app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
  key=request.json["key"]
  prompt=request.json["prompt"]
  return get_result(key,prompt)
 
if __name__=="__main__":
    app.run(debug=True,port="7910")
