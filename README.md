# Dynamics Aperture (DA) simulations scenarios proposal for HL (run 4)

In this repository, we aime to summarize a set of scenarios for the HL-LHC (run 4) DA simulations.

## Filling schemes

Many filling schemes have been tried in the past. We need to settle for one, or maybe a couple. Our main picks are:

- ```25ns_2452b_2440_1952_2240_248bpi_12inj_mixed``` as it's a hybrid scheme, therefore more conservative w.r.t. DA since a higher bunch intensity (and therefore lower DA) is needed to reach the target luminosity, while the worst bunch will have the same schedule as the worst bunch from the standard scheme.
- ```25ns_2760b_2748_2492_2574_288bpi_13inj_800ns_bs200ns```, as it's the standard scheme, and privileged choice for now.

## Missing optics

- No injection optics is available for HL 1.6. Using run III optics for now... But not ideal.
- I had to adapt some of the $\beta^\*$ in the scenarios to match the available optics. E.g. $\beta^* = 0.59m$ instead of $\beta^* = 0.64m$ as the latter is not available.
