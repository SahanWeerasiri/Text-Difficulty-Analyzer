```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
import analyzer
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(request: TextRequest) -> Dict[str, float]:
    try:
        difficulty_score = analyzer.analyze_text_difficulty(request.text)
        return {"difficulty_score": difficulty_score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
```