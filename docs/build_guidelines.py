import json
import os

def process_guideline(guideline, prefix=""):
    guideline_html = ('\n\t\t<div class="guideline">'
     '\n\t\t\t<h3>Guideline {guideline_number}: {guideline_name}. </h3>'
     '\n\t\t\t<p>{guideline_text}</p>'
     '\n\t\t</div>').format(guideline_number=str(prefix) + str(guideline['guideline_number']),
                            guideline_name=guideline['guideline_name'],
                            guideline_text=guideline['guideline_text'])
    if "guideline_pre_text" in guideline:
        guideline_html = ('\n\t<div> \n\t\t<p>{guideline_pre_text}</p>'
                          '\n\t</div>').format(guideline_pre_text=guideline['guideline_pre_text']) + guideline_html
    if "sub_guidelines" in guideline:
        for sub_guideline in guideline['sub_guidelines']:
            guideline_html + "\n" + process_guideline(sub_guideline, prefix=guideline['guideline_number'])
    return guideline_html

def process_decision(decision):
    guideline_html = ""
    if "guidelines" in decision:
        for guideline in decision['guidelines']:
            guideline_html += process_guideline(guideline) + "\n"
    decision_html = ('<!-- Decision {decision_number} --> '
                     '\n<section id="decision{decision_number}" style="margin-bottom: 3rem;"> '
                     '\n\t<div class="row"> '
                     '\n\t\t<div> \n\t\t\t<h2>Decision {decision_number}: {decision_name}</h2>'
                     '\n\t\t\t<p>{decision_text}</p>'
                     '\n\t\t</div>'
                     '{guidelines_html}'
                     '\n\t</div>'
                     '\n</section>').format(decision_number=decision['decision_number'],
                                            decision_name=decision['decision_name'],
                                            decision_text=decision['decision_text'],guidelines_html=guideline_html)
    return decision_html

def process_extra(extra):
    guideline_html = ""
    if "guidelines" in extra:
        for guideline in extra['guidelines']:
            guideline_html += process_guideline(guideline) + "\n"
    extra_html = ('<!-- {extra_name} --> '
                     '\n<section id="decision1" style="margin-bottom: 3rem;"> '
                     '\n\t<div class="row"> '
                     '\n\t\t<div> \n\t\t\t<h2>{extra_name}</h2>'
                     '\n\t\t\t<p>{extra_text}</p>'
                     '\n\t\t</div>'
                     '{guidelines_html}'
                     '\n\t</div>'
                     '\n</section>').format(extra_name=extra['topic'],
                                            extra_text=extra['topic_text'], guidelines_html=guideline_html)
    return extra_html

dir = os.path.dirname(__file__)
in_file = os.path.join(dir, 'decision-guidelines.json')
with open(in_file, "r", encoding="utf-8") as json_file:
    decision_list = json.loads(json_file.read())
    html = ""
    for decision in decision_list["decisions"]:
        html += process_decision(decision)
    for extra in decision_list["additional_guidelines"]:
        html += process_extra(extra)

out_file = os.path.join(dir, 'decision-guidelines.md')
with open(out_file, "w", encoding="utf-8") as html_file:
    html_file.write(html)

