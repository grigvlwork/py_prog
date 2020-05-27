import wave
import struct


def chip_and_dale(number):
    old_wav = wave.open("in.wav", mode="rb")
    new_wav = wave.open("out.wav", mode="wb")
    new_wav.setparams(old_wav.getparams())
    frames_count = old_wav.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", old_wav.readframes(frames_count))
    new_data = data[:: number]
    new_frames = struct.pack("<" + str(len(new_data)) + "h", *new_data)
    new_wav.writeframes(new_frames)
    old_wav.close()
    new_wav.close()
