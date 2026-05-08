import os

base_dir = '/Users/suryateja/Downloads/svcolleges/svcolleges'

css_path = os.path.join(base_dir, 'css/style.css')
with open(css_path, 'r') as f:
    css_content = f.read()

# I need to move the .nav-links rules from @media (max-width: 768px) to @media (max-width: 992px)
# But it's easier to just do a string replacement for the media queries.

# First, remove nav-links rules from 768px block and inject them into 992px block
nav_rules = """
  /* Mobile Navbar Fixes */
  .navbar-container {
    position: relative;
  }
  
  .nav-links {
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
  
  .mobile-menu-btn { display: block; }
"""

# The .mobile-menu-btn { display: block; } might be inside 768px.
if ".mobile-menu-btn { display: block; }" in css_content:
    css_content = css_content.replace(".mobile-menu-btn { display: block; }", "")

if "/* Mobile Navbar Fixes */" in css_content:
    # Just strip it out completely to reconstruct cleanly
    css_content = css_content.split("/* Mobile Navbar Fixes */")[0]

css_content += """
/* --- Re-applied Mobile Navbar Fixes for Tablet (992px) --- */
@media (max-width: 992px) {
  .navbar-container {
    position: relative;
  }
  
  .nav-links {
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
  }
  
  .nav-links li {
    width: 100%;
    margin-bottom: 1rem;
  }
  
  .dropdown-menu {
    position: static;
    opacity: 1;
    visibility: visible;
    transform: none;
    box-shadow: none;
    padding: 0 0 0 1rem;
    background: transparent;
    display: none;
    margin-top: 0.5rem;
  }
  
  .dropdown.active .dropdown-menu {
    display: block;
  }
  
  .dropdown:hover .dropdown-menu {
    display: none; 
  }
  .dropdown.active:hover .dropdown-menu {
    display: block;
  }
  
  .mobile-menu-btn { display: block; }
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
  .logo img {
    height: 40px !important;
  }
  .top-bar-container {
    flex-direction: column;
    gap: 5px;
    font-size: 0.75rem;
  }
  .hero-content h1 { font-size: 2.2rem; }
  .stats-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 480px) {
  .stats-grid { grid-template-columns: 1fr; }
}
"""

with open(css_path, 'w') as f:
    f.write(css_content)

# Update JS to trigger dropdowns at 992px
js_path = os.path.join(base_dir, 'js/main.js')
with open(js_path, 'r') as f:
    js_content = f.read()

js_content = js_content.replace('window.innerWidth <= 768', 'window.innerWidth <= 992')

# Also, when clicking a regular link inside the nav-links, on mobile we should close the menu
# Add code to close the menu on link click (if it's not a dropdown toggle)
close_menu_js = """
  // Close menu when clicking a standard link inside nav-links
  const standardLinks = document.querySelectorAll('.nav-links a:not(.dropdown-toggle)');
  standardLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 992 && navLinks.classList.contains('active')) {
        navLinks.classList.remove('active');
        const icon = mobileBtn.querySelector('i');
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
      }
    });
  });
"""

if "Close menu when clicking a standard link" not in js_content:
    js_content = js_content.replace('});\n});', '});\n' + close_menu_js + '});')

with open(js_path, 'w') as f:
    f.write(js_content)

print("Tablet & Mobile CSS completely synced to 992px")
