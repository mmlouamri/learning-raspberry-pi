### **What is an LED?**
_(from ChatGPT)_

An **LED** is a small electronic component that lights up when electricity flows through it. It's widely used in everything from TVs to flashlights because it’s efficient, durable, and comes in different colors.

- **LED stands for Light Emitting Diode**:
  - **Light Emitting**: It produces light.
  - **Diode**: It’s a special kind of electrical valve, letting current flow in one direction only.

---

### **How does it work?**

An LED is made from **semiconductor materials**, typically combining elements like gallium, arsenic, or phosphorous. When an electric current flows through the LED, **electrons and holes** in the material recombine, releasing energy in the form of **light** (this is called **electroluminescence**).

---

### **The Technical Details**

#### 1. **Semiconductors and PN Junction**
- Inside an LED is a **PN junction** made from two different types of semiconductor materials:
  - **P-type (positive):** Has extra "holes" (places electrons can jump into).
  - **N-type (negative):** Has extra free electrons.
  
When the two meet:
- A **depletion region** forms where no free charge carriers are available.
- Applying a forward voltage across the LED narrows this region, allowing electrons from the N-side to recombine with holes on the P-side, emitting photons (light).

#### 2. **Why Nonlinear?**

- LEDs don’t follow **Ohm’s Law**, which says that current (I) is proportional to voltage (V), i.e., $V = IR$, where $R$ is constant.
- Instead, the LED’s behavior is governed by the **Shockley diode equation**:
  
  $$I = I_s \left( e^{\frac{qV}{n k T}} - 1 \right)$$
  
  Here:
  - $I_s$: Reverse saturation current (a small constant current).
  - $q$: Electron charge ($1.6 \times 10^{-19} \, \text{C}$).
  - $V$: Voltage across the diode.
  - $n$: Ideality factor (typically 1-2).
  - $k$: Boltzmann constant ($1.38 \times 10^{-23} \, \text{J/K}$).
  - $T$: Temperature in Kelvin.

This equation shows that the current increases exponentially with voltage, making the LED **nonlinear**.

---

### **Light Emission**

The color of light depends on the energy gap ($E_g$) of the semiconductor material. This energy is related to the wavelength ($\lambda$) of the emitted light:
$$E_g = h f = \frac{h c}{\lambda}$$
- $E_g$: Bandgap energy (in electron volts).
- $h$: Planck’s constant ($6.63 \times 10^{-34} \, \text{Js}$).
- $c$: Speed of light ($3 \times 10^8 \, \text{m/s}$).
- $\lambda$: Wavelength of emitted light.

Different semiconductor materials are engineered to produce different $E_g$ values, giving LEDs their wide color range.

---

### **Forward Voltage Threshold**
LEDs need a minimum voltage (called the **forward voltage**, $V_f$) to light up. This threshold is typically:
- **Red LEDs**: 1.8–2.2V
- **Green LEDs**: 2.2–3.0V
- **Blue/White LEDs**: 3.0–3.5V

---

### **Key Characteristics**

1. **Current Limitation**
   - LEDs are sensitive to current. Exceeding their rated current can damage them.
   - A resistor is often placed in series with the LED to limit current. The resistor value can be calculated using:
     
     $$R = \frac{V_s - V_f}{I}$$
     
     Where:
     - $V_s$: Supply voltage.
     - $V_f$: Forward voltage of the LED.
     - $I$: Desired current.

2. **Nonlinear I-V Curve**
   - The relationship between current and voltage for an LED looks like a steep curve: small voltage, almost no current; but once $V_f$ is reached, current rises rapidly.
  
## Resources
- https://en.wikipedia.org/wiki/Shockley_diode_equation
