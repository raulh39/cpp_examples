cmake_minimum_required(VERSION 3.22.1)
project(SimpleExe LANGUAGES CXX VERSION 0.1.0)

# Generate compile_commands.json to make it easier to work with clang based tools
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Even it is recomended to create a src subdir, this super simple project don't use it

# As an example, fmt is used. Conan can be used to get it from conan center (see README.md)
find_package(fmt CONFIG)

add_executable(simple)
target_sources(simple PRIVATE main.cpp)
target_link_libraries(simple PUBLIC fmt::fmt)
