# Simple C++ project using CMake

Just an exe. No tests. No libs.

Uses [Conan](https://conan.io/) to get third-party libs ([fmt](https://github.com/fmtlib/fmt) as an example.)

In the script shown, [Ninja](https://ninja-build.org/) is used to compile, but any other generator could be used.

# Install Conan (optional)

(Assuming pip is python3's pip):

```
pip install conan
cat <<END > $(conan config home)/profiles/default
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=12
os=Linux

[conf]
tools.cmake.cmaketoolchain:generator=Ninja
END
```


# Compile

## Using Conan and Ninja

```
conan install . --output-folder=build --build=missing
cmake --preset conan-release
cmake --build build
build/simple
```
Debug version:
```
conan install . -s build_type=Debug --output-folder=build --build=missing
cmake --preset conan-debug
cmake --build build
build/simple
```



## Not using Conan
You need to have fmt installed in your system.

In Ubuntu, for example, a `sudo apt install libfmt-dev` will get it.

```
mkdir build
cd build
cmake -G Ninja -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
./simple
```
