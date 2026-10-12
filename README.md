# Harish Kumar - AI & Python Developer Portfolio

A modern, high-performance, responsive personal portfolio website designed for **Harish Kumar**, B.Sc. Artificial Intelligence student at **Annai College of Arts and Science**.

Tailored for recruiters, internship applications, entry-level AI/Python developer roles, and college project presentations.

---

## 🚀 Running the Portfolio Web Application

The portfolio includes a **Python Flask backend** ([main.py](file:///c:/Users/kumar/OneDrive/Desktop/Portfolio/main.py)) that serves the web application and handles interactive backend capabilities:

### Start the Server:
```bash
python main.py
```
* The server will launch at: **`http://localhost:5000`** (or `http://127.0.0.1:5000`)
* You can change the port anytime: `python main.py 8080`

### Interactive Backend Capabilities:
1. **Live File Uploads (`/api/upload`)**:
   - Recruiters or visitors can click **"Live Demo"** on the **ATS Resume Analyzer** project card and upload resume files (`.pdf`, `.docx`, `.txt`).
   - Uploaded files are safely stored in the `uploads/` directory, and real-time parsing insights and skill matches are returned.
2. **Contact Message Storage (`/api/contact`)**:
   - Messages sent through the contact form are stored in `data/messages.json` with timestamp, sender details, and IP address.
3. **Resume Download (`/download-resume`)**:
   - Direct download endpoint serving `assets/Harish_Kumar_Resume.pdf`.

---

## 📁 Project Structure

```
Portfolio/
├── main.py                     # Python Flask server & API backend
├── index.html                  # Main portfolio webpage (10 complete sections)
├── data/
│   └── messages.json           # Stored incoming contact form messages
├── uploads/                    # Stored resume & document uploads (ATS analyzer)
├── css/
│   ├── style.css               # Design system, responsive layout, glassmorphic styling
│   └── animations.css          # Keyframes, glow effects, Intersection Observer reveals
├── js/
│   └── main.js                 # Mobile drawer, scrollspy, modal preview, file upload & contact APIs
├── assets/
│   ├── Harish_Kumar_Resume.pdf # Placeholder resume PDF
│   └── images/
│       ├── avatar.jpg          # Profile illustration / avatar
│       ├── project-ats.jpg     # ATS Resume Analyzer project preview
│       ├── project-mnist.jpg   # MNIST Digit Classification project preview
│       └── project-nlp.jpg     # 3rd AI/ML project preview
└── README.md                   # Documentation & customization guide
```

---

## 🎨 Design & Aesthetic Highlights

- **Dark Tech Theme**: Cyber slate and deep midnight background (`#07090e`, `#0d111a`) with electric cyan (`#38bdf8`) and violet purple (`#a855f7`) accents.
- **Glassmorphism**: Subtle backdrop blur (`16px`) and translucent borders on cards and navigation bar.
- **No Fake Percentages**: Skill proficiencies are categorized with high-tech badge pills and icons instead of arbitrary percentage bars.
- **Micro-Animations**: Smooth Intersection Observer scroll reveals, floating badges, and dynamic role typewriter effect.
- **Responsive**: Fully optimized for mobile phones, tablets, laptops, and ultra-wide displays.
- **Accessibility & SEO**: Clean semantic tags, Open Graph meta tags, Schema.org `Person` JSON-LD structured data.

---

## 📝 How to Customize Your Details

Search for `[Placeholder]` in `index.html` to quickly customize any missing resume details:

1. **Education Marks / Year**:
   - Locate the `<section id="education">` block in `index.html`.
   - Update `[2023 - 2026 / Expected]` and `[CGPA / Percentage Placeholder]`.

2. **Resume PDF**:
   - Replace `assets/Harish_Kumar_Resume.pdf` with your real resume file using the exact same filename.

3. **Project Links**:
   - In `<section id="projects">`, replace `https://github.com/yourusername/...` with your real GitHub repository and demo URLs.

4. **Certifications**:
   - In `<section id="certifications">`, update the course titles, issuing organizations (e.g. Coursera, NPTEL, Infosys Springboard), and credential links.

5. **Contact Details & Social Media**:
   - In `<section id="contact">` and `<footer class="site-footer">`, update:
     - Email: `harish.kumar.dev@example.com`
     - Phone: `+91 98765 43210`
     - LinkedIn: `https://linkedin.com/in/harish-kumar-ai`
     - GitHub: `https://github.com/harish-kumar-ai`

---

## 🌐 Free 1-Click Deployment

### Deploy to GitHub Pages
1. Push this directory to a GitHub repository named `portfolio` or `<your-username>.github.io`.
2. Go to **Settings** > **Pages** in GitHub.
3. Under **Branch**, select `main` and root `/`, then click **Save**.
4. Your website is live worldwide at `https://<your-username>.github.io`!

### Deploy to Vercel / Netlify
- Drag and drop the `Portfolio` folder directly into [Vercel](https://vercel.com) or [Netlify](https://netlify.com) for instant SSL-secured hosting.

---

&copy; 2026 Harish Kumar. All Rights Reserved.
