# 🚀 Deploying to Render

## Step 1: Prepare Your Local Setup

### 1a. Get Your Credentials
1. **API_ID & API_HASH** → https://my.telegram.org/apps
   - Login with your Telegram account
   - Create or view your app
   - Copy the `api_id` and `api_hash`

2. **BOT_TOKEN** → Message @BotFather on Telegram
   - Send `/newbot`
   - Follow the prompts
   - Copy your bot token

3. **SESSION** → Run locally to generate
   ```bash
   # On your iPad/computer
   python generate_session.py
   ```
   - Enter API_ID
   - Enter API_HASH
   - Enter your Telegram phone number (with country code: +1234567890)
   - Complete 2FA if prompted
   - Copy the output SESSION string

### 1b. Create .env File (Local Only)
Copy `.env.example` to `.env` and fill in your values:
```
API_ID=your_api_id_here
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
SESSION=your_session_string_here
```

**⚠️ NEVER commit .env to GitHub** - `.gitignore` protects it

---

## Step 2: Push to GitHub

```bash
git add .
git commit -m "Setup: Add Flask server and environment configuration"
git push origin master
```

---

## Step 3: Deploy to Render

### 3a. Create New Web Service
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository `SaveRestrictedContentBot`
4. Choose branch: `master`
5. Fill in:
   - **Name:** `save-restricted-bot` (or any name)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python -m main`
   - **Plan:** Free (or Starter if budget allows)

### 3b. Add Environment Variables
In Render dashboard:
1. Go to your service → "Environment"
2. Add these variables:
   ```
   API_ID=<your_api_id>
   API_HASH=<your_api_hash>
   BOT_TOKEN=<your_bot_token>
   SESSION=<your_session_string>
   FORCESUB=<optional>
   AUTH=<optional>
   PORT=8080
   ```
3. Click "Deploy"

### 3c. Wait for Deployment
- Render will build and start your bot
- Check the logs for any errors
- Bot should show "Successfully deployed!" message

---

## Step 4: Monitoring

After deployment:
1. Go to Render dashboard
2. Click your service
3. Watch the "Logs" tab for output
4. You should see:
   - "Server started on port 8080"
   - "Successfully deployed!"
   - "By MaheshChauhan • DroneBots"

The bot will now stay online 24/7! ✅

---

## Troubleshooting Common Errors

### ❌ "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure `flask` is in `requirements.txt` (already done ✅)

### ❌ "Missing environment variable"
**Solution:** Check all variables are added in Render → Environment

### ❌ "Userbot Error ! Have you added SESSION while deploying??"
**Solution:** Your SESSION string is missing or incorrect
- Run `generate_session.py` again locally
- Copy entire output string to SESSION variable in Render

### ❌ "Port already in use"
**Solution:** Render auto-assigns ports, should work automatically

### ❌ Bot goes offline after 15 minutes
**Solution:** This is already fixed with the Flask server in this update ✅

---

## After Deployment

Your bot is now:
- ✅ Running 24/7 on Render
- ✅ Has HTTP server on port 8080 (keeps it alive)
- ✅ Listening for Telegram messages
- ✅ Can save restricted content with custom thumbnails

Test it by messaging your bot on Telegram!
