import os
import re

base_dir = '/Users/suryateja/Downloads/svcolleges/svcolleges'

css_path = os.path.join(base_dir, 'css/style.css')
with open(css_path, 'r') as f:
    css_content = f.read()

# Replace the entirely flawed mobile nav-links block
old_nav_links_mobile = """.nav-links {
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
  }"""

new_nav_links_mobile = """.nav-links {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    flex-direction: column;
    background: var(--white);
    padding: 1.5rem;
    height: auto;
    max-height: calc(100vh - 70px);
    overflow-y: auto;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.3s ease;
    box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    align-items: flex-start;
  }
  
  .nav-links.active {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }"""

css_content = css_content.replace(old_nav_links_mobile, new_nav_links_mobile)

with open(css_path, 'w') as f:
    f.write(css_content)

print("CSS Fixed for Mobile Menu")
