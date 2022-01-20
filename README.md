## API - LANGUAGE TRADUCTOR

* To start the app
    - pip install -r requirements.txt
    - uvicorn app.main:app --reload

* But first, you need to create an [IBM Cloud](https://myibm.ibm.com/) account
* create a file at the root of the project which will be called ```.env```
* Replace these values with your IBM Cloud account, I am using version ```2019-04-04```

![image](https://user-images.githubusercontent.com/70981701/150094367-a9551a20-9619-46c7-ad66-4cab778d6e6e.png)
```
    API_KEY=YOUR-API-KEY
    URL_INSTANCE=YOUR-URL
    version=YOUR-VERSION
    API_KEY_TEXT_SPEECH=YOUR-URL-TEXT-SPEECH
    URL_INSTANCE_TEXT_SPEECH=YOUR-URL-TEXT-SPEECH
```
* Running project : ```http://127.0.0.1:8000```
* Access the docs : ```http://127.0.0.1:8000/docs```

* Example :
    - POST Method:
    ```
    {
        "text" : "Je m'appelle Josue Lubaki, j'aime le éveloppement mobile, API et d'application Web",
        "model_id":"fr-en"
    }
    ```
    - Response :
    ```
    {
        "translation": "My name is Josue Lubaki, I love mobile development, API and web application"
    }
    ```
