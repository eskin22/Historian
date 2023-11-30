<p align="center">
    <img src="assets/logo.png" width="600" alt="logo">
</p>
<p align="center">
    Created by
    <img src="assets/test.svg" width="130" height="25" align="center">
</p>

---

![Python](https://img.shields.io/badge/Python-%233776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=%233776AB)
![JavaScript](https://img.shields.io/badge/JavaScript-%23F7DF1E?style=for-the-badge&logo=javascript&logoColor=black&labelColor=%23F7DF1E&color=%23F7DF1E)
![Plotly](https://img.shields.io/badge/PLOTLY-%233F4F75?style=for-the-badge&logo=plotly&logoColor=white&labelColor=%233F4F75&color=%233F4F75
)

![Release](https://img.shields.io/badge/release-Pre--Alpha-%23B5FF84?style=flat&logo=github&labelColor=%23181717)<br>
![Downloads](https://img.shields.io/badge/%E2%AC%87%EF%B8%8F_downloads-0-%23F1F1F1?style=flat&labelColor=%23181717)

# 🔎 Overview

> Final project for CS 410 Text Information Systems at the University of Illinois Urbana-Champaign

**Historian** is a Google Chrome extension that builds a knowledge graph of your visited webpages based on their similarity with respect to each other

**Features**
* Builds graph of webpages visited 
* Visualizes the similarity of webpages in history
* Presents an intuitive way to research

<br>

# 🎯 Objective

Create a Google Chrome extension that acts as a [knowledge graph builder](https://www.ibm.com/topics/knowledge-graph#:~:text=A%20knowledge%20graph%2C%20also%20known,the%20term%20knowledge%20%E2%80%9Cgraph.%E2%80%9D) for webpages that the user visits while researching information online.

The extension should represent the user's visited webpages as nodes in a graph where the edges reflect the relative similarity between them such that similar webpages will be clustered together.

This will offer users an intuitive way to visualize their search history while performing online research and eliminate the reliance on other third party applications to track this information.

# 📌 Tasks

| Task | Assigned To |
| --- | --- |
| Learn how to make a Chrome extension | Everyone |
| Visualizing Graphs | Blake |
| Web Scraping | Megha |
| Similarity Algorithm | Michael |
| Build Frontend | Rohan |
| Build Backend | Kaushal |

# 💙 Contributors

**Blake McBride** (Team Captain) <br> blakepm2@illinois.edu <br>
**Kaushal Dadi** <br> kdadi2@illinois.edu <br>
**Rohan Parekh** <br> rohanjp2@illinois.edu <br>
**Megha Chada** <br> megharc2@illinois.edu <br>
**Michael Ma** <br> chiuyin2@illinois.edu

## Prerequisites

- Node.js and npm installed for the frontend.
- Python 3.10.10 installed for the backend.

## Setup & Running Locally

### Frontend (React)

1. Navigate to the frontend directory:

```bash
cd ambassco-frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

By default, the frontend will be available at `http://localhost:3000`.

### Backend (Flask in Python)

1. Set up a virtual environment (if you haven't already):

```bash
python3 -m venv venv
```

2. Activate the virtual environment:

- **Linux/MacOS**:

```bash
source venv/bin/activate
```

- **Windows**:

```bash
venv\Scripts\activate
```

3. Install libraries:

```bash
pip install -r requirements.txt
```

Optionally, use this to add libraries to requirements.txt:
```bash
pip freeze > requirements. txt
```

4. Navigate to the backend directory:

```bash
cd backend
```

4. Start the Flask development server:

```bash
flask --app server run
```

Optionally run for automatic reloading when code changes:
```bash
flask --app server run --debug
```

By default, the backend will be available at `http://localhost:5000`.