# davinci_api
flask api to get responses from the davinci model, use a get request over here
### Url: 
```
https://openai-davinci-app.azurewebsites.net/
```
### Json body should look like this
```
{
  "key":<open-api-key>,
  "prompt":"this is a test"
}
```
I am not using or storing any passed api keys, no data is getting stored just directly coming from the azure app service.
