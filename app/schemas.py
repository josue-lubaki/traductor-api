from pydantic import BaseModel

"""
    {
        "text" : "This is a test",
        "model_id" : "en-fr"
    }
"""


class PostTranslate(BaseModel):
    text: str
    model_id: str


"""
    {
        "translation": "C'est un test"
    }
"""


class TranslateResponse(BaseModel):
    translation: str


class TextToSpeech(BaseModel):
    text: str
    voice: str
    title_file: str


class Voices(BaseModel):
    gender: str
    name: str
    url: str

    class Config:
        orm_mode = True
