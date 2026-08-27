from flask import Flask, render_template, request, jsonify

from database.queries import (
    get_all_careers,
    get_career,
    get_required_skills,
    get_courses_for_career,
    get_projects_for_career,
    get_related_careers,
    get_career_path,
    get_career_graph
)
app = Flask(__name__)


@app.route("/")
def home():
    try:
        careers = get_all_careers()
        return render_template("index.html", careers=careers)
    except Exception as e:
        return render_template(
            "error.html",
            error="Unable to connect to the database."
        ), 503


@app.route("/career/<career_name>")
def career(career_name):
    try:
        career_data = get_career(career_name)

        if not career_data:
            return render_template(
                "error.html",
                error="Career not found."
            ), 404

        skills = get_required_skills(career_name)
        courses = get_courses_for_career(career_name)
        projects = get_projects_for_career(career_name)
        related = get_related_careers(career_name)
        career_paths = get_career_path(career_name)

        return render_template(
            "career.html",
            career=career_data,
            skills=skills,
            courses=courses,
            projects=projects,
            related=related,
            career_paths=career_paths
        )

    except Exception:
        return render_template(
            "error.html",
            error="Something went wrong while loading this career."
        ), 503


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "error.html",
        error="The requested page was not found."
    ), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template(
        "error.html",
        error="An unexpected error occurred."
    ), 500

@app.route("/api/career/<career_name>/graph")
def career_graph_api(career_name):
    try:
        graph_data = get_career_graph(career_name)

        return jsonify(graph_data)

    except Exception as e:
        return jsonify({
            "error": "Unable to load graph data."
        }), 503
if __name__ == "__main__":
    app.run(debug=True)