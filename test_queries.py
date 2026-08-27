from database.queries import (
    get_all_careers,
    get_career,
    get_required_skills,
    get_courses_for_career,
    get_projects_for_career,
    get_related_careers,
    get_career_path
)

career = "Data Scientist"

print("\n=== ALL CAREERS ===")
print(get_all_careers())

print("\n=== CAREER ===")
print(get_career(career))

print("\n=== REQUIRED SKILLS ===")
print(get_required_skills(career))

print("\n=== COURSES ===")
print(get_courses_for_career(career))

print("\n=== PROJECTS ===")
print(get_projects_for_career(career))

print("\n=== RELATED CAREERS ===")
print(get_related_careers(career))

print("\n=== CAREER PATH ===")
print(get_career_path(career))