# HTTP Haven & HTTP Resurgence — FastAPI Edition

**The goal of the exercise isn't to complete tasks but to build understanding.**

**DO NOT RUSH!**

Same 14 exercises, same test scripts, same "figure it out yourself" spirit — just aimed at FastAPI instead of Go's `net/http`. Where FastAPI/Starlette does something *for* you that Go made you do by hand (method routing, JSON validation, automatic 405s), that's called out explicitly, because noticing what a framework hides is as important as noticing what it exposes.

Submit each exercise as its own file, same as before: one repo `http-haven` (7 files) and one repo `http-resurgence` (7 files). Run each exercise with:

```bash
uvicorn exercise_N:app --reload --port 8080
```

(Keeping port 8080 instead of FastAPI's usual 8000 so the test scripts below work unmodified against either language's version.)

---

## Terminal Test Script (`test_endpoints.sh`)

Identical to the Go version — that's the point. If your Go server and your FastAPI server both pass the same black-box curl script, you've proven the two implementations are behaviorally equivalent even though the code underneath looks nothing alike.



# Exercise 1 — Basic Ping-Pong Server

**Goal:** Build a minimal FastAPI app that listens on port 8080 and responds with `"pong"` (plain text, not JSON) when a user visits `/ping`.

**Tasks:**
- Create `app = FastAPI()` and a `@app.get("/ping")` route.
- Return a plain string wrapped in `PlainTextResponse` — a bare `return "pong"` from a FastAPI handler gets JSON-encoded to `"pong"` (with quotes), which will *not* match the test script's string comparison. This is the first thing worth noticing: Go's `w.Write()` writes bytes with no opinion about format; FastAPI's default return path assumes JSON unless you say otherwise.
- Run with `uvicorn exercise_1:app --port 8080` (there's no `http.ListenAndServe` call inside your file — the ASGI server is a separate process).

**Think about —** what is `app` here, and why does `uvicorn` need to import it by name (`module:app`) instead of you calling `.run()` yourself the way Go calls `ListenAndServe` inline?

---

# Exercise 2 — Query Parameters & Path Validation

**Goal:** Create a `/hello` endpoint that reads a `name` query parameter (`/hello?name=Alice`) and responds with `"Hello, Alice!"`. If missing, default to `"Hello, Guest!"`.

**Tasks:**
- Declare the parameter directly in the function signature: `def hello(name: str = "Guest")`. FastAPI reads it from the query string automatically because it isn't part of the path — this replaces Go's explicit `r.URL.Query().Get("name")` call with a type-annotated default argument.
- Return `PlainTextResponse(f"Hello, {name}!")`.
- **Method rejection:** in Go you manually checked `r.Method` and called `http.Error(w, ..., http.StatusMethodNotAllowed)`. In FastAPI, declaring the route with `@app.get(...)` and *not* also declaring `@app.post(...)` means Starlette's router itself returns 405 for a POST to that path — you get the rejection for free. Confirm this rather than assuming it; add a comment noting whether you had to write any method-checking code at all.

---

# Exercise 3 — Text Counter (Body Parsing & Methods)

**Goal:** `/count` — GET returns `"Send a POST request with text to count words"`; POST reads the raw text body and returns the character count.

**Tasks:**
- Register two handlers on the same path: `@app.get("/count")` and `@app.post("/count")`. Go used one function with an `if r.Method ==` branch; FastAPI typically wants you to split by decorator instead — try writing it as two functions and think about why that's the idiomatic split rather than one function branching on `Request.method`.
- For the POST body, use `async def count(request: Request)` and `body = await request.body()` — this is FastAPI's equivalent of `io.ReadAll(r.Body)`. Note the `await`: reading the body is an async operation here, unlike Go's synchronous `io.ReadAll`.
- Return `str(len(body))` as plain text.

**Think about —** `await request.body()` gives you raw bytes, same as Go's `[]byte`. What's the character count if the client sends UTF-8 multi-byte characters — does `len(body)` (bytes) match `len(body.decode())` (characters)?

---

# Exercise 4 — Basic Math API (Multiple Query Parameters)

**Goal:** `/calculate?op=add&a=10&b=5` → `"Result: 15"`. Support `add`, `subtract`, `multiply`. Return 400 for an unknown op or bad parsing.

**Tasks:**
- Declare `a: int` and `b: int` directly as query parameters in the function signature. This is the biggest divergence from Go: `strconv.Atoi()` was a manual conversion you called yourself and had to check the error on; FastAPI/Pydantic does the conversion *and* the validation before your function body even runs. If `a=abc` is passed, FastAPI auto-returns a 422 Unprocessable Entity — not the 400 the test script expects.
- To match the test script's expected 400 instead of FastAPI's default 422, either: (a) declare `a: str` and `b: str` and do the `int()` conversion yourself inside a `try/except`, raising `HTTPException(status_code=400, ...)` on failure — this is closer to the original Go exercise's intent — or (b) add a custom exception handler for `RequestValidationError` that remaps 422 → 400 globally. Do (a) first; it's the more honest translation of what the Go version was teaching.
- Use `HTTPException(status_code=400, detail="...")` for an unknown `op`.

**Why this matters —** this is the exercise where "FastAPI validates for you" stops being purely a convenience and becomes a design decision you have to actively override. Knowing when to lean on Pydantic's validation versus writing your own is a real skill, not a shortcut.

---

# Exercise 5 — User-Agent Echo (Reading Headers)

**Goal:** `/agent` reads the `User-Agent` header and echoes: `"You are visiting us using: [User-Agent Info]"`.

**Tasks:**
- Declare it as a header parameter: `def agent(user_agent: str | None = Header(default=None))`. FastAPI converts the header name for you — `User-Agent` on the wire maps to the Python parameter `user_agent` (underscores, lowercased) automatically. This replaces `r.Header.Get("User-Agent")`.
- Handle the missing case explicitly, same as Go's blank-string fallback: if `user_agent is None`, decide what to echo (e.g. `"Unknown"`).

**Think about —** why does FastAPI ask you to write `user_agent` instead of `User-Agent` as the parameter name, and what does that tell you about how HTTP header names and Python identifiers don't overlap cleanly?

---

# Exercise 6 — Secure Dashboard (Header-Based Authorization)

**Goal:** `/dashboard` — reject requests missing a valid `X-API-Key` header with 401; allow through with a welcome message if it matches `secret123`.

**Tasks:**
- Read the header the same way as Exercise 5: `x_api_key: str | None = Header(default=None)`.
- Compare against the hardcoded value and `raise HTTPException(status_code=401, detail="Unauthorized")` on mismatch or absence.
- **Stretch, worth doing even though the Go version didn't ask for it:** rewrite this using FastAPI's `Depends()` dependency-injection system instead of an inline check — a `def verify_api_key(x_api_key: str = Header(...))` dependency that every protected route can reuse. This is the FastAPI-native way to express "this route requires auth," and there's no equivalent primitive in bare Go `net/http` (you'd hand-roll middleware instead).

