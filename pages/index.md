<!--
.. title: HackEDX (Hackathons as EDucational eXperiences)
.. slug: index
.. date: 2025-09-10 13:31:20 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

<!-- What is... Section -->
<section class="edx_content" style="margin-bottom: 3rem;">
    <div class="row">
        <div>
            <p>
                I developed the HackEDX methodological framework as part of my dissertation at the University of Duisburg-Essen (2021--2025).
                The framework aims to support hackathon organizers and educators in designing and planning hackathons for learning. 
            </p>
            <p>
                On this website I present the resulting guidelines with abreviated reasoning. The full reasoning for the HackEDX (and a citable version) can be found in my to-be-published dissertation (that I will link here). <!--[dissertation]{}: <!--TODO: add link and reference --> 
            </p>
            <p>
                The HackEDX is an extension of the 12 decisions for hackathon organizers that are set in the <a href="https://hackathon-planning-kit.org">Hackathon Planning Kit</a>.
            <blockquote class="blockquote">
                <p style="margin-bottom: 1em; font-size: 0.75em; line-height: 1.5em;"> Affia-Jomants, A. O., Gama, K., Herbsleb, J. D., & Nolte, A. (2025). How to organize an in-person, online or hybrid hackathon—A revised planning kit (No. arXiv:2008.08025; Version 3). arXiv. <a href="https://doi.org/10.48550/arXiv.2008.08025">https://doi.org/10.48550/arXiv.2008.08025</a></p>
            </blockquote>
            <p>
                The navigation menu on the left links directly to individual decisions. Additionally, it includes links to external resources that were developed as part of the research, namely these are the repositories for a Participant toolbox  
            </p>
            <p>
                The figure below visualizes the framework and its connection to the 12 decisions.
            </p>
            <img src="/images/HackEDX.png" class="card-img-top" alt="Framework", style="max-height: 75vh">
        </div>
    </div>
    <div id="decisions"></div>
</section>


<script>
fetch('/docs/decision-guidelines.md')
  .then(response => response.text())
  .then(data => {
    document.getElementById('decisions').innerHTML = data;
  });
</script>