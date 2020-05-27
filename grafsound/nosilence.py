import wave
import struct


def break_the_silence():
    old_wav = wave.open("in.wav", mode="rb")
    new_wav = wave.open("out.wav", mode="wb")
    new_wav.setparams(old_wav.getparams())
    frames_count = old_wav.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", old_wav.readframes(frames_count))
    new_data = [i for i in data if abs(i) > 5]
    new_frames = struct.pack("<" + str(len(new_data)) + "h", *new_data)
    new_wav.writeframes(new_frames)
    old_wav.close()
    new_wav.close()
