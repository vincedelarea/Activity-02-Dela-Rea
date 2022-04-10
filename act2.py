from sympy import *
import random as r

statval = {
    "level": 90,
    "power": 110,
    "attack": 205,
    "defense": 188,
    "targets": 1,
    "weather": 1,
    "badge": 1,
    "critical": 1,
    "random": 0,
    "stab": 1.5,
    "mtype": 0.5,
    "burn": 1,
    "misc": 1,
}

statval["num"] = r.randint(85,100)/100
#level, power, attack, defense, targets, weather, badge, critical, random, stab, mtype, burn, misc
level, power, attack, defense, targets, weather, badge, critical, random, stab, mtype, burn, misc = symbols("level, power, attack, defense, targets, weather, badge, critical, random, stab, mtype, burn, misc")
modifier = (targets*weather*badge*critical*random*stab*mtype*burn*misc)
formula = ((((2*level)/5+2)*power*attack/defense)/50+2)
print(N(formula.subs([(level,statval["level"]),(power,statval["power"]),(attack,statval["attack"]),(defense,statval["defense"])])*(modifier.subs([(targets,statval["targets"]),(weather,statval["weather"]),(badge,statval["badge"]),(critical,statval["critical"]),(random,statval["num"]),(stab,statval["stab"]),(mtype,statval["mtype"]),(burn,statval["burn"]),(misc,statval["misc"])]))).evalf(4))
