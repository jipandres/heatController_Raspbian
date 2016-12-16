# heatController_Raspbian
Project to control a relay that switchs on/off a cauldron remotely using a Raspberry Pi with Raspbian

## The Cauldron
The cauldron must have support for a relay to switch on/off it.

In my case, I want to control a [Domusa BioClass NG](http://www.domusateknik.com/en/products/biomass-boiler/pellet-boilers/bioclass-hm)

# Process
This is mainly a personal project anarquic in the sense that no dates are commited, no scope is commited, there are no milestones, etc.
I will try to do what I can in my free time.

# Branch strategy
This project will mainly follow the approach of [A successful git branching model](http://nvie.com/posts/a-successful-git-branching-model/).

Development is done in private branches and once it works a piece or a component, it will be merged to **development**.
Once a desired functionality is completed, it will be moved from **development** to **release** to verify it, and once it is fixed. It will be moved to **master** 

