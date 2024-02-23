# Dynamics Aperture (DA) simulations scenarios proposal for HL (run 4)

In this repository, we aim to summarize a set of scenarios for the HL-LHC (run 4) DA simulations (or, at the very least, one full scenario). Everyone is invited to update the values according to their expertise and knowledge. The goal is to have a set of scenarios that are agreed upon by the community, covering the whole HL-LHC cycle, and that can be used as a reference for DA simulations. Ideally, we would have the final DA results in time for IPAC '24.

## Example of scenario

[Here](scenarios/scenario_round_1.csv) is an example of a scenario:

![Scenario example](plot_scenarios/HL-LHC_DA_scenario_1_(round).png)

Note that the plot is fully interactive when run in a notebook (useful to see the parameter values all at once, for each phase of the cycle).

## Parameter values

Many parameters are still to be better defined. We need at least a value (or a lower and upper bound) for the following parameters, for each step of the cycle:

### Filling schemes

Many filling schemes have been tried in the past. We need to settle for one, or maybe a couple. Given the last updates, our main picks (suggested by Lotta) are:

- The "2700", or ```25ns_2760b_2748_2492_2574_288bpi_13inj_800ns_bs200ns```, as it's the standard scheme, and privileged choice for now.
- The "2400", or ```25ns_2452b_2440_1952_2240_248bpi_12inj_mixed``` as it's a hybrid scheme, therefore more conservative w.r.t. DA since a higher bunch intensity (and therefore lower DA) is needed to reach the target luminosity, while the worst bunch will have the same schedule as the worst bunch from the standard scheme.

### Octupoles

Should we go negative? How much? And if we stay positive, do we use the values from the 2022 operational scenario?

### Emittance

I considered 2.2 for emittance at injection (average from the 2022 operational scenario), is that correct?

Should we consider a blow-up at the end of the ramp (going up to 2.5 um)?

### Chromaticity

The 2022 operational scenario has a chromaticity of 15 for the whole cycle. However, taking into account the last updates (e.g. the BST), should we consider going lower, e.g 10?

## Limited pool of available optics

All the optics in the scenarios csv files are just my best guess. Some might be outdated, and some might be missing. Please update the optics if you have better information. For now:

- No injection optics with phase knob is available for HL 1.6. Using injection optics without phase knob. Is that fine?
- Should we go to flat for collapse?

Ideally, we would not have to test more to two optics per cycle phase.

## Pile-up constraint

We need to agree on the pile-up constraint in IP 1 and 5. In the past, we haved used 160. However, according to the last presentation from the HL-LHC projec [Commisioning of run 4, Chamonix](https://indico.cern.ch/event/1343931/contributions/5673119/attachments/2790922/4867754/Commissioning%20Run%204.pdf) it seems that 132 would be more appropriate.

## Useful references

<https://cds.cern.ch/record/2803611/files/CERN-ACC-2022-0001.pdf> (not up to data as BST, new PU constraints, new filling scheme, etc).
<https://indico.cern.ch/event/1138716/contributions/5558496/attachments/2730880/4747647/THA1C1_talk.pdf>
