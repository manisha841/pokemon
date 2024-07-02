# Pokemon API

## Setup Instructions

### 1. Clone the repository
   ``` git clone git@github.com:manisha841/pokemon.git```

### 2. Create and activate virtual environment depending on your OS 
For linux: \
```virtualenv env``` \
```source env/bin/activate```

### 3. Install the dependencies
```pip install -r requirements.txt```

### 4. Install pre-commit
```` pre-commit install ````

### 5. Create .env file in the root of the folder, setup Database and add necessary credentials in .env file 

```DATABASE_URL=postgresql+asyncpg://username:password@localhost/dbname```

### 6. Fetch pokemon data by running the following command:
``` python fetch_pokemons.py```

### 7. Run the application

````uvicorn app.main:app --reload ````