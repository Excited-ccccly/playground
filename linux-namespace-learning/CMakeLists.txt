set(CMAKE_CXX_STANDARD 11)
add_executable(linux-namespace-learning main.cpp ns_exec.cpp unshare.cpp pidns_init_sleep.cpp multi_pidns.cpp ns_child_exec.cpp simple_init.cpp)