---

# Exercise 7 — Simple Redirector (Status Codes)

**Goal:** `/legacy` permanently redirects to `/v2`, which responds with `"Welcome to version 2"`.

**Tasks:**
- Use `RedirectResponse(url="/v2", status_code=status.HTTP_301_MOVED_PERMANENTLY)` — this is the direct equivalent of Go's `http.Redirect(w, r, url, http.StatusMovedPermanently)`.
- Register `/v2` as its own plain route returning the welcome text.

---

---

# HTTP Resurgence — FastAPI Edition (v2)

Same numbering, same test script pattern as the Go version — only the port assumption (8080) and framework change. Recreate `test_endpoints.sh` from the Resurgence set unmodified; every assertion should still pass against your FastAPI implementations.

---

# v2 Exercise 1 — The Method Inspector

**Goal:** `/method-inspector` accepts *any* HTTP method and echoes it back: `"You made a GET request."` / `"You made a POST request."` / `"You made a [METHOD] request."`.

**Tasks:**
- This is the one exercise where FastAPI's per-verb decorators (`@app.get`, `@app.post`, ...) work against you, since the whole point is accepting everything through one handler. Use `@app.api_route("/method-inspector", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])` — Starlette's lower-level primitive for exactly this case — and read `request.method` inside.
- `async def method_inspector(request: Request): return PlainTextResponse(f"You made a {request.method} request.")`.

**Why this matters —** Go's `http.HandleFunc` was always method-agnostic by default (you had to add the rejection yourself); FastAPI's ergonomic per-verb decorators quietly assume you *want* rejection, so accepting everything takes one extra deliberate step (`api_route`) instead of being the default.

---

# v2 Exercise 2 — The Echo Chamber

**Goal:** `/echo` — POST only. Reads the full body and returns it byte-for-byte. Empty body → 400.

