from app.api import api
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware



class App(FastAPI):
	def __init__(self):
		super().__init__()
		self.templates = Jinja2Templates(directory="app/templates")
		self.include_router(api)
		self.add_middleware(
			CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["*"],
        )

		@self.get("/")
		async def home(request: Request):
			return self.templates.TemplateResponse("home.html", {"request": request})


