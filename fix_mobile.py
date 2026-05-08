import os
import re

base_dir = '/Users/suryateja/Downloads/svcolleges/svcolleges'

# --- 1. Fix HTML files ---
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

grid_target1 = 'style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: center;"'
grid_target2 = 'style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: start;"'
grid_replacement = 'class="detailed-grid"'

admission_target = 'style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); display: flex; gap: 2rem; align-items: center;"'
admission_replacement = 'class="admission-step" data-aos="fade-up"' # Keep AOS if it was there

# Admissions specific inline fix
admissions_target_2 = '<div data-aos="fade-up" style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); display: flex; gap: 2rem; align-items: center;">'
admissions_replacement_2 = '<div class="admission-step" data-aos="fade-up">'


for file in html_files:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace detailed grid inline styles with class
    content = content.replace(grid_target1, grid_replacement)
    content = content.replace(grid_target2, grid_replacement)
    
    # Replace admissions flex inline styles with class
    content = content.replace(admission_target, 'class="admission-step"')
    content = content.replace(admissions_target_2, admissions_replacement_2)
    
    # Also fix dropdown parent links to have a class for JS targeting
    content = content.replace('<li class="dropdown">\n          <a href="#">', '<li class="dropdown">\n          <a href="#" class="dropdown-toggle">')
    
    # Quick fix for any rogue inline padding on banners
    content = re.sub(r'style="padding: 10rem 0 6rem;([^"]*)"', r'class="page-banner" style="\1"', content)
    
    with open(filepath, 'w') as f:
        f.write(content)

# --- 2. Fix CSS ---
css_path = os.path.join(base_dir, 'css/style.css')
with open(css_path, 'r') as f:
    css_content = f.read()

# Add responsive classes
responsive_css = """

/* --- Responsive Layout Fixes --- */
.detailed-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 4rem;
  align-items: start;
}

.admission-step {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  display: flex;
  gap: 2rem;
  align-items: center;
}

/* Base Page Banner adjustment */
.page-banner {
  padding: 10rem 0 6rem;
  background-position: center;
  background-size: cover;
}

@media (max-width: 992px) {
  .detailed-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  .admission-step {
    flex-direction: column;
    text-align: center;
  }
  
  .page-banner {
    padding: 7rem 0 3rem !important;
  }
  
  .page-banner h1 {
    font-size: 2.2rem !important;
  }
  
  .page-banner p {
    font-size: 1.1rem !important;
  }
  
  /* Mobile Navbar Fixes */
  .navbar-container {
    position: relative;
  }
  
  .nav-links {
    position: absolute;
    top: 100%; /* Directly below navbar */
    left: -100%;
    flex-direction: column;
    background: var(--white);
    width: 100vw;
    height: 80vh;
    padding: 1rem 2rem;
    overflow-y: auto;
    transition: left 0.3s ease;
    box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    align-items: flex-start;
  }
  
  .nav-links.active {
    left: -2rem; /* Account for container padding to span full width */
  }
  
  .nav-links li {
    width: 100%;
    margin-bottom: 1rem;
  }
  
  /* Mobile Dropdown Fix */
  .dropdown-menu {
    position: static; /* Prevent absolute positioning overlap */
    opacity: 1;
    visibility: visible;
    transform: none;
    box-shadow: none;
    padding: 0 0 0 1rem; /* Indent */
    background: transparent;
    display: none; /* Hide by default on mobile */
    margin-top: 0.5rem;
  }
  
  .dropdown.active .dropdown-menu {
    display: block; /* Show when toggled via JS */
  }
  
  .dropdown:hover .dropdown-menu {
    /* Disable hover on mobile to prevent conflicts with JS toggle */
    display: none; 
  }
  .dropdown.active:hover .dropdown-menu {
    display: block;
  }
  
  /* Logo adjustments */
  .logo img {
    height: 40px !important;
  }
  
  /* Hide Top bar on very small screens to save space, or just center */
  .top-bar-container {
    flex-direction: column;
    gap: 5px;
    font-size: 0.75rem;
  }
  
  .hero-content h1 { font-size: 2.2rem; }
  .stats-grid { grid-template-columns: 1fr 1fr; } /* Keep stats 2x2 on mobile */
}

@media (max-width: 480px) {
  .stats-grid { grid-template-columns: 1fr; } /* 1x4 on very small phones */
}
"""

if "/* --- Responsive Layout Fixes --- */" not in css_content:
    css_content += responsive_css
    
    # We must also remove the old broken .nav-links from the existing @media(max-width: 768px) block to prevent conflicts
    # Let's just do a string replace for the old nav-links block
    old_nav_css = """.nav-links {
    position: fixed;
    top: 80px;
    left: -100%;
    flex-direction: column;
    background: var(--white);
    width: 100%;
    height: calc(100vh - 80px);
    padding: 2rem;
    transition: var(--transition);
    box-shadow: 0 10px 15px rgba(0,0,0,0.1);
  }
  .nav-links.active { left: 0; }"""
    
    if old_nav_css in css_content:
        css_content = css_content.replace(old_nav_css, "/* Replaced by mobile layout fixes */")
        
    with open(css_path, 'w') as f:
        f.write(css_content)

# --- 3. Fix JS ---
js_path = os.path.join(base_dir, 'js/main.js')
with open(js_path, 'r') as f:
    js_content = f.read()

mobile_dropdown_js = """
  // Mobile Dropdown Toggle
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', function(e) {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        const parentLi = this.parentElement;
        parentLi.classList.toggle('active');
      }
    });
  });
"""

if "Mobile Dropdown Toggle" not in js_content:
    # Insert before the closing });
    js_content = js_content.replace('});', mobile_dropdown_js + '\n});')
    with open(js_path, 'w') as f:
        f.write(js_content)

print("Mobile responsiveness completely fixed.")
