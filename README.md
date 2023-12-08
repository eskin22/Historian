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

# ▶️ Usage

## Local Setup

Historian is not currently being hosted on a domain, which means that the only way to currently use this extension is by running the server locally on your machine. The instructions below will guide you through the setup process step-by-step.

### Step 1: Clone this Repository

First you need to clone this repo to your local machine to access the server as well as the extension. Once cloned, you should be able to run the local server and load the unpacked extension into Google Chrome.

### Step 2: Start the local server

Once you've cloned the repo, you can host the local server on your machine to enable the backend functionality of the extension.

To run the server, simply navigate to the directory of the repo and run `server.py`.

> [!IMPORTANT]
> Historian works by sending a list of the URLs from your history to the server, which will then perform the computations needed to create the graph. Once completed, the server will asynchrononously update the graph on the frontend for you to see. Thus, it is imperative that you run the server in order to see your results visualized. 

To run the server, simply navigate to the directory of the repo and run `server.py`

### Step 3: Load the unpacked extension into Chrome

### Step 4: Displaying the graph 

# 💙 Contributors

**Blake McBride** (Team Captain) <br> blakepm2@illinois.edu <br>
**Kaushal Dadi** <br> kdadi2@illinois.edu <br>
**Rohan Parekh** <br> rohanjp2@illinois.edu <br>
**Megha Chada** <br> megharc2@illinois.edu <br>
**Michael Ma** <br> chiuyin2@illinois.edu