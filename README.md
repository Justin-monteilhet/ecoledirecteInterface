# Ecole DIrecte Interface
## _Python OOP Interface for [EcoleDirecte](https://ecoledirecte.com) API._

Use python to easily parse data about your grades. 

# Installation
Install the projects' files and unzip it in your own project's folder. 
The only not built-in library that you'll need is requests. Use ``pip install requests`` and you're ready to go.

# Quick Start
First, you have to authenticate. No tokens are needed (for you), you just need your username and your password :
```py
from ecoledirecte import Pupil

me = Pupil(username="Abigail", password="1234")
```

Once you've got your instance of *Pupil*, the main thing you'll want to use in the method ``get_periods`` which will return a list of trimesters as Period objects. With these, you can see your grades, teachers, means, or even council dates.

```py
for period in me.get_periods(): 
    print(period.name)
    print(period.grades["Français"])
    print(period.main_teacher)
    print(period.is_finished)
    for subj in period.subjects :
        print(subj.teacher, subj.coeff)
```

# Contact
You can reach me on Discord, I'll be happy to answer : ӄ.ʀǟռɖօʍ_ce#2808.
