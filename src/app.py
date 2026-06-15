

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Train for interschool soccer matches and improve teamwork",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["Lucas@mergington.edu", "Mia@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and compete in weekly scrimmages",
        "schedule": "Wednesdays and Fridays, 3:45 PM - 5:15 PM",
        "max_participants": 16,
        "participants": ["Noah@mergington.edu", "Ava@mergington.edu"]
    },
    "Volleyball Team": {
        "description": "Practice volleyball drills and compete in friendly matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["sophia@mergington.edu", "jack@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Develop tennis techniques and prepare for local tournaments",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["olivia@mergington.edu", "noah@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore drawing, painting, and creative design projects",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["Isabella@mergington.edu", "Ethan@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and capture creative images",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["mia@mergington.edu", "lucas@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Practice instruments and perform musical pieces together",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ava@mergington.edu", "ethan@mergington.edu"]
    },
    "Drama Club": {
        "description": "Rehearse scenes, develop acting skills, and prepare performances",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": ["Sophia@mergington.edu", "Liam@mergington.edu"]
    },
    "Debate Team": {
        "description": "Build public speaking, research, and argumentation skills",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["Olivia@mergington.edu", "Mason@mergington.edu"]
    },
    "Math Olympiad Club": {
        "description": "Solve advanced math problems and prepare for academic competitions",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["Emma@mergington.edu", "Sophia@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build robots, learn engineering concepts, and tackle STEM challenges",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["michael@mergington.edu", "isabella@mergington.edu"]
    },
    "Science Club": {
        "description": "Explore experiments, scientific ideas, and hands-on research",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["daniel@mergington.edu", "sophia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

 # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up for this activity")

    # Add student
   
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
