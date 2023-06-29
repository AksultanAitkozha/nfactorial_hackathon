from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl


class QuestionData(BaseModel):
    question: str
    image: HttpUrl
    answer: str


app = FastAPI()


@app.get("/questions/{category}", response_model=List[QuestionData])
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
            }
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
    if category in questions_data:
        return questions_data[category]
    else:
        raise HTTPException(status_code=404, detail="Category not found")
