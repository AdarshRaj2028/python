# r stands for "raw" string, which means backslashes are treated literally.
r"""
=============================================================================
PYTHON VIRTUAL ENVIRONMENTS - COMPLETE GUIDE
=============================================================================

WHAT IS A VIRTUAL ENVIRONMENT?
------------------------------
A virtual environment is a self-contained directory that maintains separate 
and isolated environments for Python projects. These are simply directories 
on your system that can be placed in logical locations, typically alongside 
the Python projects that require them.

BENEFITS:
---------
- Manage Dependencies: Keep project requirements separate
- Python Versions: Use different Python versions per project  
- Python Packages: Avoid conflicts between project requirements
- Each project has its own set of installed packages, independent of 
  global installations or other environments

=============================================================================
MAC/LINUX SETUP
=============================================================================

# 1. Navigate to your project directory
cd /path/to/your/project

# 2. Create virtual environment
python3 -m venv env

# Command breakdown:
# python3 = Python interpreter
# -m = "run module as script" flag
# venv = the virtual environment creator module
# env = name of your virtual environment (convention)

# 3. Activate the virtual environment
source env/bin/activate
# Your prompt will change to show (env) indicating active environment

# 4. Install packages as needed
pip3 install package_name

# 5. View installed packages
pip3 list

# 6. Deactivate when finished
deactivate

=============================================================================
WINDOWS SETUP
=============================================================================

# 1. Navigate to your project directory (CMD or PowerShell)
cd C:\path\to\your\project  

# 2. Create virtual environment
python -m venv env

# Command breakdown:
# python = Python interpreter (Windows uses 'python' not 'python3')
# -m = "run module as script" flag
# venv = the virtual environment creator module
# env = name of your virtual environment (convention)

# 3. Activate the virtual environment
env\Scripts\activate.bat
# OR if .bat doesn't work:
env\Scripts\activate

# Your prompt will change to show (env) indicating active environment

# 4. Install packages as needed
pip install package_name

# 5. View installed packages
pip list

# 6. Deactivate when finished
deactivate

=============================================================================
SHARING PROJECTS - REQUIREMENTS FILE
=============================================================================

CREATING REQUIREMENTS FILE:
---------------------------
# Generate requirements.txt with all installed packages and versions
pip freeze > requirements.txt

# View the contents (optional)
nano requirements.txt    # Linux/Mac
type requirements.txt    # Windows

# The file will contain packages in format:
# package-name==version.number
# another-package==version.number

INSTALLING FROM REQUIREMENTS FILE:
----------------------------------
# 1. Create and activate new virtual environment first
python -m venv env
source env/bin/activate     # Mac/Linux
# OR
env\Scripts\activate        # Windows

# 2. Install all packages from requirements.txt
pip install -r requirements.txt

# Command breakdown:
# -r = install from requirements file
# requirements.txt = file containing package dependencies

=============================================================================
BEST PRACTICES
=============================================================================

DIRECTORY STRUCTURE:
-------------------
your-project/
├── env/                 # Virtual environment directory
├── requirements.txt     # Dependencies list
├── main.py             # Your Python code
└── README.md           # Project documentation

IMPORTANT REMINDERS:
-------------------
- Always activate your virtual environment before working on a project
- Add 'env/' to .gitignore when using version control
- Use 'pip freeze' regularly to keep requirements.txt updated
- Each project should have its own virtual environment
- Common naming conventions: env, venv, myproject-env
- Never commit the virtual environment directory to version control
- This workflow ensures reproducible environments and prevents conflicts

=============================================================================
QUICK REFERENCE COMMANDS
=============================================================================

CREATE:     python3 -m venv env        (Mac/Linux)
            python -m venv env          (Windows)

ACTIVATE:   source env/bin/activate     (Mac/Linux)
            env\Scripts\activate        (Windows)

DEACTIVATE: deactivate                  (All platforms)

FREEZE:     pip freeze > requirements.txt
INSTALL:    pip install -r requirements.txt

LIST:       pip3 list                   (Mac/Linux)
            pip list                    (Windows)



=============================================================================
POWERSHELL EXECUTION POLICY - VIRTUAL ENVIRONMENT SETUP
=============================================================================

WHAT IS EXECUTION POLICY?
-------------------------
PowerShell execution policy is a Windows security feature that controls 
which scripts can run on your system. By default, Windows sets this to 
"Restricted" which blocks ALL PowerShell scripts, including virtual 
environment activation scripts.

THE PROBLEM:
-----------
When trying to activate a virtual environment in PowerShell:
.\venv\Scripts\Activate.ps1

You get this error:
"File cannot be loaded because running scripts is disabled on this system"
"PSSecurityException: UnauthorizedAccess"

This happens because Activate.ps1 is a PowerShell script, and Windows 
blocks it for security reasons.

=============================================================================
SOLUTION: SET EXECUTION POLICY
=============================================================================

RECOMMENDED FIX (Current User Only):
-----------------------------------
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# When prompted, type 'Y' and press Enter
# This only affects your user account, not the entire system

ALTERNATIVE FIX (System-wide - Requires Admin):
----------------------------------------------
# Right-click PowerShell -> "Run as Administrator"
Set-ExecutionPolicy RemoteSigned
# Type 'Y' when prompted

ONE-TIME BYPASS (Temporary):
---------------------------
powershell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
# This bypasses the policy for just this one command

=============================================================================
UNDERSTANDING EXECUTION POLICIES
=============================================================================

RESTRICTED (Default):
--------------------
- No PowerShell scripts can run
- Blocks virtual environment activation
- Maximum security but prevents development work

REMOTESIGNED (Recommended):
--------------------------
- Local scripts (your venv) can run without digital signatures
- Downloaded scripts from internet must be digitally signed
- Perfect balance of security and functionality
- Allows development while protecting from malicious downloads

UNRESTRICTED:
------------
- All scripts can run regardless of source
- Less secure but maximum flexibility
- Not recommended for general use

BYPASS:
-------
- No restrictions or warnings
- Used for temporary situations
- Not recommended as permanent setting

=============================================================================
VERIFICATION COMMANDS
=============================================================================

CHECK CURRENT POLICY:
--------------------
Get-ExecutionPolicy
# Shows current policy (Restricted, RemoteSigned, etc.)

CHECK POLICY FOR DIFFERENT SCOPES:
---------------------------------
Get-ExecutionPolicy -List
# Shows policy for CurrentUser, LocalMachine, etc.

TEST VIRTUAL ENVIRONMENT AFTER FIX:
----------------------------------
.\venv\Scripts\Activate.ps1    # Should work now
python -c "import sys; print(sys.executable)"  # Verify activation
deactivate                     # Exit virtual environment

=============================================================================
WHY THIS HAPPENS
=============================================================================

SECURITY DESIGN:
---------------
- Windows assumes downloaded scripts could be malicious
- PowerShell scripts can access system resources
- Default "Restricted" policy prevents accidental script execution
- Virtual environment activation is caught in this security net

DEVELOPMENT IMPACT:
------------------
- Affects Python virtual environments
- Impacts automation scripts
- Blocks legitimate development tools
- Requires one-time configuration for development work

=============================================================================
BEST PRACTICES
=============================================================================

FOR DEVELOPMENT MACHINES:
------------------------
- Use "RemoteSigned" policy with CurrentUser scope
- This allows your development work while maintaining security
- Only affects your user account, not other users

FOR PRODUCTION SERVERS:
----------------------
- Keep "Restricted" policy unless scripts are required
- Use signed scripts for production automation
- Consider "AllSigned" for maximum security with script capability

REMEMBER:
--------
- This is a ONE-TIME setup per user account
- Once set, all future virtual environments will activate normally
- The policy persists across PowerShell sessions
- You can always check current policy with Get-ExecutionPolicy

=============================================================================
TROUBLESHOOTING
=============================================================================

IF REMOTESIGNED DOESN'T WORK:
-----------------------------
1. Try running PowerShell as Administrator
2. Set policy system-wide: Set-ExecutionPolicy RemoteSigned
3. Restart PowerShell and try again

IF YOU STILL GET ERRORS:
-----------------------
1. Check if antivirus is blocking scripts
2. Verify the Activate.ps1 file exists in venv\Scripts\
3. Try the one-time bypass method as a test

ALTERNATIVE ACTIVATION METHODS:
------------------------------
venv\Scripts\activate.bat      # Uses batch file instead of PowerShell
cmd /c "venv\Scripts\activate.bat"  # Run through Command Prompt

=============================================================================

"""
