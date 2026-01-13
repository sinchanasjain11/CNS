cybersecurity_incidents=[
    "the morris worm disrupted computers in 1988 ,one of the first computer worms distributed via the internet ",
    " in 2007 ,estonia suffered a massive ddos attack that crippled the nation's digital infrastructure",
    " in 2013 ,target experienced a major data breach where milliojns of credit card details were stolen",
    " the wannacry ransomware attack in 2017 affected thousand of computer globally, enrypting data and demanding ransom ",
    " a phishing attack in 2016 compromised the email account of several high profile figures,leading to the release of sensitive information",
    " the mirai botnet in 2016 launched ddos attack using lot device ,bringing down large parts of the internet"
]
categories={"virus":[],"phising":[],"ddos":[],"ransomware":[],"data breach":[]}
for incident in cybersecurity_incidents:
    for category in categories:
        if category in incident.lower():
            categories[category].append(incident)
for category ,incidents in categories.items():
    print(f"\ncategory:{category.capitalize()}")
    print("\n".join(incidents)if incidents else "no incidents in this category")
            