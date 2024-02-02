import matplotlib.pyplot as plt

class Step:
    def __init__(self, name, time, energy, emittance, intensity, beta, luminosity, octupoles, crab_cavities):
        self.name = name
        self.time = time
        self.energy = energy
        self.emittance = emittance
        self.intensity = intensity
        self.beta = beta
        self.luminosity = luminosity
        self.octupoles = octupoles
        self.crab_cavities = crab_cavities

    def __repr__(self) -> str:
        return f"Step(name={self.name}, time={self.time},energy={self.energy},emittance={self.emittance},intensity={self.intensity},beta={self.beta},luminosity={self.luminosity},octupoles={self.octupoles},crab_cavities={self.crab_cavities})"

    def clone(self, **kwargs):
        out = Step(
            self.name,
            self.time,
            self.energy,
            self.emittance,
            self.intensity,
            self.beta,
            self.luminosity,
            self.octupoles,
            self.crab_cavities,
        )
        for key, value in kwargs.items():
            setattr(out, key, value)
        return out

class Cycle:
    scales = {
        "energy": (1, "TeV"),
        "time": (1, "h"),
        "emittance": (1, "$\\mu$m"),
        "intensity": (1, "10E11 ppb"),
        "beta": (1, "m"),
        "luminosity": (1, "10E34 cm$^{-2}$ s$^{-1}$"),
        "octupoles": (1 / 100, "100 A"),
        "crab_cavities": (1 / 100, "100 $\\mu$rad"),
    }

    def __init__(self, name, steps):
        self.name = name
        self.steps = steps

    def plot(self, names, ax=None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 5))
        xv = [step.time for step in self.steps]
        for name in names:
            yv = [getattr(step, name) * self.scales[name][0] for step in self.steps]
            ax.plot(xv, yv, label=f"{name} [{self.scales[name][1]}]")
        for tt in xv:
            ax.axvline(tt, color="k", linestyle="--", alpha=0.5)

        ax.set_xlabel("Time [not to scale]")
        ax.set_ylabel("Value")
        ax.set_title(self.name)
        print(xv)
        print([step.name for step in self.steps])

        ax.set_xticks(xv, labels=[step.name for step in self.steps], rotation=90)
        ax.legend(loc='upper right')
        fig.tight_layout()

run4 = Cycle(
    "An example of Run 4 Schematic Cycle",
    [
        Step("Start injection", 0, 0.45, 2.0, 0, 6, 0, 10,0),
        Step("End of injection", 0.2, 0.45, 2.0, 2.3, 6, 0, 10,0),
        Step("End of ramp", 0.5, 7, 2.0, 2.3, 1, 0, 450,0),
        Step("Start of collapse", 0.6, 7, 2.0, 2.3, 1, 0, 450,0),
        Step("End of collapse", 0.65, 7, 2.0, 2.3, 1, 2, 450,0),
        Step("End of collapse", 0.65, 7, 2.5, 2.2, 1, 2, 450,0),
        Step("Start of levelling", 0.9, 7, 2.5, 2.2, 0.64, 5, 60,190),
        Step("End of levelling", 2, 7, 2.5, 1.4, 0.15, 5, 60,190),
        Step("Dump", 2.5, 7, 2.5, 1.2, 0.15, 4, 60,190),
        ],
)

run4.plot(["energy", "intensity", "beta", "emittance", "luminosity", "crab_cavities", "octupoles"])
plt.savefig("run4.pdf")
plt.show()