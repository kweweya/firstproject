from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.responses import HTMLResponse
from starlette.routing import Route


async def homepage (request):
    return HTMLResponse ('<h1> Admin Login </h1> <form method="post" action="/result"> <input type="text" name="user"> <input type="password" name="pass" /> <input type="submit" value="Submit" /></form>')

async def result (request):
    async with request.form() as form:
        if form and form["user"] and form["pass"] and "admin" == form["user"] and "12345678" == form["pass"]:
            return PlainTextResponse ("Success")
        else:
            return PlainTextResponse ("Failure")

app = Starlette(debug=True, routes=[
    Route ('/', homepage, methods=["GET"]),
    Route ('/result', result, methods=["POST"])
])
