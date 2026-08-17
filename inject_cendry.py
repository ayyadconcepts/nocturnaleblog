import os

target_files = [
    "src/content/blog/alarm-readiness-wake-up-rehearsal.md",
    "src/content/blog/bedwetting-alarm-vs-medication.md",
    "src/content/blog/clinical-hypnotherapy-nocturnal-enuresis.md",
    "src/content/blog/find-qualified-clinical-hypnotherapist-enuresis.md",
    "src/content/blog/hypnosis-vs-bedwetting-alarm.md",
    "src/content/blog/mind-body-bedwetting-self-hypnosis.md",
    "src/content/blog/self-guided-hypnosis-teens-bedwetting.md",
    "src/content/blog/clinical-bladder-diary-bedwetting.md",
    "src/content/blog/free-clinical-bladder-diary.md",
    "src/content/blog/parents-guide-nocturnal-enuresis.md",
    "src/content/blog/teen-guide-stopping-bedwetting.md"
]

html_snippet = """

<div class="cendry-callout">
  <p><strong>Dr. Barroso Recommends: Cendry Bedwetting Assistant</strong></p>
  <p>I highly recommend the <strong><a href="https://cendry.app" target="_blank">Cendry app</a></strong>. I use it with my own patients, and it offers an incredibly robust approach to overcoming bedwetting. Cendry features <strong>advanced progress tracking</strong> to pinpoint exactly what works for each user, alongside <strong>built-in alarms</strong> and <strong>targeted hypnosis tracks</strong> designed with two goals: helping you wake up at night, or training the brain to stay dry until tomorrow.</p>
</div>

"""

for f in target_files:
    if not os.path.exists(f):
        print(f"File not found: {f}")
        continue
        
    with open(f, 'r') as file:
        lines = file.readlines()
        
    # Check if already injected
    already_injected = False
    for line in lines:
        if "cendry-callout" in line:
            already_injected = True
            break
            
    if already_injected:
        print(f"Already injected in {f}")
        continue
        
    # Inject before the LAST h2 or h3
    injection_idx = -1
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("##"):
            injection_idx = i
            break
            
    if injection_idx != -1:
        lines.insert(injection_idx, html_snippet)
    else:
        # Fallback: just append
        lines.append(html_snippet)
        
    with open(f, 'w') as file:
        file.writelines(lines)
        
print("Injection complete!")
