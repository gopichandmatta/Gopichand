# Price Comparison Service

This project is a backend system for a price comparison service that aggregates product prices from various online stores. It is implemented using FastAPI and SQLAlchemy.

## Project Structure
price_comparison_service/
├── app/
│ ├── init.py
│ ├── crud.py
│ ├── database.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
├── data/
│ └── store_data.json
├── venv/
└── requirements.txt


## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Setup Instructions

## Search Products[GET]
URL: /api/products?name=<product_name>

## Add Product [POST]
URL: /api/products

## Get All Products[GET]
URL: /api/products

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/price_comparison_service.git
   cd price_comparison_service

## Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate


## Install Dependencies
pip install -r requirements.txt

## Run the Application
uvicorn app.main:app --reload



