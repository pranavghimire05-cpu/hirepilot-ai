from app.agents.resume_agent import ask_resume

print(
    ask_resume(
        question="Do I have experience with FastAPI?",
         resume_id="ea9e4c03-ba49-4bc2-84bd-0f6539d87f10"
    ).content
)