import wave
import struct


def pitch_and_toss():
    old_wav = wave.open("in.wav", mode="rb")
    new_wav = wave.open("out.wav", mode="wb")
    new_wav.setparams(old_wav.getparams())
    frames_count = old_wav.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h",
                         old_wav.readframes(frames_count))
    len_part = len(data) // 4
    part1 = data[:len_part]
    part2 = data[len_part:len_part * 2]
    part3 = data[len_part * 2: len_part * 3]
    part4 = data[len_part * 3:]
    new_data = part3 + part4 + part1 + part2
    new_frames = struct.pack("<" + str(len(new_data)) + "h", *new_data)
    new_wav.writeframes(new_frames)
    old_wav.close()
    new_wav.close()
