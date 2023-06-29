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
                "question": "Кто ты, юный падаван: iOS или fullstack",
                "image": "https://drive.google.com/file/d/1Jf6zcJUKKuum7_FBRctslKYOlw3H0Am5/view?usp=drive_link",
                "answer": "yes"
            },
            {
                "question": "Твой любимый ментор?",
                "image": "https://drive.google.com/file/d/1Jf6zcJUKKuum7_FBRctslKYOlw3H0Am5/view?usp=drive_link",
                "answer": "optional"
            },
            {
                "question": "Запитчил идею Арману?",
                "image": "https://drive.google.com/file/d/1cEErufIAhYnr7bx0Mof_qmmCRfZg1AYe/view?usp=drive_link",
                "answer": "yes"
            },
            {
                "question": "Запитчил идею Арману?",
                "image": "https://drive.google.com/file/d/1cEErufIAhYnr7bx0Mof_qmmCRfZg1AYe/view?usp=drive_link",
                "answer": "yes"
            },
            {
                "question": "шаришь за лангчейн? а за векторные базы данных? 🤔",
                "image": "https://drive.google.com/file/d/15uy5T45Jkb5aEdodNeCUHIwzu4qgv8ZD/view?usp=drive_link",
                "answer": "yes"
            }
        ],
        "random": [
            {
                "question": "Спал на лекции?",
                "image": "https://drive.google.com/file/d/1h_hg0D8vxNd23iWSqXayIp2OaGPOfXAo/view?usp=drive_link",
                "answer": "noR"
            },
            {
                "question": "Вжжж... на вас напал клоп!",
                "image": "https://drive.google.com/file/d/1u5jDh-iy_uhyJaaUwAgu-kdPqgcBWlk3/view?usp=drive_link",
                "answer": "yesR"
            },
            {
                "question": "Кто из них Оссейн?",
                "image": "https://drive.google.com/file/d/1zQyI0yZFKhKivmKd8NS_u9xU5IGd50KF/view?usp=drive_link",
                "answer": "yesR"
            },
            {
                "question": "Кто разрабатывает ImamAI?",
                "image": "https://drive.google.com/file/d/12jZkIsg0mSpZCHDOxH29ksit7ljGfK5i/view?usp=drive_link",
                "answer": "ArthurR"
            }
        ]
    }
    category_data = questions_data.get(category)
    return {category: category_data}
