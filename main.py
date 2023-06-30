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
                "question": "Есть любимый ментор?",
                "image": "mentors",
                "answer": "yes"
            },
            {
                "question": "Запитчил идею Арману?",
                "image": "arman_su",
                "answer": "yes"
            },
            {
                "question": "Сделал больше трёх домашек по бэку?",
                "image": "ali_tlek",
                "answer": "yes"
            },
            {
                "question": "Шаришь за лангчейн? 🤔",
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
                "image": "mentors",
                "answer": "yes"
            },
            {
                "question": "Показал MVP?",
                "image": "gustavo_fring",
                "answer": "yes"
            },
            {
                "question": "Любишь проект, который ты делаешь?",
                "image": "love",
                "answer": "yes"
            },
            {
                "question": "Знаешь, как набрать первые 5к юзеров?",
                "image": "popular",
                "answer": "yes"
            },
            {
                "question": "Можешь назвать себя промпт инженером?",
                "image": "prompt_eng",
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
                "question": "С длинными волосами лучше?",
                "image": "ossein",
                "answer": "yesR"
            },
            {
                "question": "ImamAI разрабатывает Артур?",
                "image": "arthur_ossein",
                "answer": "noR"
            },
            {
                "question": "Ставил балапашку, чтобы получить ваучер?",
                "image": "balapan",
                "answer": "yesR"
            },
            {
                "question": "НУшников много! заметил? NUfactorial прям :)",
                "image": "nu",
                "answer": "yesR"
            },
            {
                "question": "Многих запомнил после спид дейтинга?",
                "image": "date",
                "answer": "yesR"
            },
            {
                "question": "Поднялся по ступеням до Горельников без одышки?",
                "image": "gorelnik",
                "answer": "yesR"
            },
            {
                "question": "Играл в мафию в читалке?",
                "image": "mafia",
                "answer": "yesR"
            },
            {
                "question": "Сфоткался с Ерсултаном?",
                "image": "office",
                "answer": "yesR"
            },
            {
                "question": "Dalida is the Queen?",
                "image": "dalida",
                "answer": "yesR"
            },
        ]
    }
    category_data = questions_data.get(category)
    return {category: category_data}
