# Grazioso-Salvare-Rescue-Animal-Dashboard
### A.R.I.D© Animal Rescue Intelligence Dashboard

> Transforming raw shelter data into life-saving operational intelligence.

**Role:** Full-Stack / Backend Engineer (Academic Project)  
**Author:** Zion Kiniebrew-Jenkins  
**Institution:** Southern New Hampshire University, CS 340  
**Tech Stack:** Python · MongoDB · Dash · Plotly · pandas · dash-leaflet

---

## Table of Contents

- [Project Summary](#-project-summary)
- [Skills Demonstrated](#-skills-demonstrated)
- [Problem Statement](#-problem-the-system-solves)
- [Architecture](#-architecture-overview)
- [Technology Stack](#️-technology-stack)
- [Setup Instructions](#️-setup-instructions)
- [Project Structure](#-project-structure)
- [CRUD Module](#-crud-module)
- [Running the Application](#️-running-the-application)
- [Core Features](#-core-features)
- [Example Query](#-example-mongodb-query)
- [Portfolio Reflection](#-portfolio-reflection)
- [Roadmap](#-roadmap)

---

## 🚀 Project Summary

A full-stack, data-driven dashboard that transforms raw animal shelter data into actionable intelligence for a rescue-training organization. Built with a clean MVC architecture and production-style engineering practices.

| Outcome | Detail |
|---|---|
| 🔐 Security | Secure authentication and role-based database access |
| 🧩 Modularity | Reusable Python CRUD data layer decoupled from UI |
| ⚡ Real-Time | Live filtering, sorting, and analytics |
| 🗺 Geospatial | Interactive shelter mapping via dash-leaflet |
| 🏗 Architecture | Production-style modular, maintainable design |

---

## 💼 Skills Demonstrated

- Database design and CRUD abstraction
- Secure authentication workflows
- Modular, maintainable Python architecture
- Data visualization and interactive analytics
- Full-stack application development
- Client requirement analysis and translation
- Debugging and performance optimization

---

## 🧠 Problem the System Solves

**Grazioso Salvare** evaluates thousands of animal shelter records to identify dogs suitable for specialized rescue operations:

| Mission Type | Description |
|---|---|
| 🌊 Water Rescue | Breeds suited for aquatic environments |
| 🏔 Mountain / Wilderness | Dogs trained for high-altitude terrain search |
| 🔍 Disaster and Tracking | Scent and detection specialists |

Manual review of shelter databases is slow and error-prone. This dashboard enables staff to **filter, analyze, and visualize data instantly**, improving decision accuracy and operational efficiency at scale.

---

## 🏗 Architecture Overview

```
MongoDB (Model)
      │
      ▼
Python CRUD Module (Data Access Layer)
      │
      ▼
Dash Callbacks (Controller)
      │
      ▼
Interactive Dashboard (View)
```

All database operations are isolated inside a reusable `AnimalShelter` class, ensuring:

- **Clean separation of concerns** — UI changes never break database logic
- **Easy refactoring** — swap databases without touching the application layer
- **Reusability** — the CRUD module is portable across future projects

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Application logic and data processing |
| **MongoDB** | Document-based NoSQL database |
| **Dash** | Reactive web application framework |
| **Plotly** | Interactive charting and visualization |
| **dash-leaflet** | Geospatial mapping |
| **pandas** | Data filtering and aggregation |

---

## ⚙️ Setup Instructions

### 1️⃣ Start MongoDB

```bash
sudo systemctl start mongod
```

Verify the service is running:

```bash
sudo systemctl status mongod
```

### 2️⃣ Import the Dataset

```bash
mongoimport --db AAC \
  --collection animals \
  --type csv \
  --headerline \
  --file aac_shelter_outcomes.csv
```

### 3️⃣ Create a Database User

```bash
mongosh
```

```js
use AAC

db.createUser({
  user: "aacuser",
  pwd: "SNHU1234",
  roles: [{ role: "readWrite", db: "AAC" }]
})
```

### 4️⃣ Install Dependencies

```bash
pip install jupyter-dash dash dash-leaflet plotly pandas pymongo
```

---

## 📁 Project Structure

```
grazioso-salvare/
├── CRUD_Python_Module.py        # Reusable database access layer
├── dashboard_upgraded.py        # Main dashboard application
├── ProjectTwoDashboard.ipynb    # Jupyter Notebook version
├── aac_shelter_outcomes.csv     # Animal shelter dataset
├── Grazioso Salvare Logo.png    # Organization branding
└── README.md
```

---

## 🔌 CRUD Module

The `AnimalShelter` class abstracts all database operations, keeping the UI completely decoupled from persistence logic.

```python
from CRUD_Python_Module import AnimalShelter

# Authenticated database connection
db = AnimalShelter("aacuser", "SNHU1234")

# Query for all dogs
results = db.read({"animal_type": "Dog"})

for record in results:
    print(record["name"], record["breed"])
```

> **Why this matters:** This abstraction means the UI layer can be entirely redesigned, or the database swapped out, without a single change to the data logic. It is a critical maintainability pattern in professional engineering environments.

---

## ▶️ Running the Application

**Option A — Python Script**

```bash
python dashboard_upgraded.py
```

**Option B — Jupyter Notebook**

Open `ProjectTwoDashboard.ipynb` and run all cells. A preview URL will be generated:

```
https://<codio-domain>-8060.codio.io
```

**Login Credentials**

| Field | Value |
|---|---|
| Username | `aacuser` |
| Password | `SNHU1234` |

---

## 📊 Core Features

| Feature | Description |
|---|---|
| 🔐 Authentication Gate | Secure login before dashboard access |
| 🎯 Rescue-Type Filters | One-click presets for Water, Mountain, and Disaster |
| 🔬 Multi-Filter Controls | Advanced compound filtering by breed, age, and sex |
| 📋 Data Table | Paginated, sortable, searchable animal records |
| 📈 Analytics Charts | Breed distribution and demographic breakdowns |
| 🗺 Geospatial Map | Interactive shelter location mapping |
| 📌 KPI Cards | At-a-glance summary statistics |
| 🌗 Dark / Light Mode | User-selectable theme toggle |
| 📥 CSV Export | One-click data download |
| 🚪 Session Logout | Secure session termination |

---

## 🧪 Example MongoDB Query

**Water Rescue Filter**

```python
query = {
    "breed": {"$in": [
        "Labrador Retriever Mix",
        "Chesapeake Bay Retriever",
        "Newfoundland"
    ]},
    "sex_upon_outcome": "Intact Female",
    "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
}

results = db.read(query)
```

This query runs cleanly through the CRUD module with no UI coupling. Changes to rescue criteria require updating only the query, not the application structure.

---

## 📓 Portfolio Reflection

### How do you write programs that are maintainable, readable, and adaptable?

Writing maintainable code starts with discipline at the structural level, before a single function is written. For this project, that meant committing to a strict separation of concerns from the beginning: the database layer would never know about the UI, and the UI would never write a raw database query. Every operation that touched MongoDB was routed through the `AnimalShelter` CRUD class, which exposed clean, intention-revealing methods like `read()`, `create()`, `update()`, and `delete()`. Inside those methods, I used descriptive variable names, inline comments explaining non-obvious logic, and kept each method focused on a single responsibility so that future developers, or a future version of myself, could open any file and understand its purpose within seconds.

The advantages of working this way became clear during development. When the dashboard's filtering requirements changed, for example adjusting the age range for water rescue candidates, I only needed to modify the query dictionary passed into `db.read()`. Nothing else in the application changed. That kind of insulation between layers is what separates maintainable code from code that becomes a liability as requirements evolve.

The CRUD module has clear utility beyond this project. It could be reused as the data access layer for a REST API built with Flask or FastAPI, exposing the same animal shelter data to mobile apps or third-party systems without rewriting any database logic. It could also serve as the backend for an automated reporting pipeline, where a scheduled script calls `db.read()` with different queries each morning and emails summary statistics to shelter administrators. Because the module is fully decoupled from any specific application, it is plug-and-play for any Python project that needs to interact with this database.

---

### How do you approach a problem as a computer scientist?

My approach to this project followed a deliberate sequence: understand the client's operational reality first, then design the data model, then build the interface around it, never the other way around. When Grazioso Salvare's requirements called for filtering animals by rescue type, my first instinct was not to build a dropdown. It was to understand *why* certain breeds and age ranges matter for each mission type, so that the MongoDB queries would accurately reflect real-world rescue criteria rather than arbitrary guesses. That domain understanding shaped every technical decision that followed, from the compound query structure to the way filter presets were organized in the UI.

This approach differed meaningfully from previous course assignments, which typically provided a fully-defined problem with a known correct answer. There, the challenge was implementation. Here, the challenge was interpretation: translating ambiguous client goals into precise, testable technical specifications. I had to ask questions like what does "suitable for water rescue" actually mean in terms of breed, age, and sex, and what does a staff member need to see at a glance to make a confident placement decision. Those questions do not appear in a textbook, and learning to ask them is one of the most transferable skills this project developed.

For future database projects serving client needs, I would apply several strategies learned here. First, index fields that appear in frequent query filters early in the design process to prevent performance degradation as the dataset grows. In this project, those fields were `breed`, `sex_upon_outcome`, and `age_upon_outcome_in_weeks`. Second, design the schema around query patterns rather than around the raw data shape; documents should be structured the way they will be read, not just the way they arrive. Third, prototype queries directly in `mongosh` before wiring them into the application, so that correctness is verified independently of the UI.

---

### What do computer scientists do, and why does it matter?

Computer scientists translate complex, messy human problems into systems that are faster, more consistent, and more scalable than any manual process could be. The work is fundamentally about leverage: a well-designed system lets a small team accomplish what would otherwise require far more people, time, and resources, while also reducing the errors that come from fatigue and inconsistency.

For an organization like Grazioso Salvare, this project eliminates several specific operational bottlenecks. Before a dashboard like this, identifying a suitable water rescue candidate likely meant a staff member manually reviewing hundreds of CSV rows, cross-referencing breed lists, and filtering by age, a process that could take hours and was vulnerable to human error. A missed record could mean a well-qualified dog is overlooked; an incorrect match could place an animal in a dangerous environment. The dashboard reduces that process to seconds, applies the criteria consistently every time, and surfaces the data in a format that supports confident, informed decisions rather than educated guesses.

More broadly, this project illustrates why software engineering matters beyond the technical: it directly affects outcomes for real animals and the communities those animals are trained to serve. The code itself is invisible to the end user, but its effects, including faster placements, better-matched rescue teams, and fewer errors, are entirely concrete. That connection between engineering decisions and real-world impact is what makes computer science more than a technical discipline. It is, at its best, a tool for making organizations and the people they serve meaningfully better off.

---

## 🗺 Roadmap

| Enhancement | Status |
|---|---|
| Role-based access control (RBAC) | Planned |
| REST API layer | Planned |
| Cloud deployment (Docker / AWS) | Planned |
| Automated test suite (pytest) | Planned |

---

## 📄 License

Open-source and available for educational or organizational adaptation.

---

*Built with Python, MongoDB, and Dash · Southern New Hampshire University CS 340*
