# Contributing to Job Trends & Skill-Gap Analyzer

First off, thank you for considering contributing to this project! 🎉

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

This project and everyone participating in it is governed by respect, professionalism, and collaboration. Be kind and considerate.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/job-trend.git
   cd job-trend
   ```
3. **Set up your environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
4. **Create a branch** for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 💡 How to Contribute

### Reporting Bugs
- Use the GitHub issue tracker
- Describe the bug clearly
- Include steps to reproduce
- Mention your environment (OS, Python version)

### Suggesting Features
- Open an issue with the "enhancement" label
- Use the task request template (`.github/ISSUE_TEMPLATE/task_request.md`)
- Explain the use case and benefits

### Picking Up Tasks
- Check `TODO.md` for available tasks
- Look for tasks marked as `High` or `Medium` priority
- Comment on the issue to claim it
- Update TODO.md checkbox when starting/completing

## 🔄 Development Workflow

1. **Sync with main branch**:
   ```bash
   git checkout main
   git pull upstream main
   ```

2. **Create feature branch**:
   ```bash
   git checkout -b feature/add-skill-extraction
   ```

3. **Make your changes**:
   - Write clean, documented code
   - Follow the coding standards below
   - Add tests if applicable

4. **Test your changes**:
   ```bash
   python src/your_script.py
   # or use VS Code tasks
   ```

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add skill extraction for Python jobs"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/add-skill-extraction
   ```

7. **Open a Pull Request** on GitHub

## 📝 Coding Standards

### Python Style
- Follow **PEP 8** style guide
- Use **4 spaces** for indentation (not tabs)
- Maximum line length: **88 characters** (Black formatter)
- Use **type hints** where appropriate

### Documentation
- Add **docstrings** to all functions and classes:
  ```python
  def extract_skills(job_description: str) -> list:
      """
      Extract technical skills from job description.
      
      Args:
          job_description: Full text of job posting
          
      Returns:
          List of identified skills
      """
      pass
  ```

### Naming Conventions
- **Variables/Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private methods**: `_leading_underscore`

### File Organization
- Place scripts in `src/`
- Dashboard code in `app/`
- Utilities in `src/utils.py`
- Configuration in `src/config.py`

### Comments
- Write **clear, concise** comments
- Explain **WHY**, not what
- Update comments when changing code

## 📦 Commit Guidelines

We follow **Conventional Commits**:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting, missing semicolons)
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples
```bash
feat(extraction): add skill extraction for Java jobs
fix(cleaning): handle missing company_name values
docs(readme): update installation instructions
refactor(charts): simplify bar chart generation
```

## 🔍 Pull Request Process

1. **Update TODO.md** - Mark completed tasks with `[x]`

2. **Update documentation** - If you added features, update README.md

3. **Fill PR template**:
   - Description of changes
   - Related issue number
   - Screenshots (if UI changes)
   - Checklist completion

4. **Ensure all checks pass**:
   - Code runs without errors
   - No new warnings
   - Follows style guide

5. **Request review** from maintainers

6. **Address feedback** promptly

7. **Squash commits** if requested before merge

## 🧪 Testing Guidelines

- Test your code manually before committing
- Add unit tests for complex logic
- Verify data processing doesn't break existing outputs
- Check dashboard pages render correctly

## 📁 Project-Specific Guidelines

### Working with Data
- Never commit large CSV files (use .gitignore)
- Document data transformations
- Preserve original data in `data/raw/`
- Save processed data to `data/processed/`

### Creating Visualizations
- Save charts to `outputs/charts/`
- Use high DPI (300) for quality
- Follow color scheme in `config.py`
- Add axis labels and titles

### Dashboard Development
- Use Streamlit best practices
- Add caching with `@st.cache_data`
- Make filters intuitive
- Test on different screen sizes

### Adding Skills/Categories
- Update `src/config.py` → `SKILL_CATEGORIES`
- Keep alphabetically sorted
- Add common variations

## 💬 Questions?

- Open an issue for general questions
- Tag maintainers with `@username`
- Join our discussion board

## 🎁 Recognition

Contributors will be:
- Listed in README.md
- Credited in final presentation
- Mentioned in blog post (if applicable)

---

Thank you for contributing! 🙌

**Happy Coding!** 🚀
