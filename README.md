# Dynamics Aperture (DA) simulations scenarios proposal for HL (run 4)

In this repository, we aim to summarize a set of scenarios for the HL-LHC (run 4) DA simulations (or, at the very least, one full scenario). Everyone is invited to update the values according to their expertise and knowledge. The goal is to have a set of scenarios that are agreed upon by the community, covering the whole HL-LHC cycle, and that can be used as a reference for DA simulations. Ideally, we would have the final DA results in time for IPAC '24.

## Example of scenario

[Here](scenarios/scenario_round_1.csv) is an example of a scenario:

![Scenario example](plot_scenarios/HL-LHC_DA_scenario_1_(round).png)

Note that the plot is fully interactive when run in a notebook (useful to see the parameter values all at once, for each phase of the cycle).

## Parameter values

We favoured parameters coming from the [Run 4 Operational scenario from 2022](https://cds.cern.ch/record/2803611/files/CERN-ACC-2022-0001.pdf), however, given that this document is not up to date with the latest developments (e.g. beam screen treatment, filling scheme, pile-up constraints, etc.), we also tried to update the values inspiring ourselves from [Mounet et al., 2024](https://cernbox.cern.ch/s/fvNx0JfKtse1Kjo), the [WP2 talk form Riccardo during December 2023](https://indico.cern.ch/event/1355706/#19-update-on-the-hl-lhc-cycle), and the talk presenting the [Commisioning of run 4, at Chamonix](https://indico.cern.ch/event/1343931/contributions/5673119/attachments/2790922/4867754/Commissioning%20Run%204.pdf).

Yet, many parameters are still to be better defined. We need at least a value (or a lower and upper bound) for the following parameters, for each step of the cycle.

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

The 2022 operational scenario has a chromaticity of 15 for the whole cycle. However, taking into account the last updates, should we consider going lower, e.g 10?

### Bunch intensity

Should we go from 2.3e11 to 2.2e11 after collapse, just like in the operational scenario? Or should we keep 2.3e11 as e.g. in the simulations presented in [Mounet et al., 2024](https://cernbox.cern.ch/s/fvNx0JfKtse1Kjo)?

### Crab cavities

Given the last updates, especially regarding the filling scheme, and the available optics at the start of levelling, we were considering optimizing the luminosity at the start of levelling using the crab cavities not to exceed the target lumi or PU constraint. The crab would then be pushed to the max (-190), once the ATS squeezing can't compensate for the loss of lumi (or conversely). Does that seem like a reasonable strategy?

## Limited pool of available optics

For DA simulations, we ideally need thin optics, that are already available (as there's not much time to produce new ones, and the deadline for IPAC is coming quickly). However, the pool of available optics is quite limited.

- No injection optics with phase knob is available for HL 1.6. For consistency, we decided to use the HL 1.6 injection optics without phase knob (rather than the run III optics with phase knob). Is that fine?
- Should we go to flat for collapse to decrease crab cavities impedance?
- The only thin optics available at the end of ramp is ```opt_ramp_500_1500_thin.madx```, which has a smaller beta than the topics at start of collapse. That seems problematic. The alternative would be to use the ```opt_ramp_2000_1500.madx```, but it doesn't seem to be thin. What should we do?

## Pile-up constraint

We need to agree on the pile-up constraint in IP 1 and 5. In the past, we haved used 160. However, according to the last presentation from the HL-LHC project [Commisioning of run 4, Chamonix](https://indico.cern.ch/event/1343931/contributions/5673119/attachments/2790922/4867754/Commissioning%20Run%204.pdf) it seems that 132 would be more appropriate.

## Useful references

[Run 4 Operational scenario from 2022](https://cds.cern.ch/record/2803611/files/CERN-ACC-2022-0001.pdf)

[Mounet et al., 2024](https://cernbox.cern.ch/s/fvNx0JfKtse1Kjo)

[December talk form Riccardo during december 2023](https://indico.cern.ch/event/1355706/#19-update-on-the-hl-lhc-cycle)

[Commisioning of run 4, Chamonix](https://indico.cern.ch/event/1343931/contributions/5673119/attachments/2790922/4867754/Commissioning%20Run%204.pdf)
