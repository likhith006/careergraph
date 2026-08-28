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
