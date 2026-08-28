# CareerGraph
> A graph-powered career exploration platform that connects careers, skills, courses, projects, and related career paths.

## Demo

CareerGraph allows users to:

- Search for careers
- Explore required skills
- Discover relevant courses
- Explore project ideas
- Find related careers
- Visualize career relationships as an interactive graph
CareerGraph is a graph-powered career exploration application built with Flask, Python, Neo4j/CognoDB, Cypher, and Cytoscape.js.

The application helps users explore career paths through connected skills, courses, projects, and related careers.

---

## Deploy to Vercel

1. Import this repository into Vercel. The included `vercel.json` routes requests to the Flask app in `app.py`.
2. Add these environment variables in the Vercel project settings for every environment you deploy:

	- `COGNODB_URI`
	- `COGNODB_USERNAME`
	- `COGNODB_PASSWORD`

3. Deploy. The Neo4j connection is created lazily when a request needs database data, so Vercel can import the app during its build step.

Before the first deployment, create the database constraints and seed data from a machine that can reach the database:

```powershell
.\venv\Scripts\python.exe -m database.schema
.\venv\Scripts\python.exe -m database.seed
```

For local development, put the same variables in a `.env` file and run:

```powershell
.\venv\Scripts\python.exe app.py
```

---

## Features

- Career exploration
- Career search with live suggestions
- Required skills for each career
- Recommended courses
- Project ideas
- Related career paths
- Multi-hop graph traversal
- Interactive graph visualization
- Parameterized Cypher queries
- Error handling for missing pages and database failures

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| CognoDB / Neo4j | Graph database |
| Cypher | Graph queries |
| Neo4j Python Driver | Database connectivity |
| HTML/CSS | Frontend |
| JavaScript | Frontend interactions |
| Cytoscape.js | Graph visualization |

---

## Project Structure

```text
careergraph/
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── schema.py
│   ├── seed.py
│   └── queries.py
│
├── templates/
│   ├── index.html
│   ├── career.html
│   └── error.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── app.py
├── test_connection.py
├── test_queries.py
├── requirements.txt
├── .gitignore
└── README.md
