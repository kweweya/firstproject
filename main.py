from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.responses import HTMLResponse
from starlette.routing import Route


async def homepage (request):
    return HTMLResponse ('<h1> What is your password </h1> <form method="post" action="/result"> <input type="password" name="name" /> <input type="submit" value="Submit" /></form>')

async def result (request):
    async with request.form() as form:
        if form and form["name"] and "admin" == form["name"]:
            return PlainTextResponse ("Success")
        else:
            return PlainTextResponse ("Failure")

app = Starlette(debug=True, routes=[
    Route ('/', homepage, methods=["GET"]),
    Route ('/result', result, methods=["POST"])
])
