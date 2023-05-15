# Example of a Conan recipe for a 3rd party library

This is not a simple example of how to build a recipe in Conan, but it is not overly complicated either.

I want to create a Conan package, async/0.0.1, for Klemens Morgenstern's proposed Boost.Async library.

The problem with this library is that it is in a very early stage of development, and requires some fine-tuning before it can be used.

In particular, it needs to patch its CMakeLists.txt because it does not handle header files properly and as a result they are not installed via "cmake --install".

On the other hand, this library requires Boost.Asio and OpenSSL, which will be obtained via Conan.

Finally, the conanfile.txt file cannot be committed to the official Boost.Async repository, so I'm doing this whole recipe out-of-band, so to speak.

So besides declaring some dependencies, downloading the repo from Github and compiling it with CMake, this recipe shows a way to patch the downloaded code (using 'git apply') and how to test that the recipe is correct.

To patch the original code we make use of two features of Conan:
1. Attribute 'exports_sources', which allows the recipe to have additional files associated with it, in this case the file "patches/fix_install_includes.patch".
2. git.run("apply ...") which will run 'git apply' with that file.

In order to test the recipe, the directory test_package is committed with:
* A conanfile.txt that requires the artifact created by the main recipe
* A CMakeLists.txt that uses the library created by the main recipe
* A example.cpp file with some real Boost.Async code

## How to use this recipe

```
$ git clone https://github.com/raulh39/cpp_examples.git
$ cd cpp_examples/02_conan_third_party_recipe
$ conan create .
```
If everything works as expected, async will be now in the Conan cache, compiled for the detected package_id:
```
$ conan list async/0.0.1#:*
Local Cache
  async
    async/0.0.1
      revisions
        2fa531e9406cea3eebb67a9958d49721 (2023-05-15 11:35:16 UTC)
          packages
            9912f8b9aeaf134387642b48bfb973703fb32769
              info
                settings
                  arch: x86_64
                  build_type: Debug
                  compiler: gcc
                  compiler.cppstd: 20
                  compiler.libcxx: libstdc++11
                  compiler.version: 12
                  os: Linux
                requires
                  boost/1.Y.Z
                  bzip2/1.Y.Z
                  libbacktrace/cci
                  openssl/3.Y.Z
                  zlib/1.Y.Z
```

conan cache can also be used to check that the binaries has been built:
```
conan cache path \
async/0.0.1#2fa531e9406cea3eebb67a9958d49721:9912f8b9aeaf134387642b48bfb973703fb32769 \
--folder=build
```
