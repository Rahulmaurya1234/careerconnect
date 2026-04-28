# CareerConnect – Job Portal Web Application

CareerConnect is a full stack web application built using Django, designed to connect job seekers with employers. The platform provides features such as user authentication, job posting, resume management, and dashboard functionality.

---

## Live Demo

https://careerconnect-3z8g.onrender.com/

---

## Overview

CareerConnect is a job portal system that allows users to:

- Register and manage profiles  
- Browse and apply for jobs  
- Upload and manage resumes  
- Access personalized dashboards  

The application follows Django’s MVC (MVT) architecture and is built for scalability and real-world usage.

---

## Tech Stack

- Python  
- Django  
- HTML, CSS, JavaScript  
- SQLite (or your DB)  
- Django Templates  

---

## Project Structure

careerconnect/
├── about/ # About page module
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── accounts/ # User authentication & profile
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│
├── contact/ # Contact form module
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── core/ # Main app logic (home, base templates)
│ ├── views.py
│ ├── urls.py
│
├── customer_dashboard/ # User dashboard features
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── dashboard/ # Admin / analytics dashboard
│ ├── migrations/
│ ├── views.py
│ ├── urls.py
│
├── jobs/ # Job listings & applications
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── ml/ # Machine learning module (optional)
│ ├── models.py
│ ├── views.py
│
├── profilename/ # Profile management
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│
├── resumes/ # Resume upload & handling
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│
├── static/ # Static files (CSS, JS, Images)
│ ├── css/
│ ├── js/
│ ├── images/
│
├── templates/ # HTML templates
│ ├── base.html
│ ├── about/
│ ├── accounts/
│ ├── contact/
│ ├── core/
│ ├── dashboard/
│ ├── jobs/
│ ├── profilename/
│
├── manage.py # Django management script
├── db.sqlite3 # Database file
├── requirements.txt # Project dependencies
├── render.yaml # Deployment configuration


---

## Features

- User authentication (login/register/logout)  
- Profile management  
- Job listing and job application system  
- Resume upload and management  
- Dashboard for users  
- Admin panel for managing data  
- Organized Django apps for modular structure  

---

## Modules

- Accounts: User authentication and profile  
- Jobs: Job posting and listings  
- Resumes: Resume upload and management  
- Dashboard: User-specific dashboard  
- Core: Main application logic  
- ML: (Optional) Machine learning module  

---

## Installation & Setup

### 1. Clone the repository


git clone https://github.com/Rahulmaurya1234/your-repo-name.git
cd careerconnect

## 2. Create virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

## 3. Install dependencies

pip install -r requirements.txt

## 4. Run migrations

python manage.py migrate

## 5. Run server

python manage.py runserver
 
Future Improvements : 
  Advanced job filtering and search
  Recommendation system (ML-based)
  Notification system
  Resume parsing
  Improved UI/UX
  
## Screenshots

<p align="center">
  <img src="Home.png" width="45%"/>
  <img src="Job.png" width="45%"/>
</p>

<p align="center">
  <img src="dashboard.png" width="45%"/>
  <img src="Profile.png" width="45%"/>
</p>

<p align="center">
  <img src="about.png" width="45%"/>
</p>


## Author

Rahul Maurya
GitHub: https://github.com/Rahulmaurya1234

Portfolio: https://rahulmaurya1234.github.io/my-portfolio/

Email: rahul2003maurya@gmail.com

This project demonstrates full stack development using Django with modular architecture and real-world job portal features.
