#!/bin/bash

# ========================================
# GitHub Push Setup Script (Linux/Mac)
# Repository: Linkedin-job-trend-dashboard
# Username: princeraj026-code
# ========================================

echo ""
echo "========================================"
echo "GitHub Push Setup Script"
echo "Repository: Linkedin-job-trend-dashboard"
echo "Username: princeraj026-code"
echo "========================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}ERROR: Git not found!${NC}"
    echo ""
    echo "Please install Git:"
    echo "  Ubuntu/Debian: sudo apt-get install git"
    echo "  macOS: brew install git"
    echo "  Fedora: sudo dnf install git"
    echo ""
    exit 1
fi

echo -e "${GREEN}✓ Git found: $(git --version)${NC}"
echo ""

# Step 1: Configure Git
echo -e "${YELLOW}Step 1: Configuring Git user...${NC}"
git config --global user.name "princeraj026-code"
git config --global user.email "rajputprincesingh026@gmail.com"
echo -e "${GREEN}✓ Git user configured${NC}"
echo ""

# Step 2: Initialize repository
echo -e "${YELLOW}Step 2: Initializing Git repository...${NC}"
if [ -d .git ]; then
    echo -e "${GREEN}✓ Repository already initialized${NC}"
else
    git init
    echo -e "${GREEN}✓ Repository initialized${NC}"
fi
echo ""

# Step 3: Add files
echo -e "${YELLOW}Step 3: Adding all files...${NC}"
git add .
echo -e "${GREEN}✓ Files staged${NC}"
echo ""

# Step 4: Create commit
echo -e "${YELLOW}Step 4: Creating initial commit...${NC}"
if git rev-parse --verify HEAD &>/dev/null; then
    echo -e "${CYAN}Note: Commits already exist, creating new commit${NC}"
fi
git commit -m "Initial commit: LinkedIn Job Trends Dashboard with AI features"
echo -e "${GREEN}✓ Commit created${NC}"
echo ""

# Step 5: Set branch to main
echo -e "${YELLOW}Step 5: Setting branch to main...${NC}"
git branch -M main
echo -e "${GREEN}✓ Branch set to main${NC}"
echo ""

# Step 6: Add remote
echo -e "${YELLOW}Step 6: Adding remote repository...${NC}"
if git remote | grep -q "^origin$"; then
    echo -e "${CYAN}Note: Remote 'origin' already exists, updating URL${NC}"
    git remote set-url origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
else
    git remote add origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
fi
echo -e "${GREEN}✓ Remote repository configured${NC}"
echo ""

# Step 7: Authentication info
echo ""
echo -e "${CYAN}========================================"
echo "AUTHENTICATION REQUIRED"
echo "========================================${NC}"
echo "GitHub will ask for authentication. Use one of these:"
echo ""
echo -e "${GREEN}1. Personal Access Token (RECOMMENDED):${NC}"
echo "   - Go to: https://github.com/settings/tokens"
echo "   - Click 'Generate new token (classic)'"
echo "   - Select scope: 'repo' (full control)"
echo "   - Copy the token"
echo "   - When prompted for password, paste the TOKEN (not your GitHub password)"
echo ""
echo -e "${GREEN}2. GitHub CLI:${NC}"
echo "   - Install: brew install gh (macOS) or see https://cli.github.com/"
echo "   - Run: gh auth login"
echo ""
echo -e "${GREEN}3. SSH Key (Advanced):${NC}"
echo "   - Generate: ssh-keygen -t ed25519 -C \"rajputprincesingh026@gmail.com\""
echo "   - Add to GitHub: https://github.com/settings/keys"
echo "   - Change remote: git remote set-url origin git@github.com:princeraj026-code/Linkedin-job-trend-dashboard.git"
echo ""
echo -e "${CYAN}========================================${NC}"
echo ""

# Step 7: Push to GitHub
echo -e "${YELLOW}Step 7: Pushing to GitHub...${NC}"
if git push -u origin main; then
    echo ""
    echo -e "${GREEN}========================================"
    echo "✓ SUCCESS! Your code is on GitHub!"
    echo "========================================${NC}"
    echo ""
    echo "View your repository at:"
    echo -e "${CYAN}https://github.com/princeraj026-code/Linkedin-job-trend-dashboard${NC}"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Push failed!${NC}"
    echo ""
    echo -e "${YELLOW}Common solutions:${NC}"
    echo "1. Set up authentication (see options above)"
    echo "2. If authentication is already set up, try:"
    echo "   git pull --rebase origin main"
    echo "   git push -u origin main"
    echo ""
    exit 1
fi

echo "Press Enter to exit..."
read
