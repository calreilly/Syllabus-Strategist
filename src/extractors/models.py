from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class Assignment(BaseModel):
    title: str = Field(..., description="Name of the assignment, exam, or project")
    due_date: Optional[str] = Field(None, description="Due date as mentioned in the syllabus (e.g., 'Oct 4', 'Week 5')")
    weight: Optional[str] = Field(None, description="Percentage of grade (e.g., '20%', '100 points')")
    description: Optional[str] = Field(None, description="Brief details about the assignment")

class ScheduleItem(BaseModel):
    date: Optional[str] = Field(None, description="Date or Week number (e.g., 'Week 1', 'Jan 15')")
    topic: str = Field(..., description="Main topic covered")
    readings: List[str] = Field(default_factory=list, description="Required readings for this period")

class Syllabus(BaseModel):
    course_code: str = Field(..., description="Course code (e.g., 'GRAD 5900')")
    course_title: str = Field(..., description="Full name of the course")
    instructor: Optional[str] = Field(None, description="Name of the instructor")
    semester: Optional[str] = Field(None, description="Semester and Year (e.g., 'Spring 2026')")
    assignments: List[Assignment] = Field(default_factory=list, description="List of all graded items")
    schedule: List[ScheduleItem] = Field(default_factory=list, description="Weekly schedule or calendar")
    policies: List[str] = Field(default_factory=list, description="Key policies (late work, attendance, etc.)")
