from typing import List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware


class QuestionData(BaseModel):
    question: str
    image: HttpUrl
    answer: str


class ResponseData(BaseModel):
    data: Dict[str, List[QuestionData]]


app = FastAPI()


origins = [
    "http://localhost:8000",
    "https://nfactorial-hackathon-1.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/questions/{category}")
async def get_questions(category: str):
    questions_data = {
        "timeline": [
            {
                "question": "кто ты, юный падаван: iOS или fullstack",
                "image": "https://drive.google.com/file/d/1Jf6zcJUKKuum7_FBRctslKYOlw3H0Am5/view?usp=drive_link",
                "answer": "yes"
            },
            {
                "question": "твой любимый ментор?",
                "image": "https://drive.google.com/file/d/1Jf6zcJUKKuum7_FBRctslKYOlw3H0Am5/view?usp=drive_link",
                "answer": "optional"
            },
        ],
        "random": [
            {
                "question": "Спал на лекции? 🤔",
                "image": "https://drive.google.com/file/d/1h_hg0D8vxNd23iWSqXayIp2OaGPOfXAo/view?usp=drive_link",
                "answer": "noR"
            },
            {
                "question": "вжжж... на вас напал клоп!",
                "image": "https://drive.google.com/file/d/1u5jDh-iy_uhyJaaUwAgu-kdPqgcBWlk3/view?usp=drive_link",
                "answer": "yesR"
            },
            {
                "question": "кто из них Оссейн?",
                "image": "https://drive.google.com/file/d/1zQyI0yZFKhKivmKd8NS_u9xU5IGd50KF/view?usp=drive_link",
                "answer": "yesR"
            }
        ]
    }
    category_data = questions_data.get(category)
    return {category: category_data}
