# Dynamics Aperture (DA) simulations scenarios proposal for HL (run 4)

In this repository, we aim to summarize a set of scenarios for the HL-LHC (run 4) DA simulations. Everyone is invited to update the values according to their expertise and knowledge. The goal is to have a set of scenarios that are agreed upon by the community, covering the whole HL-LHC cycle, and that can be used as a reference for DA simulations. Ideally, we would have the final DA results in time for IPAC '24.

## Example of scenario

Here is an example of a scenario:

```csv
Time (a.u.),Step,Energy (TeV),Emittance (μm),Intensity (1e11 ppb),Beta (m),Luminosity (1e34 cm2/s),Octupoles (A),Crabs (μrad),Chromaticity,Optics
0,Start injection,0.45,2.0,0,11,0,10,0,15,Skipped
0.2,End of injection,0.45,2.0,2.3,11,0,10,0,15,operation/optics/R2023a_A11mC11mA10mL10m_PhaseKnob100ON.madx
0.5,End of ramp,7,2.0,2.3,1,0,?,0,15,Same_as_start_of_collapse
0.6,Start of collapse,7,2.0,2.3,1,0,?,0,15,flat/start_collapse/opt_collapse_flathv_700_2800_thin.madx (not here anymore)
0.65,End of collapse,7,2.5,2.3,1,2,?,0,15,?
0.9,Start of levelling,7,2.5,2.2,0.59,5,60,190,15,acc-models-lhc/strengths/flat/opt_flatvh_500_2000.madx
2,End of levelling,7,2.5,1.4,0.15,5,60,190,15,acc-models-lhc/strengths/round/opt_flatvh_75_180_1500.madx
2.5,Dump,7,2.5,1.2,0.15,4,60,190,15,Same as end of levelling
``````


## Parameter values

Many parameters are still to be better defined. We need at least a lower and upper bound for the following parameters, for each step of the cycle:

- octupoles
- emittance
- chromaticity

## Filling schemes

Many filling schemes have been tried in the past. We need to settle for one, or maybe a couple. Our main picks are:

- ```25ns_2452b_2440_1952_2240_248bpi_12inj_mixed``` as it's a hybrid scheme, therefore more conservative w.r.t. DA since a higher bunch intensity (and therefore lower DA) is needed to reach the target luminosity, while the worst bunch will have the same schedule as the worst bunch from the standard scheme.
- ```25ns_2760b_2748_2492_2574_288bpi_13inj_800ns_bs200ns```, as it's the standard scheme, and privileged choice for now.

## Missing optics

All the optics in the scenarios csv files are just my best guess. Some might be outdated, and some might be missing. Please update the optics if you have better information. For now:

- No injection optics is available for HL 1.6. Using run III optics for now... But not ideal.
- No flat end of collapse optics seems available.
- I had to adapt some of the $\beta^\*$ in the scenarios to match the available optics. E.g. $\beta^* = 0.59m$ instead of $\beta^* = 0.64m$ as the latter is not available.

Ideally, we would not have to test more to two optics per cycle phase.

## Pile-up constraint

We need to agree on the pile-up constraint in IP 1 and 5. In the past, we haved used 160. However, according to the last presentation from the HL-LHC projec [Commisioning of run 4, Chamonix](https://indico.cern.ch/event/1343931/contributions/5673119/attachments/2790922/4867754/Commissioning%20Run%204.pdf) it seems that 132 would be more appropriate.
