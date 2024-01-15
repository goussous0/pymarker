from pydantic import BaseModel
from fastapi import Form, UploadFile, File
from dataclasses import dataclass

@dataclass
class UploadForm:
    wm_text: str = Form(...)
    document: UploadFile = File(...) 

