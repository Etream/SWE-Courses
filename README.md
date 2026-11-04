<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">Carleton Course Graph & Prerequisite Visualizer</h3>

  <p align="center">
    A student-built tool designed to parse Carleton University's undergraduate course calendars, untangle complex prerequisite strings, and visualize degree paths as an interactive dependency graph.
    <br />
    <a href="#-roadmap">View Roadmap</a>
    ·
    <a href="https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/issues">Report Bug</a>
    ·
    <a href="https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#-getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#-roadmap">Roadmap</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-license">License</a></li>
    <li><a href="#-contact">Contact</a></li>
  </ol>
</details>

---

## About The Project

University degree planning shouldn't require decoding multi-line text strings like *"Prereq: COMP 1805 with min grade C- and (COMP 1406 or COMP 1006)"*. Official university portals often lack clean, intuitive visual tools for mapping out a 4-year degree path without hitting prerequisite dead ends.

This project solves that friction by:
* Scraping Carleton University's official undergraduate calendar.
* Parsing course blocks and isolating prerequisite requirements.
* *(Planned)* Rendering an interactive Directed Acyclic Graph (DAG) where students can click a 4th-year course to instantly highlight its required precursor path.

### Built With

* [![Python][Python.org]][Python-url]
* [![BeautifulSoup][BeautifulSoup.dev]][BeautifulSoup-url]
* *Planned:* React / React Flow

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3.x installed on your machine.

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   ```
2. Navigate to the project directory
   ```bash
   cd YOUR_REPOSITORY
   ```
3. Install required Python packages
   ```bash
   pip install requests beautifulsoup4
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

Run the data scraping script to fetch Carleton course blocks and print out their mapped prerequisites directly to your console:

```bash
python scraper.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

- [x] **Phase 1: Data Ingestion & Scraper**
  - [x] Connect to Carleton course catalog pages (COMP, SYSC).
  - [x] Safely scope and parse DOM elements (`div.courseblock`) to map titles to their respective raw prerequisites.
- [x] **Phase 2: Text Normalization & JSON Structure**
  - [x] Implement Regex parsing to convert natural language prerequisite strings into structured boolean dependency trees (AND/OR logic).
  - [x] Export structured data to a clean JSON format.
- [ ] **Phase 3: Interactive Visual Graph**
  - [ ] Set up a React frontend.
  - [ ] Integrate React Flow to render nodes and directed edges for course dependencies.
- [ ] **Phase 4: User State & Local Storage**
  - [ ] Add interactive checkboxes ("Mark as Completed") to dim finished courses and dynamically unlock valid upcoming options.

See the [open issues](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📬 Contact

Josh Niyo - niyorukj@gmail.com

Project Link: https://github.com/Etream/SWE-Courses

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[BeautifulSoup.dev]: https://img.shields.io/badge/BeautifulSoup-4-green?style=for-the-badge
[BeautifulSoup-url]: https://www.crummy.com/software/BeautifulSoup/
