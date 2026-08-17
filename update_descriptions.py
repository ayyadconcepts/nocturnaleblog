import os
import re

descriptions = {
    "about-ubirajara-barroso.md": "Learn about Prof. Dr. Ubirajara Barroso Jr., MD, PhD, a leading pediatric urologist specializing in evidence-based nocturnal enuresis treatments.",
    "adult-bedwetting-sleep-apnea.md": "Discover the critical medical link between adult bedwetting (nocturnal enuresis) and obstructive sleep apnea, and how treating breathing can stop bedwetting.",
    "adult-enuresis-medical-treatments.md": "Explore the latest clinical medical treatments and pharmacotherapy options for adults suffering from nocturnal enuresis (bedwetting).",
    "adult-nocturnal-enuresis.md": "A comprehensive clinical guide to adult bedwetting, covering underlying causes, targeted urological work-ups, and evidence-based treatments.",
    "alarm-readiness-wake-up-rehearsal.md": "Prepare for success with our bedwetting alarm readiness checklist and wake-up rehearsal strategies to build a strong mind-bladder connection.",
    "bedwetting-alarm-vs-medication.md": "Compare the clinical efficacy, safety, and long-term success rates of bedwetting alarms versus desmopressin and other enuresis medications.",
    "bedwetting-constipation-bladder-bowel-dysfunction.md": "Understand how hidden constipation reduces bladder capacity and why resolving bowel dysfunction is the mandatory first step to curing bedwetting.",
    "bedwetting-fluid-management-diet.md": "Learn how specific dietary restrictions, limiting evening fluids, and avoiding bladder irritants can significantly reduce bedwetting incidents.",
    "bedwetting-red-flags-when-to-see-doctor.md": "Recognize the clinical red flags of bedwetting. Learn when daytime symptoms, pain, or sudden onset enuresis require immediate urological care.",
    "bedwetting-sleep-snoring-sleep-apnea.md": "Explore why children who snore or have sleep apnea frequently wet the bed, and how correcting airway issues can resolve enuresis.",
    "bedwetting-sleepover-camp-guide.md": "A practical, medically sound guide for managing sleepovers and summer camps for children and teens with bedwetting to protect their confidence.",
    "bedwetting-treatment-not-working.md": "What to do when bedwetting treatments fail. A clinical guide to reassessing alarms, adjusting medications, and exploring advanced therapies.",
    "clinical-bladder-diary-bedwetting.md": "Learn how to use a clinical bladder and bowel diary to track voiding patterns, identify root causes, and accelerate bedwetting treatment.",
    "clinical-hypnotherapy-nocturnal-enuresis.md": "An evidence-based look at clinical hypnotherapy as an adjunct treatment for nocturnal enuresis, reducing anxiety and supporting alarm therapy.",
    "find-qualified-clinical-hypnotherapist-enuresis.md": "Learn how to find and vet a qualified, credentialed clinical hypnotherapist to support your child's comprehensive bedwetting treatment plan.",
    "free-clinical-bladder-diary.md": "Download our free, clinician-approved bladder and bowel diary in CSV format to track bedwetting triggers, voiding patterns, and treatment progress.",
    "hypnosis-vs-bedwetting-alarm.md": "Compare clinical hypnotherapy with the bedwetting alarm. Learn why alarms are the gold standard and how hypnosis can provide valuable adjunct support.",
    "mind-body-bedwetting-self-hypnosis.md": "Discover how mind-body techniques, self-hypnosis, and guided imagery can reduce bedtime anxiety and strengthen the mind-bladder connection.",
    "nocturnal-enuresis-research-publications.md": "Explore Dr. Ubirajara Barroso Jr.'s extensive peer-reviewed research and academic publications advancing the treatment of pediatric nocturnal enuresis.",
    "parents-guide-nocturnal-enuresis.md": "The complete parent's guide to understanding, diagnosing, and treating nocturnal enuresis. Stop the blame and start evidence-based clinical care.",
    "primary-vs-secondary-enuresis.md": "Understand the critical clinical difference between primary bedwetting and secondary enuresis, and how this distinction changes the treatment approach.",
    "self-guided-hypnosis-teens-bedwetting.md": "A guide for teens on using self-guided hypnosis and mental rehearsal to manage the stress of bedwetting and improve treatment adherence.",
    "teen-guide-stopping-bedwetting.md": "A private, science-based guide for teenagers suffering from bedwetting. Discover effective treatments, privacy tips, and how to finally wake up dry."
}

directory = "src/content/blog/"

for filename, new_desc in descriptions.items():
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Replace the description line using regex
        new_content = re.sub(r'description:\s*".*?"', f'description: "{new_desc}"', content, count=1)
        
        with open(filepath, 'w') as file:
            file.write(new_content)
            
print("Descriptions updated successfully!")