**Tasks:**
- `@app.post("/echo")`, `async def echo(request: Request): body = await request.body()`.
- Non-POST methods are already rejected with 405 by the route declaration itself — no manual check needed, unlike Go's explicit `if r.Method != http.MethodPost`.
- `if len(body) == 0: raise HTTPException(status_code=400, detail="body cannot be empty")`.
- Return the body as `Response(content=body, media_type="text/plain")` — using `Response` rather than `PlainTextResponse` here matters because you have raw `bytes`, not a `str`; `PlainTextResponse` expects a string and will error or force a decode.

**Think about —** Go's version made you `defer r.Body.Close()` right after error-checking, because leaving a body stream open leaks the connection. What is the equivalent resource-management concern in FastAPI's `async def` handlers, given that `await request.body()` reads the whole thing into memory in one call rather than exposing a stream you manage yourself?

**Stretch —** add `Response(..., headers={"Content-Type": "text/plain"})` explicitly and compare it against letting `media_type` set it. What's the actual difference between the two in the response you get back from curl?

---

# v2 Exercise 3 — Header Detective

**Goal:** `/headers` inspects `X-Custom-Token` and `Content-Type`. Missing token → 400. Present token → echo it plus the `Content-Type` (or a fallback message).

**Tasks:**
- `x_custom_token: str | None = Header(default=None)` and `content_type: str | None = Header(default=None)`.
- `if not x_custom_token: raise HTTPException(status_code=400, detail="X-Custom-Token header is missing")`.
- Build the two-line response exactly as specified:
  ```
  Token received: abc123
  Content-Type: application/json
  ```

