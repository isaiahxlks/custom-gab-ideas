from pydub import AudioSegment
from pydub.generators import Sine

# Helper to make tones
def make_tone(freq, duration_ms, volume=-10):
    return Sine(freq).to_audio_segment(duration=duration_ms).apply_gain(volume)

# Verse riff (chaotic climb)
verse = (
    make_tone(440, 300) +   # A4
    make_tone(494, 300) +   # B4
    make_tone(523, 300) +   # C5
    make_tone(587, 300)     # D5
)

# Chorus riff (anthemic pulse)
chorus = (
    make_tone(660, 400) +   # E5
    make_tone(880, 400) +   # A5
    make_tone(990, 400) +   # B5
    make_tone(1320, 400)    # E6
)

# Bridge (glitch surge)
bridge = (
    make_tone(1200, 150).fade_in(50).fade_out(50) +
    make_tone(1400, 150).fade_in(50).fade_out(50) +
    make_tone(1600, 150).fade_in(50).fade_out(50)
)

# Build the full track: Verse → Chorus → Verse → Chorus → Bridge → Chorus
song = verse + chorus + verse + chorus + bridge + chorus

# Add layered chaos (overlay glitch pulses)
glitch = make_tone(2000, 100).fade_in(30).fade_out(30)
song = song.overlay(glitch * 10, position=200)

# Export the anthem
song.export("brainrot_song_long.wav", format="wav")
print("Extended Brainrot anthem generated: brainrot_song_long.wav")
