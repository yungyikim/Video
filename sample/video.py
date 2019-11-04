
import os
import av

def resolve(filepath):
    container = av.open(filepath)
    print (container)

    stream = next(s for s in container.streams if s.type == 'video')
    print (stream, stream.average_rate)

    for packet in container.demux(stream):
        if packet.dts is None:
            continue

        for frame in packet.decode():
            # Get an RGB PIL.Image of this frame.
            image = frame.to_image()
            print(type(image))

            # Get a numpy array of this frame.
            ndarr = frame.to_ndarray()
            print(type(ndarr))

            # Get an RGB version of this frame.
            rgb = frame.to_rgb()
            print(type(rgb))


if __name__ == '__main__':
    dir = './media'
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        resolve(filepath)
