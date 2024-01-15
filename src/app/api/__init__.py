from os import makedirs, path
from fastapi import APIRouter, Request, Depends
from app.schema import UploadForm
from app.marker import water_mark_docx

api = APIRouter(prefix="/api")
UPLOADS = "uploads"

@api.post("/upload")
async def upload_file(request: Request, data: UploadForm = Depends()):

    directory = data.document.filename.split(".")[0]
    file_folder_path = f"{UPLOADS}/{directory}"

    makedirs(file_folder_path, exist_ok=True)
    file_path = path.join(file_folder_path, data.document.filename)

    with open(file_path, "wb") as f:
        f.write(data.document.file.read())

    water_mark_docx(file_folder_path, data.document.filename, data.wm_text)


    return {"file": "name"}


