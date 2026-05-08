import os
import re

base_dir = '/Users/suryateja/Downloads/svcolleges/svcolleges'

nav_html = """  <!-- Top Bar -->
  <div class="top-bar">
    <div class="container top-bar-container">
      <div class="top-bar-left">
        <span><i class="fas fa-map-marker-alt"></i> Campuses: Dilsukhnagar | Narayanguda | Champapet</span>
      </div>
      <div class="top-bar-right">
        <span><i class="fas fa-phone-alt"></i> +91 84990 84447</span>
        <span><i class="fas fa-envelope"></i> info@svcolleges.com</span>
      </div>
    </div>
  </div>

  <!-- Navigation -->
  <nav class="navbar">
    <div class="container navbar-container">
      <div class="logo">
        <a href="index.html">
          <img src="assets/images/logo.png" alt="SV Colleges Logo" style="height: 60px; max-width: 180px; object-fit: contain;">
        </a>
      </div>
      
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About Us</a></li>
        <li class="dropdown">
          <a href="#">Courses <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
          <ul class="dropdown-menu">
            <li><strong>Intermediate</strong></li>
            <li><a href="mpc-jee-nda.html">MPC with JEE/NDA</a></li>
            <li><a href="mec-ca-civils.html">MEC with CA/Civils</a></li>
            <li><a href="cec-civils-clat.html">CEC with Civils/CLAT</a></li>
            <li><hr style="margin: 0.5rem 0; opacity: 0.2;"></li>
            <li><strong>Degree</strong></li>
            <li><a href="bcom-computer-applications.html">B.Com Computer App</a></li>
            <li><a href="bcom-general.html">B.Com General</a></li>
            <li><a href="bba.html">BBA</a></li>
            <li><hr style="margin: 0.5rem 0; opacity: 0.2;"></li>
            <li><strong>Integrated</strong></li>
            <li><a href="integrated-iit-jee.html">IIT-JEE</a></li>
            <li><a href="integrated-civils.html">Civils Foundation</a></li>
            <li><a href="integrated-ca.html">CA Foundation</a></li>
            <li><a href="integrated-crt.html">CRT</a></li>
          </ul>
        </li>
        <li><a href="admissions.html">Admissions</a></li>
        <li class="dropdown">
          <a href="#">Campuses <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
          <ul class="dropdown-menu">
            <li><a href="campus-dilsukhnagar.html">Dilsukhnagar</a></li>
            <li><a href="campus-narayanguda.html">Narayanguda</a></li>
            <li><a href="campus-champapet.html">Champapet</a></li>
          </ul>
        </li>
        <li class="dropdown">
          <a href="#">More <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
          <ul class="dropdown-menu">
            <li><a href="results.html">Results</a></li>
            <li><a href="faculty.html">Faculty</a></li>
            <li><a href="gallery.html">Gallery</a></li>
            <li><a href="student-life.html">Student Life</a></li>
          </ul>
        </li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="admissions.html" class="btn btn-primary" style="color: white; padding: 0.5rem 1.2rem;">Apply Now</a></li>
      </ul>
      
      <div class="mobile-menu-btn">
        <i class="fas fa-bars"></i>
      </div>
    </div>
  </nav>"""

footer_html = """  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <div style="margin-bottom: 1.5rem; background: white; padding: 10px; display: inline-block; border-radius: 8px;">
            <img src="assets/images/logo.png" alt="SV Colleges Logo" style="height: 50px; max-width: 150px; object-fit: contain;">
          </div>
          <p>Empowering students with value-based education and integrated coaching for over two decades. Your gateway to premier academic and professional success.</p>
          <div class="social-links">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
          </div>
        </div>
        
        <div class="footer-links">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="about.html">About Us</a></li>
            <li><a href="admissions.html">Admissions</a></li>
            <li><a href="results.html">Achievements</a></li>
            <li><a href="gallery.html">Gallery</a></li>
            <li><a href="privacy-policy.html">Privacy Policy</a></li>
          </ul>
        </div>
        
        <div class="footer-links">
          <h4>Programs</h4>
          <ul>
            <li><a href="mpc-jee-nda.html">Intermediate Courses</a></li>
            <li><a href="bcom-computer-applications.html">Degree Courses</a></li>
            <li><a href="integrated-iit-jee.html">Integrated JEE</a></li>
            <li><a href="integrated-civils.html">Civils Foundation</a></li>
            <li><a href="integrated-ca.html">CA Foundation</a></li>
          </ul>
        </div>
        
        <div class="footer-contact">
          <h4>Contact Us</h4>
          <div class="contact-item">
            <i class="fas fa-phone-alt"></i>
            <span>+91 84990 84447<br>+91 92480 30405</span>
          </div>
          <div class="contact-item">
            <i class="fas fa-envelope"></i>
            <span>info@svcolleges.com</span>
          </div>
          <div class="contact-item">
            <i class="fas fa-map-marker-alt"></i>
            <span>Head Office: Dilsukhnagar, Hyderabad, Telangana</span>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2026 Sree Venkateswara Colleges. All Rights Reserved. Designed to inspire.</p>
      </div>
    </div>
  </footer>"""

files_to_update = ['index.html', 'about.html', 'contact.html']

for file in files_to_update:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We might have <!-- Top Bar --> already if we run it twice, so let's remove it if it exists.
    content = re.sub(r'<!-- Top Bar -->.*?<\/div>\s*<\/div>\s*<!-- Navigation -->', '<!-- Navigation -->', content, flags=re.DOTALL)

    nav_pattern = re.compile(r'<!-- Navigation -->.*?<\/nav>', re.DOTALL)
    content = nav_pattern.sub(nav_html, content)
    
    footer_pattern = re.compile(r'<!-- Footer -->.*?<\/footer>', re.DOTALL)
    content = footer_pattern.sub(footer_html, content)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Updated index, about, and contact with local logo and top bar.")
