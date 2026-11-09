"""
https://fastapi.tiangolo.com/
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Simple app
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def dashboard(request: Request):
    results = [
        {"device": "router-01", "datacenter": "US-East", "cpu": 92.4},
        {"device": "router-02", "datacenter": "US-West", "cpu": 45.2},
        {"device": "router-03", "datacenter": "US-East", "cpu": 78.1},
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"results": results},
    )

    # If using pandas DataFrame, you can convert it to html and pass it to the template
    # df = pd.DataFrame(results)
    # return templates.TemplateResponse(request=request, name="index.html", context={"results": df.to_html()})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # From terminal
    # uv run uvicorn fastapi_stuffz:app --reload