This repository contains three example Python projects that compile to a single binary for distribution, using [pex](https://pypi.org/project/pex/).

![Make Python pebbles](./python-pebbles.svg)

Platforms like Rust and Go output a single binary by default. This is nice because a single file is easier to upload, copy around, and work with in general. You also don't have to install any dependencies as they are bundled in. In these examples we demonstrate a similar thing in Python, except that our binaries can also be architecture and version agnostic. You can copy them to any machine and they will run, so long as it has a Python executable somewhere in the path.

This works well for small programs without a ton of dependencies, for example:

 * A command line utility for doing devops tasks.
 * A TCP/IP server on an embedded Raspberry Pi.
 * A web based microservice.

As long as we a) write portable code b) have a Python executable somewhere on the target machine's path, it will run. Fortunately most machines these days have some version of Python installed and it's possible to make your package
completely version independent by coding defensively and conservatively.

# Build

Each script can be built by going into the `example-*` folder and running `make`.

# Bundling architecture specific wheels

It's possible to bundle in wheels containing compiled C code for multiple architectures. Check out the [pex](https://pex.readthedocs.io/en/stable/buildingpex.html#platform) documentation for more details.

# Bundling external resources

It's possible to bundle external resources such as images and HTML files into your single binary. Check [example-http-server](./example-http-server) for more details.