**Stretch —** header names in HTTP are case-insensitive (`r.Header.Get` in Go handled this for you; so does FastAPI's `Header()` parameter). Confirm by sending `x-custom-token` in lowercase with curl and checking it still matches.

---

# v2 Exercise 4 — Form Decoder

**Goal:** `/form` — POST, URL-encoded body with `username` and `language`. Validate both non-empty; respond `"Hello [username], you are coding in [language]!"`.

**Tasks:**
- Declare form fields directly: `async def form(username: str = Form(...), language: str = Form(...))`. This is FastAPI's version of `r.ParseForm()` + `r.FormValue()` combined into one step — the parsing, extraction, *and* "is it present" check all happen before your function body runs, since `Form(...)` (the `...` meaning "required") makes FastAPI reject the request automatically if a field is absent from the body entirely.
- The Go exercise's distinct "username is required" vs "language is required" messages need you to *not* use `Form(...)` for this — use `Form(default="")` instead and check emptiness yourself with explicit `if not username: raise HTTPException(400, "username is required")` checks, so you control the message per field rather than getting FastAPI's generic 422.
- Requires `python-multipart` installed for form parsing to work at all — this has no Go equivalent to think about, but it's the kind of dependency gap that trips people up on their first form-handling route.

**Stretch —** reject non-form content types with 415, same as the Go version — check `request.headers.get("content-type")` before FastAPI's own form-parsing runs, which means dropping the `Form(...)` parameter declaration and reading the raw request instead.

---

# v2 Exercise 5 — Status Code Factory

**Goal:** `/status?code=404` responds using that exact status code. Missing/non-integer/out-of-range `code` → 400.

**Tasks:**
- `code: str = Query(...)` (read as a string first, deliberately, so you control the int-conversion error message — same reasoning as Exercise 4 in the Haven set).
- Validate: missing → `"code parameter is required"`; `int(code)` raising `ValueError` → `"code must be a valid integer"`; outside 100–599 → `"code must be a valid HTTP status code (100–599)"`. All three as 400s via `HTTPException`.
- Return the *dynamic* status code with `Response(content=f"Responding with status {code}", status_code=code)`.

**Critical rule, FastAPI edition —** Go's version made you think hard about `w.WriteHeader()` vs `w.Write()` ordering because the header is genuinely locked the instant bytes hit the socket. In FastAPI, `Response(content=..., status_code=...)` sidesteps this entirely — you build the whole response object, headers and status and body together, and return it in one shot. There's no equivalent moment where you can "accidentally" send a 200 before deciding the real code. Write a comment on whether you think this makes the underlying HTTP behavior different, or just hides the same rule behind an object constructor.

**Stretch —** use `http.client.responses[code]` (Python's standard-library status-text lookup, the equivalent of Go's `http.StatusText(code)`) to append the official reason phrase: `?code=404` → `"Responding with status 404 Not Found"`.

---

# v2 Exercise 6 — The API Subtree

**Goal:** Mount `/api/v1/ping` and `/api/v1/greet` under a `/api/v1` prefix, structurally separate from the main app's routes.

**Tasks:**
- FastAPI's direct equivalent of a second `http.ServeMux` mounted with `http.StripPrefix` is `APIRouter`:
  ```python
  from fastapi import APIRouter, FastAPI

  api_router = APIRouter(prefix="/api/v1")

  @api_router.get("/ping")
  def ping():
      return PlainTextResponse("pong")

  @api_router.get("/greet")
  def greet(name: str = "Stranger"):
      return PlainTextResponse(f"Greetings, {name}!")

  app = FastAPI()
  app.include_router(api_router)
  ```
- `app.include_router(api_router)` is doing exactly what `mainMux.Handle("/api/", http.StripPrefix("/api", apiMux))` did in Go: routes registered on the sub-router (`/ping`, `/greet`) are declared *without* the prefix, and the prefix is added once, at mount time, in one place.

**Think about, same prompts as the Go version, now against `APIRouter` —**
- What happens if you forget the `prefix="/api/v1"` argument and instead try to hardcode `/api/v1/ping` on every route inside `api_router` — what have you lost by doing it that way instead?
- Go's version made you reason about `http.StripPrefix` as a wrapping *handler*. Is `APIRouter` a handler in the same sense, or is it closer to a plain data structure that FastAPI flattens into the main app's route table at `include_router()` time? Try `print(app.routes)` after including the router and see what actually got registered.
- `http.ListenAndServe` took a `Handler` interface, satisfied by anything with the right method signature — that's why a bare `*http.ServeMux` could be passed directly. What does `uvicorn` require of `app`, and is FastAPI's `app` satisfying an interface in the same structural-typing sense, or is it a specific concrete class `uvicorn` knows about by name?

---

# v2 Exercise 7 — Template Renderer

**Goal:** `/render?title=X&body=Y` renders both into inline HTML. Missing either param → 400. Template defined in-file, no external HTML files.

**Tasks:**
- FastAPI doesn't ship a template engine the way Go's standard library ships `html/template` — you bring your own, almost always **Jinja2**. Install it (`pip install jinja2`) and note this is a real difference worth sitting with: Go's approach to HTML templating is "in the standard library, use it"; Python's is "bring your own, FastAPI just wires it up."
- Define the template as a Python string constant, same spirit as the Go raw-string constant:
  ```python
  from jinja2 import Template

  TMPL = Template("""
  <!DOCTYPE html>
  <html>
  <head><title>{{ title }}</title></head>
  <body>
    <h1>{{ title }}</h1>
    <p>{{ body }}</p>
  </body>
  </html>
  """)
  ```
- In the handler: read `title` and `body` as query params (`str | None = None`); if either is missing, `raise HTTPException(status_code=400, detail="title and body are required")`.
- Render with `TMPL.render(title=title, body=body)` — Jinja2's `.render()` is the equivalent of Go's `tmpl.Execute(w, PageData{...})`, except it returns a string rather than writing directly to the response stream, so there's no "headers get locked the instant Execute writes its first byte" moment to worry about — you build the full HTML string first, *then* wrap it in a response.
- Return `HTMLResponse(content=rendered_html)` — this sets `Content-Type: text/html` for you; you don't set the header manually the way the Go version required you to do before calling `Execute`.
- Jinja2 auto-escapes `{{ title }}` and `{{ body }}` by default when using `jinja2.Environment` with `autoescape=True` (FastAPI's `Jinja2Templates` helper turns this on for you) — Go's `html/template` does the same escaping automatically, unlike `text/template`. Note in a comment: what would happen to this exercise if `body` contained `<script>alert(1)</script>` — does your version escape it, and why does that matter?

**Stretch —** add a third param `style`; if `style=bold`, wrap `{{ body }}` in `<strong>` — Jinja2 conditionals use `{% if style == "bold" %}<strong>{{ body }}</strong>{% else %}{{ body }}{% endif %}`, structurally identical to Go's `{{if eq .Style "bold"}}` template syntax.

---

# FastAPI Cheat Sheet

## 1. Routing & App (`fastapi`, `uvicorn`)

| FastAPI / Starlette | Go equivalent | Notes |
|---|---|---|
| `app = FastAPI()` | `http.NewServeMux()` implicitly via `DefaultServeMux` | The app object *is* the router. |
| `@app.get("/path")` | `http.HandleFunc("/path", ...)` + manual method check | Verb is baked into the decorator; non-matching methods get an automatic 405. |
| `@app.api_route("/path", methods=[...])` | `http.HandleFunc` with no method filtering | Use when you genuinely want to accept multiple/any methods, like Exercise 1. |
| `APIRouter(prefix="/api/v1")` + `app.include_router(...)` | second `http.ServeMux` + `http.StripPrefix` | Groups related routes under a shared prefix, registered without the prefix internally. |
| `uvicorn app:app --port 8080` | `http.ListenAndServe(":8080", handler)` | The server process is external to your file; you don't call `.run()` inline. |
| `HTTPException(status_code, detail)` | `http.Error(w, msg, code)` | Raised, not called — Python's control flow (`raise`) replaces Go's "call then `return`" pattern. |
| `RedirectResponse(url, status_code)` | `http.Redirect(w, r, url, code)` | |

## 2. Reading Inputs (`Query`, `Header`, `Form`, `Request`)

| FastAPI | Go equivalent | Notes |
|---|---|---|
| `name: str = "Guest"` (query param) | `r.URL.Query().Get("name")` | Declared as a typed function argument, not fetched imperatively. |
| `code: int = Query(...)` | `strconv.Atoi(r.URL.Query().Get("code"))` | Type conversion + validation happen before your function runs — a 422 on failure unless you take the string first and convert yourself. |
| `token: str | None = Header(default=None)` | `r.Header.Get("X-Custom-Token")` | Header name auto-converted: `X-Custom-Token` → `x_custom_token`. |
| `username: str = Form(...)` | `r.ParseForm()` + `r.FormValue("username")` | Requires `python-multipart` installed. `Form(...)` = required, auto-422 if absent. |
| `await request.body()` | `io.ReadAll(r.Body)` | Returns raw `bytes`; must be awaited. |
| `request.method` | `r.Method` | Only accessible via the raw `Request` object, not injectable as a typed param. |

## 3. Sending Responses

| FastAPI | Go equivalent | Notes |
|---|---|---|
| `PlainTextResponse("pong")` | `fmt.Fprint(w, "pong")` | A bare `return "pong"` gets JSON-encoded instead — easy first mistake. |
| `Response(content=bytes_val, media_type="text/plain")` | `w.Write([]byte)` | Use when you have raw bytes, not a string. |
| `HTMLResponse(content=html_str)` | `w.Header().Set("Content-Type", "text/html")` + `w.Write(...)` | Sets the content type for you. |
| `Response(content=..., status_code=code)` | `w.WriteHeader(code)` then `w.Write(...)` | One constructor call replaces Go's strict two-step ordering rule. |
| `raise HTTPException(status_code=401, detail="...")` | `http.Error(w, "...", http.StatusUnauthorized)` | Short-circuits the handler immediately, like Go's early `return` after `http.Error`. |

## 4. Templating (`jinja2`)

| Jinja2 | Go `html/template` | Notes |
|---|---|---|
| `Template("...{{ title }}...")` | `` template.New("page").Parse(tmplStr) `` | No `.Must()` equivalent needed — Jinja2 raises `TemplateSyntaxError` immediately on bad syntax. |
| `tmpl.render(title=title, body=body)` | `tmpl.Execute(w, PageData{...})` | Returns a string instead of writing directly to `w` — build the string, then wrap it in a `Response`. |
| Autoescaping via `Jinja2Templates` / `Environment(autoescape=True)` | Automatic in `html/template` (not in `text/template`) | Both escape by default when used correctly — verify rather than assume. |

## 5. What FastAPI Gives You "For Free" (worth noticing, not just using)

1. **Method-not-allowed (405):** automatic from route declarations — no manual `r.Method` check.
2. **Type conversion + validation (422):** automatic from type-annotated parameters — but its default error code (422) doesn't match what these exercises ask for (400), so several exercises require you to *opt out* of the automatic behavior to match spec.
3. **Content-Type headers:** `HTMLResponse`, `JSONResponse`, etc. set them for you — Go required an explicit `w.Header().Set(...)` every time.
4. **Interactive docs:** visiting `/docs` on any of these apps gives you a live Swagger UI generated from your type annotations — there is no equivalent in plain Go `net/http` without a third-party library. Worth opening once, just to see what your query/header/form declarations produced automatically.
