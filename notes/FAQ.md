# FAQ

## Button Bouncing
When using a Raspberry Pi with the gpiozero library, I set `btn.when_pressed = led.toggle`, but sometimes when I press the button very quickly, the LED toggles on and off unexpectedly. What is the best way to fix this issue?

**Answer (ChatGPT)**:
The issue you’re encountering is caused by button bouncing or switch debounce. When a button is pressed or released, its mechanical contacts may "bounce," causing multiple very quick on-off signals instead of a single, clean press. This leads to the toggling behavior you described. The `gpiozero` library includes a `bounce_time` parameter, which automatically handles button debounce issues by ignoring any bounces that occur within a specified time window.

```python
from gpiozero import Button, LED
from signal import pause

led = LED(17)
button = Button(18, bounce_time=0.05)  # 50ms debounce time

button.when_pressed = led.toggle
pause()
```

In this example, setting `bounce_time=0.05` (50 milliseconds) helps prevent the LED from toggling multiple times due to quick or multiple presses.