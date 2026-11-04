# Website Setup Guide

This guide sets up two one-page business websites, both hosted free on GitHub Pages, both using the same booking calendar:

- **Textile site**: `textile-site` (embroidery and textile art)
- **Tech site**: `tech-site` (small business and design services)

Work through Part 1 once, then repeat Parts 3 to 6 for each site.

---

## Part 0: What you need

- A computer (Mac is fine) with an internet connection
- A **GitHub account** (free): https://github.com/signup
- A **Google account** (free) that holds the calendar you use for appointments
- **Python 3.9 or newer**
- **Git**
- **GitHub Desktop** (optional, but recommended if you're not comfortable with the terminal): https://desktop.github.com

### Check Python and Git

Open Terminal (Applications → Utilities → Terminal) and run:

```bash
python3 --version
git --version
```

If Python is missing, install it from https://www.python.org/downloads/. If Git is missing, running `git --version` on a Mac will offer to install the developer tools; accept.

---

## Part 1: Create your booking calendar (once, shared by both sites)

Both websites will use the same Google Calendar booking page, so a slot booked on one site disappears on the other.

1. Go to https://calendar.google.com and sign in.
2. Click the **+** next to "Create" or the **Create** button, then choose **Appointment schedule**.
   - If you don't see this option, search Google Calendar's help for "appointment schedules" to confirm your account type supports it.
3. Give it a name, for example "Consultations".
4. Set your **booking page** details:
   - **Duration:** how long each appointment lasts (for example, 60 minutes)
   - **Availability:** the days and hours you're open
   - **Buffer time:** time between appointments so you aren't back-to-back
   - **Booking form:** ask for name, email, and a short note about the project
5. Save the schedule.
6. Open the schedule and find the **share** or **embed** option. Copy the **booking page link**. It looks like `https://calendar.google.com/calendar/appointments/schedules/...`.
7. Test it: open the link in a private browser window, book a fake appointment, and confirm the slot disappears when you check it again. Then cancel the test booking in your calendar.

Keep this link. You'll paste it into both config files.

**Embed check:** Some booking pages refuse to show inside another website. Once your site is live, look at the "Book a time" panel. If it's blank or shows an error, tell me and I'll change the template to show a "Book now" button that opens the booking page in a new tab.

---

## Part 2: Set up your project folder (once)

1. Create a folder for your work, for example `Documents/websites/`.
2. Copy the `website-template` folder into it. You should now have `Documents/websites/website-template/` containing:

```
website-template/
  build.py              the build script
  requirements.txt      the Python packages it needs
  templates/index.html  the page layout
  static/style.css      colors, fonts, and borders
  posts/                your blog posts
  configs/              one config file per site
  docs/                 created when you build (this is the website)
```

3. Install the Python packages. In Terminal, go into the folder:

```bash
cd ~/Documents/websites/website-template
pip3 install -r requirements.txt --break-system-packages
```

The `--break-system-packages` flag is needed on newer Macs. If you see "command not found" for `pip3`, use `python3 -m pip install -r requirements.txt --break-system-packages` instead.

---

## Part 3: Set up the textile site

### 3a. Make a copy for this site

Duplicate the template folder so each site has its own copy. In Terminal:

```bash
cd ~/Documents/websites
cp -r website-template textile-site
cd textile-site
```

### 3b. Edit the configuration

Open `configs/textile.json` in any text editor (TextEdit works, but set it to plain text: Format → Make Plain Text). Replace every `PLACEHOLDER` with your real content:

| Field | What to put |
|---|---|
| `business_name` | Your business name as customers know it |
| `tagline` | One short line under the name |
| `url` | `https://YOUR-GITHUB-USERNAME.github.io/textile-site/` (see Part 5) |
| `location` | City and state, for example "Rochester, NY" |
| `contact_email` | The email people should use |
| `meta_description` | One sentence, around 120 to 155 characters. Shown in Google search results |
| `keywords` | Five to ten comma-separated terms people would search, for example "embroidery, custom embroidery, hoop art, textile art" |
| `bio` | Two or three sentences about you |
| `booking_embed_url` | The booking link from Part 1 |
| `services` | Three services, each with a `name` and `description` |

**Keep the JSON valid.** Every text value stays inside double quotes, and commas go between items but not after the last one. Don't delete the quotation marks or braces. If a build fails with a message mentioning "JSON" or "Expecting", check for a missing comma or quote near the line it names. Online checker: https://jsonlint.com

**Where the blog file lives:** Your posts are in `posts/`. The configuration for the textile site doesn't point to a separate folder, so both sites use their own `posts/` folder.

### 3c. Replace the placeholder post

Open `posts/2026-10-first-post.md` and replace the placeholders. Keep the three lines between the `---` markers:

```
---
title: Your post title
date: 2026-10-01
excerpt: One or two sentences shown on the homepage.
---

Your post body. Blank lines separate paragraphs. **Bold** and *italic* work.
```

- The `date` must be in `YYYY-MM-DD` format. The post with the newest date is the one shown.
- To add another post, copy the file, give it a new name (for example `2026-11-05-hoop-colors.md`), and change its title, date, excerpt, and body.

### 3d. Build the site

```bash
python3 build.py configs/textile.json
```

You should see: `Built .../docs/index.html from textile.json`

To see the result, open `docs/index.html` in your browser by double-clicking it in Finder. The layout appears; the blog post and services display. Note that the booking panel may not load until the site is live on GitHub.

---

## Part 4: Set up the tech site

Repeat Part 3 with these differences:

```bash
cd ~/Documents/websites
cp -r website-template tech-site
cd tech-site
```

Edit `configs/tech.json` instead. Its URL should end in `/tech-site/`. Write new posts in the `posts/` folder of this copy. Then build:

```bash
python3 build.py configs/tech.json
```

Each site has its own `posts/` folder, so the textile and tech blogs stay separate. Posts you write for one site won't appear on the other.

---

## Part 5: Publish to GitHub Pages

Do this for each site. Start with the textile site.

### 5a. Create the repository on GitHub

1. Sign in to https://github.com.
2. Click **+** (top right) → **New repository**.
3. Repository name: `textile-site` (must match the folder name and the URL in your config).
4. Choose **Public**. GitHub Pages is free for public repositories.
5. Leave "Add a README" and other options unchecked. Click **Create repository**.

Your GitHub username will appear in the address: `https://github.com/YOUR-USERNAME/textile-site`. Your site will live at `https://YOUR-USERNAME.github.io/textile-site/`.

### 5b. Upload your files

**Option A: GitHub Desktop (easier)**

1. Open GitHub Desktop and sign in.
2. File → **Add local repository** → choose your `textile-site` folder. If it asks to create a repository, accept.
3. In the "Changes" list, check that you see your files. If you see a huge list including `__pycache__`, see Part 7.
4. Write a summary such as "First version", then click **Commit to main**.
5. Click **Publish repository**. Keep "Keep this code private" unchecked, then publish.

**Option B: Terminal**

```bash
cd ~/Documents/websites/textile-site
git init
git add .
git commit -m "First version"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/textile-site.git
git push -u origin main
```

Git may ask you to sign in. Use a GitHub personal access token as the password, or use GitHub Desktop's sign-in, which handles this for you.

### 5c. Turn on GitHub Pages

1. On your repository's GitHub page, click **Settings** (top tab).
2. In the left sidebar, click **Pages**.
3. Under "Build and deployment," set **Source** to **Deploy from a branch**.
4. Set **Branch** to `main` and the folder to **/docs**. Click **Save**.
5. Wait one to three minutes. Refresh the Pages page; it will show your live address.

Visit `https://YOUR-USERNAME.github.io/textile-site/`. If you see the page, the site is live.

**Important:** The website is the `docs` folder. That's why the folder setting must be `/docs`. The `build.py` script writes into `docs/` every time you run it.

---

## Part 6: Updating your site

Every change follows the same routine:

1. Edit a config file, a post, or the style or layout.
2. Build from Terminal:
   ```bash
   cd ~/Documents/websites/textile-site
   python3 build.py configs/textile.json
   ```
3. Publish the change:
   - **GitHub Desktop:** write a summary, click **Commit to main**, then **Push origin**.
   - **Terminal:** `git add . && git commit -m "Update" && git push`
4. Wait about a minute, then refresh the live site. Try a hard refresh (Command+Shift+R) if you still see the old version.

**Adding a blog post:** create a new `.md` file in `posts/`, build, and push.

**Changing the look:** edit the colors at the top of `static/style.css`, then build and push.

**Changing the layout:** edit `templates/index.html`, then build and push. Make one change at a time, so it's easy to undo if something breaks.

---

## Part 7: Things that go wrong, and fixes

**"command not found: python3" or "pip3"**
Install Python from python.org. Restart Terminal afterward.

**"ModuleNotFoundError: No module named jinja2" or "markdown"**
Run the install step from Part 2 again.

**"JSONDecodeError" or "Expecting ',' delimiter"**
There's a typo in the config file. Check for a missing comma, a missing quotation mark, or a comma after the last item in a list.

**Build works but the live site shows an old version**
Did you commit and push after building? The build only changes the files on your computer. GitHub only sees what you push. Also check that Pages is set to `main` and `/docs`.

**The booking calendar is blank**
Check that `booking_embed_url` in the config is the full link (starts with `https://`). Rebuild and push. If it's still blank, the calendar page doesn't allow embedding; tell me and I'll switch to a button.

**GitHub shows a 404 page**
Check the repository name matches the URL in your config, and that Pages is enabled on the `main` branch in the `/docs` folder.

**GitHub Desktop lists a huge number of changed files, including `__pycache__`**
Create a file named `.gitignore` in the project folder (in a text editor, plain text, no extension beyond `.gitignore`) containing:

```
__pycache__/
*.pyc
```

Then commit again.

**Styles or images look broken on the live site**
The style file is linked as `static/style.css`. Make sure the `static` folder was copied and pushed. It's created inside `docs/` when you build.

---

## Part 8: Checklist before you announce the site

- [ ] Every `PLACEHOLDER` is replaced in both config files, and no placeholder text appears on the live pages
- [ ] The `url` in each config matches the live GitHub Pages address
- [ ] The booking panel displays and a test booking removes the slot on both sites
- [ ] The blog panel shows your newest post and the "Read the post" link opens it
- [ ] The page looks right on a phone (open it on your phone or press Option+Command+I in Chrome and choose a phone view)
- [ ] Search results: wait a week or two, then search `site:YOUR-USERNAME.github.io/textile-site` in Google to confirm it's indexed. To speed this up, go to https://search.google.com/search-console, add the site as a property, and submit the `sitemap.xml` file
- [ ] Test the share preview: paste the site link into Facebook's Sharing Debugger (https://developers.facebook.com/tools/debug/) to confirm the title and description appear

---

## Part 9: Using a custom domain later

When you buy a domain (for example, from Namecheap or Google Domains' successor, Squarespace Domains), follow GitHub's guide "Managing a custom domain for your GitHub Pages site" in the repository's Pages settings. Then update the `url` in the config to your new domain and rebuild.

---

## Quick reference

| Task | Command |
|---|---|
| Build textile site | `python3 build.py configs/textile.json` |
| Build tech site | `python3 build.py configs/tech.json` |
| Publish (Terminal) | `git add . && git commit -m "Update" && git push` |
| Textile live address | `https://YOUR-USERNAME.github.io/textile-site/` |
| Tech live address | `https://YOUR-USERNAME.github.io/tech-site/` |
