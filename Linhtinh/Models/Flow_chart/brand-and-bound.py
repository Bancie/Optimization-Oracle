import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.add(elm.Resistor())
    d.add(elm.Capacitor())
    d.add(elm.Diode())