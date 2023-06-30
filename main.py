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
                "image": "blue_red_pill",
                "answer": "optional"
            },
            {
                "question": "Твой любимый ментор?",
                "image": "https://drive.google.com/file/d/1pn6PVxh9IFpee38ip3N5y3FnfbiRCZ1a/view?usp=sharing",
                "answer": "optional"
            },
            {
                "question": "Запитчил идею Арману?",
                "image": "https://drive.google.com/file/d/1cEErufIAhYnr7bx0Mof_qmmCRfZg1AYe/view?usp=sharing",
                "answer": "yes"
            },
            {
                "question": "Сделал больше трёх домашек по бэку?",
                "image": "ali_tlek",
                "answer": "yes"
            },
            {
                "question": "Шаришь за лангчейн? а за векторные базы данных? 🤔",
                "image": "doge",
                "answer": "yes"
            },
            {
                "question": "Не пропустил ни одну лекцию?",
                "image": "full_attendance",
                "answer": "yes"
            },
            {
                "question": "Знаком с каждым ментором?",
                "image": "gustavo_fring",
                "answer": "yes"
            },
            {
                "question": "Показал MVP?",
                "image": "gustavo_fring",
                "answer": "yes"
            },
            {
                "question": "любишь проект, который ты делаешь?",
                "image": "gustavo_fring",
                "answer": "yes"
            },
            {
                "question": "Знаешь, как набрать первые 5к юзеров?",
                "image": "popular",
                "answer": "yes"
            },
            {
                "question": "За AI будущее! согласен?",
                "image": "future",
                "answer": "yes"
            },
            {
                "question": "го делать KazakhGPT? just for fun :)",
                "image": "kazakh",
                "answer": "yes"
            },
        ],
        "random": [
            {
                "question": "Спал на лекции?",
                "image": "sleepy_kasym",
                "answer": "noR"
            },
            {
                "question": "Вжжж... на нас напал клоп!",
                "image": "cockroach",
                "answer": "yesR"
            },
            {
                "question": "Кто из них Оссейн?",
                "image": "imgonline-com-ua-twotoone-L8LnrnsCBzlS3(1)",
                "answer": "yesR"
            },
            {
                "question": "кто разрабатывает ImamAI? первое демо, как никак",
                "image": "arthur_ossein",
                "answer": "noR"
            },
            {
                "question": "Ставил балапашку, чтобы получить ваучер?",
                "image": "balapan",
                "answer": "yesR"
            },
            {
                "question": "НУшников много! заметил?",
                "image": "nu_uni",
                "answer": "yesR"
            },
            {
                "question": "многих запомнил после спид дейтинга?",
                "image": "date",
                "answer": "yesR"
            },
        ]
    }
    category_data = questions_data.get(category)
    return {category: category_data}
