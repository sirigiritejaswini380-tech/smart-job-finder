from tkinter import *
from tkinter import ttk, messagebox
import webbrowser

# ---------------- WINDOW ----------------
root = Tk()
root.title("Smart Job Finder - MCA Mini Project")
root.geometry("900x780")
root.config(bg="#E8F5FF")

title = Label(root,
              text="SMART JOB FINDER",
              font=("Arial", 22, "bold"),
              bg="#0066CC",
              fg="white",
              pady=12)
title.pack(fill=X)

# ---------------- VARIABLES ----------------
name = StringVar()
skills = StringVar()
location = StringVar()
experience = StringVar()

recommended_job = ""

# ---------------- INPUT FRAME ----------------
frame = Frame(root, bg="#E8F5FF")
frame.pack(pady=15)

Label(frame, text="Name", bg="#E8F5FF",
      font=("Arial",11,"bold")).grid(row=0,column=0,padx=10,pady=8,sticky=W)

Entry(frame,textvariable=name,width=35).grid(row=0,column=1)

Label(frame,text="Skills (comma separated)",
      bg="#E8F5FF",
      font=("Arial",11,"bold")).grid(row=1,column=0,padx=10,pady=8,sticky=W)

Entry(frame,textvariable=skills,width=35).grid(row=1,column=1)

Label(frame,text="Preferred Location",
      bg="#E8F5FF",
      font=("Arial",11,"bold")).grid(row=2,column=0,padx=10,pady=8,sticky=W)

Entry(frame,textvariable=location,width=35).grid(row=2,column=1)

Label(frame,text="Experience Level",
      bg="#E8F5FF",
      font=("Arial",11,"bold")).grid(row=3,column=0,padx=10,pady=8,sticky=W)

experience_box = ttk.Combobox(frame,
                              textvariable=experience,
                              values=["Fresher","Intermediate","Experienced"],
                              width=32)

experience_box.grid(row=3,column=1)
experience_box.current(0)

# ---------------- OUTPUT ----------------
output = Text(root,width=100,height=20,font=("Arial",10))
output.pack(pady=15)

# ---------------- JOB DATA ----------------
jobs = {
    "python":("Python Developer","₹4-10 LPA",
              "Flask, Django, APIs, SQL"),

    "java":("Java Developer","₹5-12 LPA",
            "Spring Boot, MySQL, REST API"),

    "html":("Frontend Developer","₹3-8 LPA",
            "HTML, CSS, JavaScript, Bootstrap"),

    "javascript":("Frontend Developer","₹3-8 LPA",
            "HTML, CSS, JavaScript, React"),

    "react":("React Developer","₹5-10 LPA",
             "React, JavaScript, CSS"),

    "sql":("Database Administrator","₹4-9 LPA",
           "Oracle, MySQL, MongoDB"),

    "aws":("Cloud Engineer","₹7-18 LPA",
           "AWS, Docker, Kubernetes"),

    "azure":("Azure Cloud Engineer","₹7-18 LPA",
             "Azure, DevOps, Networking"),

    "machine learning":("Machine Learning Engineer","₹8-20 LPA",
                        "Python, TensorFlow, Scikit-Learn"),

    "ai":("AI Engineer","₹8-22 LPA",
          "Python, Deep Learning, TensorFlow"),

    "cybersecurity":("Cyber Security Analyst","₹6-15 LPA",
                     "Linux, Networking, CEH"),

    "networking":("Network Engineer","₹4-10 LPA",
                  "CCNA, Routers, Switches"),

    "docker":("DevOps Engineer","₹8-20 LPA",
              "Docker, Kubernetes, Jenkins"),

    "figma":("UI/UX Designer","₹4-8 LPA",
             "Figma, Adobe XD"),

    "android":("Android Developer","₹5-12 LPA",
               "Java, Kotlin, Firebase")
}

# ---------------- ANALYZE ----------------
def find_job():
    global recommended_job

    output.delete(1.0,END)

    user_skills = [x.strip().lower() for x in skills.get().split(",")]

    output.insert(END,"SMART JOB ANALYSIS REPORT\n")
    output.insert(END,"="*70+"\n\n")

    output.insert(END,f"Name : {name.get()}\n")
    output.insert(END,f"Location : {location.get()}\n")
    output.insert(END,f"Experience : {experience.get()}\n\n")

    found=False

    for skill in user_skills:
        if skill in jobs:

            found=True

            job,salary,need = jobs[skill]
            recommended_job = job

            output.insert(END,f"Recommended Job : {job}\n")
            output.insert(END,f"Estimated Salary : {salary}\n")
            output.insert(END,f"Important Skills : {need}\n")

            if experience.get()=="Fresher":
                output.insert(END,"Experience Suggestion : Apply for internships and entry-level jobs.\n")

            elif experience.get()=="Intermediate":
                output.insert(END,"Experience Suggestion : Apply for Associate Developer positions.\n")

            else:
                output.insert(END,"Experience Suggestion : Apply for Senior/Lead positions.\n")

            output.insert(END,"\n")
            output.insert(END,"-"*70+"\n\n")

    if not found:
        recommended_job="Software Developer"
        output.insert(END,"No direct job matched.\n\n")
        output.insert(END,"Suggested Career : Software Developer\n")
        output.insert(END,"Learn Python, Java, SQL, HTML, CSS and Cloud Computing.\n")

# ---------------- GOOGLE FUNCTIONS ----------------
def google_jobs():
    webbrowser.open(
        f"https://www.google.com/search?q={recommended_job}+jobs+in+{location.get()}")

def google_courses():
    webbrowser.open(
        f"https://www.google.com/search?q={recommended_job}+online+courses")

def google_internships():
    webbrowser.open(
        f"https://www.google.com/search?q={recommended_job}+internship+in+{location.get()}")

def google_interview():
    webbrowser.open(
        f"https://www.google.com/search?q={recommended_job}+interview+questions")

# ---------------- BUTTONS ----------------
Button(root,text="Find Best Job",
       command=find_job,
       bg="green",
       fg="white",
       font=("Arial",12,"bold"),
       width=25).pack(pady=5)

Button(root,text="Google Jobs",
       command=google_jobs,
       bg="#4285F4",
       fg="white",
       width=25).pack(pady=5)

Button(root,text="Google Courses",
       command=google_courses,
       bg="#34A853",
       fg="white",
       width=25).pack(pady=5)

Button(root,text="Google Internship",
       command=google_internships,
       bg="#FBBC05",
       fg="black",
       width=25).pack(pady=5)

Button(root,text="Google Interview Questions",
       command=google_interview,
       bg="#EA4335",
       fg="white",
       width=25).pack(pady=5)

root.mainloop()