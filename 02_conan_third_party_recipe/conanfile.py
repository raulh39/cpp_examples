import os
from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.scm import Git


class asyncRecipe(ConanFile):
    name = "async"
    version = "0.0.1"
    exports_sources = "patches*"

    # Optional metadata
    license = "Boost Software License"
    author = "Klemens Morgenstern"
    url = "https://klemens.dev/async/"
    description = "Library that provides a set of easy to use coroutine primitives & utilities for use with Asio"
    topics = ("Asio", "Async", "Coroutines")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    # options = {"shared": [True, False], "fPIC": [True, False]}
    # default_options = {"shared": False, "fPIC": True}

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("boost/1.81.0")
        self.requires("openssl/3.1.0")

    def validate(self):
        check_min_cppstd(self, "20")

    def layout(self):
        cmake_layout(self, src_folder='src')

    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/klemens-morgenstern/async.git", target=".")
        git.checkout("90f58290dbc7216a5a53000ce1dc104c0a92c442")
        patch_file=os.path.join(self.export_sources_folder, "patches/fix_install_includes.patch")
        git.run(f"apply {patch_file}")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["BOOST_ASYNC_BUILD_TESTS"] = False
        tc.cache_variables["BOOST_ASYNC_BUILD_EXAMPLES"] = False
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["boost_async"]
