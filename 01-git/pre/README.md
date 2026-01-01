# Pre-work: Getting Ready for Git

Before our first session, please make sure you have the following set up. This is **mandatory** for the class.

## 1. Create a GitHub Account

GitHub is where your code will live in the cloud. You need an account to collaborate.

1. Go to [github.com](https://github.com/).
2. Click **Sign Up**.
3. Enter your email (preferably your university email for Student Developer Pack perks) and create a password.
4. Choose a username (professional usernames recommended!).
5. Verify your account via email.

## 2. Install Git Locally

Git is the engine that runs version control on your machine.

### Windows

1. Download **Git for Windows** from [git-scm.com/download/win](https://git-scm.com/download/win).
2. Run the installer. **Important**: When asked about "Adjusting your PATH environment", select "Git from the command line and also from 3rd-party software".
3. Keep other defaults unless you know what you are doing.
4. Open **Git Bash** (a new terminal installed with Git) and type `git --version` to verify.

### Mac

1. Open your Terminal (Command + Space, type "Terminal").
2. Check if git is installed:
   ```bash
   git --version
   ```
3. If not installed, it might prompt you to install XCode Command Line Tools. Say yes.
4. Alternatively, if you have Homebrew installed:
   ```bash
   brew install git
   ```

### Linux

1. Ubuntu/Debian: `sudo apt-get install git`
2. Fedora: `sudo dnf install git`

## 3. Configure Git (Crucial Step!)

Once Git is installed, you must tell it who you are. Open your terminal (Git Bash on Windows) and run these two commands:

```bash
git config --global user.name "Your Actual Name"
git config --global user.email "your.email@example.com"
```

_Note: Use the same email you used for your GitHub account._

## 4. Install VS Code

Our recommended code editor.

- [Download VS Code](https://code.visualstudio.com/)

## 📺 Watch (Optional but Recommended)

- **What is Git?** (5 mins): [Git & GitHub Crash Course](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
- **Git vs GitHub**: Understand that Git is the tool on your computer, and GitHub is the website.
