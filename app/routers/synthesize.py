from typing import List
from fastapi import APIRouter, status, HTTPException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from ibm_watson import TextToSpeechV1
from ..config import settings
from .. import schemas

router = APIRouter(
    prefix='/synthesize',
    tags=['Synthesize']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_synthesize(to_speech: schemas.TextToSpeech):
    try:
        # Invoke a method
        authenticator = IAMAuthenticator(settings.api_key_text_speech)
        text_to_speech = TextToSpeechV1(authenticator=authenticator)

        text_to_speech.set_default_headers(
            {'x-watson-learning-opt-out': "true"})

        # Add the text to speech service to the service
        text_to_speech.set_service_url(settings.url_instance_text_speech)

        data = to_speech.dict()
        title_file = data["title_file"]
        path = f"public/mp3/{title_file}"

        with open(path, 'wb') as audio_file:
            audio_file.write(text_to_speech.synthesize(
                text=data["text"],
                voice=data["voice"],
                accept="audio/mp3").get_result().content)
            return {"message": f"{audio_file.name} created"}

    except ApiException as ex:
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error: " + ex.message)


@router.post('/bytes', status_code=status.HTTP_201_CREATED)
def create_synthesize_to_bytes(to_speech: schemas.TextToSpeech):
    try:
        # Invoke a method
        authenticator = IAMAuthenticator(settings.api_key_text_speech)
        text_to_speech = TextToSpeechV1(authenticator=authenticator)

        text_to_speech.set_default_headers(
            {'x-watson-learning-opt-out': "true"})

        # Add the text to speech service to the service
        text_to_speech.set_service_url(settings.url_instance_text_speech)

        data = to_speech.dict()
        title_file = data["title_file"]
        path = f"public/mp3/{title_file}"

        with open(path, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(text=data["text"],
                                          voice=data["voice"],
                                          accept="audio/mp3").get_result().content)

        # convertir le fichier mp3 en tableau de bytes
        with open(path, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            return {"bytes": f"{audio_bytes}"}

    except ApiException as ex:
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error: " + ex.message)


@router.get('/voices', status_code=status.HTTP_200_OK, response_model=List[schemas.Voices])
def get_voices():
    try:
        authenticator = IAMAuthenticator(settings.api_key_text_speech)
        text_to_speech = TextToSpeechV1(authenticator=authenticator)

        text_to_speech.set_default_headers(
            {'x-watson-learning-opt-out': "true"})

        # Add the text to speech service to the service
        text_to_speech.set_service_url(settings.url_instance_text_speech)
        # Liste de voix disponibles
        voices = text_to_speech.list_voices().get_result()

        voices_list = []

        for voice in voices["voices"]:
            # Récupèrer le propriété "gender", "name" et "url"
            response = {
                "gender": voice['gender'],
                "name": voice['name'],
                "url": voice['url']
            }

            # ajouter response dans la liste voices_list
            voices_list.append(response)

        return voices_list

    except ApiException as ex:
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Error: " + ex.message)
