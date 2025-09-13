# 🌍 Global Quotes App

Small, deployable full-stack project to showcase developer skills:
- **Backend:** Python + Flask API serving random quotes
- **Frontend:** Static HTML + JS that consumes the API
- **Deployable** on Render / Heroku / any Python host for backend; GitHub Pages or any static host for frontend.

## What I prepared for you (Step 1 deliverable)
I packaged the entire project so you can **download and upload it to GitHub** in one go. After you upload, tell me and I'll walk you through deployment (backend + frontend) step-by-step.

## Files included
- `backend/app.py` — Flask app (endpoint: `/quote`)
- `frontend/index.html` — Static UI
- `frontend/script.js` — JS that calls the API (edit BACKEND_URL after deploy)
- `requirements.txt` — Python dependencies
- `Procfile` — for Heroku/Gunicorn
- `.gitignore` — common ignores
- `README.md` — this file

## Quick local test (optional)
1. Install Python 3.8+ and create a virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows (PowerShell)
   pip install -r requirements.txt
   python backend/app.py
   ```
2. Open `frontend/index.html` in your browser. Edit `frontend/script.js` to use `http://localhost:5000` for `BACKEND_URL` if testing locally.

## Step 1 — Upload to GitHub (detailed)
Follow these exact steps **to upload the project to GitHub**. I assume you either already have a GitHub account or will create one.

1. **Download the ZIP** (I gave you a ZIP file with this repo).
2. Unzip the file on your computer so you have the `global-quotes-app` folder.
3. If you don't have a GitHub account, go to https://github.com and sign up (choose a username you like; verify your email).
4. On GitHub (after login), click the **+** icon top-right and select **New repository**.
   - Repository name: `global-quotes-app`
   - Description: `Full-stack demo: Flask API + static frontend`
   - **Public**
   - Do NOT initialize with a README (we already have one). Click **Create repository**.
5. On the new repo page, click **Add file → Upload files**.
6. Drag-and-drop the entire contents of the `global-quotes-app` folder (both `backend/` and `frontend/`, and the other files).
7. Wait for the upload to finish, then at the bottom enter commit message: `Initial project upload: Global Quotes App` and click **Commit changes**.
8. You should now see your files in the repository.

✅ When you're done upload, come back and tell me **"step1 done"** (or just "uploaded"). I'll then walk you through **Step 2: Deploy the backend to Render (free) and connect the frontend** so the app goes live.

## Notes / Safety
- All example code is purely demo; there is no private or sensitive data.
- If you prefer, I can also give you exact command-line Git commands instead of the web UI. Tell me which you prefer.

---
Good job — once you upload, tell me and we'll deploy the backend and finish the app.
