# Simple C++ project using CMake

Just an exe. No tests. No libs.

But uses [Conan](https://conan.io/) to get third-party libs ([fmt](https://github.com/fmtlib/fmt) as an example.)
And [Ninja](https://ninja-build.org/) to compile the examples.

# Compile

## Using Conan and Ninja

```
mkdir build
cd build
conan install .. -s build_type=Debug --build=missing
conan install .. -s build_type=Release --build=missing

cmake -G Ninja -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH=$(pwd) -DCMAKE_MODULE_PATH=$(pwd) ..
cmake --build .
./simple

cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=$(pwd) -DCMAKE_MODULE_PATH=$(pwd) ..
cmake --build .
./simple
```
Please note that I've used Ninja to compile (-G option)


## Not using Conan
You need to have fmt installed in your system.

In Ubuntu, for example a
`sudo apt install libfmt-dev`
will get it.

```
cmake -G Ninja -DCMAKE_BUILD_TYPE=Debug
cmake --build .
./simple
```
