# Product Management System

It is a product management system that allows you to create, retrieve, update and delete products. It uses FastAPI for API construction, SQLAlchemy for database interaction, Alembic for database migrations, and Pydantic for data validation.

## Technologies

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- SQLite (можна змінити на іншу СУБД)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/product-management-system.git
cd product-management-system
```

### Step 2: Creating a virtual environment

It is recommended to use a virtual environment to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
```

### Step 3: Installing dependencies

Install the necessary libraries:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the database

We use Alembic for database migrations. To initialize Alembic, run the following commands:

```bash
alembic init alembic
```

Configure the alembic.ini file with the URL of your database. For SQLite, the default will be:

```bash
sqlalchemy.url = sqlite:///./test.db
```

Create the first migration:

```bash
alembic revision --autogenerate -m "Create products table"
alembic upgrade head
```

### Step 5: Start the server

Start the FastAPI server:

```bash
uvicorn main:app --reload
```
The server will be available at http://127.0.0.1:8000.

### Step 6: Using Swagger UI
The API automatically generates documentation using the Swagger UI. Go to: http://127.0.0.1:8000/docs There you can test all endpoints.

## API Endpoints

- ##### Get product list (GET /products/) - This endpoint allows you to get a list of all products.
- ##### Product creation (POST /products/) - This endpoint allows you to create a new product.
- ##### Get product (GET /products/{id}) - This endpoint allows you to get information about a product by its ID.
- ##### Product update (PUT /products/{id}) - This endpoint allows you to update a product by its ID.
- ##### Deleting a product (DELETE /products/{id}) - This endpoint allows you to remove a product by its ID.

