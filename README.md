# Website Link

https://jo-saa-analysis.vercel.app/

# JOSAA Seat Allotment Portal

This project aims to create a portal to explore the seat allotment statistics of the Joint Seat Allocation Authority (JOSAA) until 2023. The portal allows users to analyze the data and provides insights and visualizations based on the JOSAA seat allotment data from 2016 to 2023. The following are the key goals and technologies used in this project.

## Goals
- Perform data cleaning and exploratory data analysis (EDA) on the JOSAA seat allotment data.
- Create a SQLite database from the cleaned data and perform queries on it.
- Create a website to present the analysis using various charts and tables.

## Tech Stack/Frameworks
- Frontend: HTML, CSS, JavaScript
- Backend: Django, SQLite
- Data Scraping: Selenium
- Data Cleaning: NumPy, Pandas
- Visualization: Chart.js

## Usage
To run the JOSAA Seat Allotment Portal locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/josaa-portal.git`
2. Change to the project directory: `cd josaa-portal`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Run database migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Access the portal in your web browser at `http://localhost:8000/`

## Data Extraction and Cleaning
The JOSAA seat allotment data has been provided and is ready for analysis. The data cleaning process involves using the NumPy and Pandas libraries to clean and transform the data as required for analysis.

## Data Analysis and Insights
The cleaned data is stored in a SQLite database. The website's "Insights" page presents various charts and tables generated using Chart.js, providing users with visualizations and insights based on the data.

## Final Output
When we run this project on our local servers we mainly get 4 sections to analyze the data based on various trends.
1) Analyse trends based on year : Discover the yearwise cutoff variations and delve into valuable insights on admission trends.
2) Analyse trends based on Round : Analyse trends based on roundwise cutoffs for years.
3) Best institute for coursed : Find best IIT for selected course based on last year's data.
4) Know your IIT : Explore your IIT possibilities with last year's cutoffs,revealing the institution that could be your future.

## Ouptut Files
In the Outputs(images & video) folder we have droped some graph images and also video of working project.

## Contributions
Contributions to this project are welcome! If you have any suggestions, improvements, or new features to add, please open an issue or submit a pull request.

## Acknowledgements
This project makes use of the following open-source libraries and frameworks:
- Django: https://www.djangoproject.com/
- Selenium: https://www.selenium.dev/
- Pandas: https://pandas.pydata.org/
- NumPy: https://numpy.org/
- Chart.js: https://www.chartjs.org/

We would like to express our gratitude to the developers of these tools for their invaluable contributions to the open-source community.
