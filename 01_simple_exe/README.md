# Simple C++ project using CMake

Just an exe. No tests. No libs.

Uses [Conan](https://conan.io/) to get third-party libs ([fmt](https://github.com/fmtlib/fmt) as an example.)

In the script shown, [Ninja](https://ninja-build.org/) is used to compile, but any other generator could be used.

# Install Conan (optional)

(Assuming pip is python3's pip):

```
pip install conan
conan profile new --detect default
conan profile update settings.compiler.libcxx=libstdc++11 default
```


# Compile

## Using Conan and Ninja

```
mkdir build
cd build
conan install .. --build=missing # Will get the Release version of fmt
conan install .. -s build_type=Debug --build=missing # Will get the Debug version of fmt

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

In Ubuntu, for example, a `sudo apt install libfmt-dev` will get it.

```
mkdir build
cd build
cmake -G Ninja -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
./simple
```
