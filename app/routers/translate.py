from fastapi import APIRouter, HTTPException, status
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from ..config import settings
from .. import schemas

router = APIRouter(
    prefix='/translate',
    tags=['Translate']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.TranslateResponse)
def translate(data: schemas.PostTranslate):
    try:
        # Authenticate with IAM
        authenticator = IAMAuthenticator(settings.api_key)
        language_translator = LanguageTranslatorV3(
            version=settings.version,
            authenticator=authenticator
        )

        # Add the language translator service to the service
        language_translator.set_service_url(settings.url_instance)

        translation = language_translator.translate(**data.dict()).get_result()

        return translation["translations"][0]

    except ApiException as ex:
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error: " + ex.message)
