These are some example Python projects that compile into single binaries for distribution, using [pex](https://pypi.org/project/pex/).

Platforms like Rust and Go output a single binary by default. This is nice because a single file is easier to upload, copy around, and work with in general, and also you don't have to install any dependencies.

Here we demonstrate similar advantages using Python, except that our binaries can also be architecture and version agnostic. You can copy them to any machine and they will run, so long as it has a Python executable somewhere in the path.

This works well for small programs without a ton of dependencies, for example:

 * A command line utility for doing devops tasks.
 * A TCP/IP server on an embedded Raspberry Pi.
 * A web based microservice.

As long as we a) write portable code b) have a Python executable somewhere on the target machine's path, it will run. Fortunately most machines these days have some version of Python installed and it's possible to make your package
completely version independent by coding defensively and conservatively.

# Build

Each script can be built by going into the `example-*` folder and running `make`.
