# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API using the FastAPI framework and practice defining routes, handling request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create a FastAPI app

#### Description
Create a new FastAPI application in `starter-code.py` with a root endpoint and at least two additional routes.

#### Requirements
Completed app should:

- Import `FastAPI` and create an app instance.
- Define a root endpoint (`/`) that returns a welcome message.
- Include at least two more endpoints: one `GET` route and one `POST` route.

### 🛠️ Implement route parameters and query parameters

#### Description
Add routes that use path parameters and query parameters so the API can respond dynamically.

#### Requirements
Completed app should:

- Add a route like `/items/{item_id}` that returns the requested `item_id`.
- Add a `GET` route that accepts a query parameter such as `?category=` or `?limit=`.
- Return the path and query values in JSON format.

### 🛠️ Handle JSON request bodies

#### Description
Add a `POST` endpoint that receives JSON data and returns a processed response.

#### Requirements
Completed app should:

- Define a `POST` route such as `/users/` or `/orders/`.
- Accept JSON body data using a Pydantic model or raw Python dictionary.
- Return a JSON response that includes the submitted data and a confirmation message.

### 🛠️ Test the API locally

#### Description
Run the FastAPI app and confirm endpoints work using the browser or a tool like `curl`.

#### Requirements
Completed project should:

- Be runnable with `uvicorn starter-code:app --reload`.
- Return valid JSON responses from the defined endpoints.
- Include at least one example request in comments or README notes.
