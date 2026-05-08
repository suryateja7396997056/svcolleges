import os
import re

base_dir = '/Users/suryateja/Downloads/svcolleges/svcolleges'

aos_css = '\n  <!-- AOS Animation CSS -->\n  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">'
aos_js = '\n  <!-- AOS Animation JS -->\n  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n  <script>\n    AOS.init({\n      duration: 800,\n      once: true,\n      offset: 100\n    });\n  </script>\n</body>'

# Process all html files
for filename in os.listdir(base_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # 1. Add AOS CSS
        if 'aos.css' not in content:
            content = content.replace('</head>', aos_css + '\n</head>')
            
        # 2. Add AOS JS
        if 'aos.js' not in content:
            content = content.replace('</body>', aos_js)
            
        # 3. Add AOS attributes to sections and cards to make them animate in
        # For hero content
        content = content.replace('<div class="hero-content">', '<div class="hero-content" data-aos="fade-up">')
        content = content.replace('<h1 style="font-size: 4rem;', '<h1 data-aos="fade-down" style="font-size: 4rem;')
        content = content.replace('<p style="font-size: 1.3rem;', '<p data-aos="fade-up" data-aos-delay="100" style="font-size: 1.3rem;')
        
        # For section headers
        content = content.replace('<div class="section-header">', '<div class="section-header" data-aos="fade-up">')
        
        # For stat cards and feature cards
        content = content.replace('<div class="stat-card">', '<div class="stat-card" data-aos="zoom-in" data-aos-delay="100">')
        content = content.replace('<div class="card">', '<div class="card" data-aos="fade-up" data-aos-delay="150">')
        
        # For newly generated detailed pages grids
        content = content.replace('<div style="background: var(--bg-color); padding: 3rem;', '<div data-aos="fade-left" style="background: var(--bg-color); padding: 3rem;')
        content = content.replace('<div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: center;">\n        <div>', '<div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: center;">\n        <div data-aos="fade-right">')
        content = content.replace('<div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: start;">\n        <div>', '<div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: start;">\n        <div data-aos="fade-right">')
        
        # Admissions step boxes
        content = content.replace('<div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); display: flex; gap: 2rem; align-items: center;">', '<div data-aos="fade-up" style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); display: flex; gap: 2rem; align-items: center;">')

        # Fix index.html specific broken links in the course cards
        if filename == 'index.html':
            # Card 1 MPC
            content = content.replace(
                '<a href="#" class="btn btn-outline" style="align-self: flex-start;">View Details</a>',
                '<a href="mpc-jee-nda.html" class="btn btn-outline" style="align-self: flex-start;">View Details</a>',
                1
            )
            # Card 2 MEC
            content = content.replace(
                '<a href="#" class="btn btn-outline" style="align-self: flex-start;">View Details</a>',
                '<a href="mec-ca-civils.html" class="btn btn-outline" style="align-self: flex-start;">View Details</a>',
                1
            )
            # Card 3 BCom
            content = content.replace(
                '<a href="#" class="btn btn-outline" style="align-self: flex-start;">View Details</a>',
                '<a href="bcom-computer-applications.html" class="btn btn-outline" style="align-self: flex-start;">View Details</a>',
                1
            )

        with open(filepath, 'w') as f:
            f.write(content)

print("AOS Animations added to all pages and internal links fixed.")
