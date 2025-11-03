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
<section class="py-5 bg-light" style="margin-bottom: 3rem;">
    <div class="row">
        <div class="col-md-6">
            <p>
                I developed the HackEDX methodological framework as part of my dissertation at the University of Duisburg-Essen (2021--2025).
                The framework aims to support hackathon organizers and educators in designing and planning hackathons for learning. 
                HackEDX extends the 12 decisions for hackathon organizers that are set in the [Hackathon Planning Kit][https://hackathon-planning-kit.org].
            </p>
            <blockquote class="blockquote">
                <p style="margin-bottom: 1em; font-size: 0.75em; line-height: 1.5em;"> Affia-Jomants, A. O., Gama, K., Herbsleb, J. D., & Nolte, A. (2025). How to organize an in-person, online or hybrid hackathon—A revised planning kit (No. arXiv:2008.08025; Version 3). arXiv. https://doi.org/10.48550/arXiv.2008.08025</p>
            </blockquote>
            <img src="/images/HackEDX.png" class="card-img-top" alt="Framework", style="max-height: 75vh">
            <p>
                The full reasoning for the HackEDX (and a citable version) can be found in my [dissertation]{}: <!--TODO: add link and reference --> 
            </p>
        </div>
    </div>
</section>


<div id="decisions"></div>
<script>
fetch('/docs/decision-guidelines.md')
  .then(response => response.text())
  .then(data => {
    document.getElementById('decisions').innerHTML = data;
  });
</script>