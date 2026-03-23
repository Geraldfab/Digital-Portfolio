from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Portfolio Data - Edit this information as needed
PORTFOLIO_DATA = {
    # Personal Information
    "name": "Your Name",
    "title": "Full Stack Developer | Designer | Creative Professional",
    "tagline": "Building digital experiences that matter",
    "about": """
        I'm a passionate developer with expertise in creating beautiful, 
        functional web applications. With years of experience in the industry,
        I specialize in turning ideas into reality through clean code and 
        innovative solutions.
        
        My journey began with curiosity about how things work on the web,
        and it has evolved into a career dedicated to creating impactful
        digital experiences. I believe in continuous learning and staying
        updated with the latest technologies.
    """,
    
    # Contact Information
    "contact": {
        "email": "your.email@example.com",
        "phone": "+1 (555) 123-4567",
        "location": "San Francisco, CA",
        "website": "www.yourwebsite.com"
    },
    
    # Social Links
    "social": {
        "github": "https://github.com/yourusername",
        "linkedin": "https://linkedin.com/in/yourusername",
        "twitter": "https://twitter.com/yourusername",
        "instagram": "https://instagram.com/yourusername",
        "facebook": "https://facebook.com/yourusername"
    },
    
    # Skills
    "skills": [
        {"name": "Python", "level": 90, "category": "backend"},
        {"name": "JavaScript", "level": 85, "category": "frontend"},
        {"name": "React", "level": 80, "category": "frontend"},
        {"name": "Flask/Django", "level": 85, "category": "backend"},
        {"name": "HTML/CSS", "level": 95, "category": "frontend"},
        {"name": "SQL/Databases", "level": 80, "category": "backend"},
        {"name": "Git/Version Control", "level": 85, "category": "tools"},
        {"name": "Docker", "level": 70, "category": "tools"},
        {"name": "UI/UX Design", "level": 75, "category": "design"},
        {"name": "Cloud Services", "level": 70, "category": "tools"}
    ],
    
    # Experience
    "experience": [
        {
            "company": "Tech Company Inc.",
            "position": "Senior Developer",
            "duration": "2022 - Present",
            "description": "Leading development of cloud-based applications, mentoring junior developers, and implementing best practices for code quality and performance."
        },
        {
            "company": "StartupXYZ",
            "position": "Full Stack Developer",
            "duration": "2020 - 2022",
            "description": "Built and maintained multiple client websites, implemented REST APIs, and optimized database queries for better performance."
        },
        {
            "company": "Digital Agency Co.",
            "position": "Junior Developer",
            "duration": "2018 - 2020",
            "description": "Developed responsive websites, collaborated with design team, and learned modern web technologies."
        }
    ],
    
    # Education
    "education": [
        {
            "institution": "University of Technology",
            "degree": "Bachelor of Science in Computer Science",
            "duration": "2014 - 2018",
            "details": "Graduated with honors, specialized in Software Engineering"
        },
        {
            "institution": "Tech Academy",
            "degree": "Web Development Bootcamp",
            "duration": "2018",
            "details": "Intensive 12-week program focusing on modern web technologies"
        }
    ],
    
    # Projects
    "projects": [
        {
            "title": "E-Commerce Platform",
            "category": "Web Application",
            "description": "A full-featured online shopping platform with payment integration, inventory management, and admin dashboard.",
            "tech": ["Python", "Flask", "React", "PostgreSQL", "Stripe"],
            "github": "https://github.com/yourusername/ecommerce",
            "live": "https://ecommerce-demo.com",
            "image": "project1"
        },
        {
            "title": "Task Management App",
            "category": "Productivity Tool",
            "description": "Collaborative task management application with real-time updates, Kanban boards, and team collaboration features.",
            "tech": ["JavaScript", "Node.js", "MongoDB", "Socket.io"],
            "github": "https://github.com/yourusername/taskmanager",
            "live": "https://taskmanager-demo.com",
            "image": "project2"
        },
        {
            "title": "Portfolio Website Builder",
            "category": "SaaS Application",
            "description": "A platform that allows users to create beautiful portfolio websites with customizable templates and themes.",
            "tech": ["Python", "Django", "Vue.js", "AWS"],
            "github": "https://github.com/yourusername/portfolio-builder",
            "live": "https://portfolio-builder-demo.com",
            "image": "project3"
        },
        {
            "title": "Weather Dashboard",
            "category": "Web Application",
            "description": "Real-time weather tracking application with forecasts, interactive maps, and location-based alerts.",
            "tech": ["JavaScript", "React", "OpenWeather API", "Leaflet"],
            "github": "https://github.com/yourusername/weather-app",
            "live": "https://weather-demo.com",
            "image": "project4"
        }
    ],
    
    # Services
    "services": [
        {
            "title": "Web Development",
            "icon": "code",
            "description": "Custom websites and web applications built with modern technologies and best practices."
        },
        {
            "title": "UI/UX Design",
            "icon": "palette",
            "description": "User-centered design that combines aesthetics with functionality for optimal user experience."
        },
        {
            "title": "Consulting",
            "icon": "chart-line",
            "description": "Technical advice and guidance for your projects, from architecture to implementation."
        },
        {
            "title": "Maintenance",
            "icon": "cogs",
            "description": "Ongoing support and maintenance to keep your applications running smoothly."
        }
    ],
    
    # Testimonials
    "testimonials": [
        {
            "name": "John Smith",
            "position": "CEO, Tech Startup",
            "quote": "An exceptional developer who delivered our project on time and exceeded our expectations. The attention to detail and communication throughout the project was outstanding.",
            "image": "testimonial1"
        },
        {
            "name": "Sarah Johnson",
            "position": "Product Manager",
            "quote": "Working with this developer was a great experience. They understood our requirements perfectly and delivered a solution that helped our business grow.",
            "image": "testimonial2"
        },
        {
            "name": "Michael Brown",
            "position": "Founder, Design Agency",
            "quote": "Their technical skills combined with design sensibility resulted in a product that looks great and performs even better. Highly recommended!",
            "image": "testimonial3"
        }
    ],
    
    # Blog Posts (optional)
    "blog": [
        {
            "title": "Getting Started with Flask",
            "excerpt": "Learn how to build web applications with Flask, from setup to deployment.",
            "date": "January 15, 2024",
            "category": "Python",
            "url": "#"
        },
        {
            "title": "Best Practices for Web Development",
            "excerpt": "Essential tips and practices that every developer should know.",
            "date": "December 10, 2023",
            "category": "Development",
            "url": "#"
        }
    ],
    
    # Achievements
    "achievements": [
        "Best Developer Award 2023",
        "Published 20+ Open Source Projects",
        "500+ GitHub Contributions",
        "Speaker at Tech Conference 2022",
        "100% Project Success Rate"
    ],
    
    # Interests
    "interests": [
        "Open Source Development",
        "Machine Learning & AI",
        "Photography",
        "Travel & Exploration",
        "Reading & Learning",
        "Gaming"
    ]
}


@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)


@app.route('/api/data')
def api_data():
    return jsonify(PORTFOLIO_DATA)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)