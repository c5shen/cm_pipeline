git submodule update --init --recursive
cd hm01/tools/python-mincut
if [ -d 'build/' ]; then
    rm -r build/
fi
mkdir build
cd build
cmake .. && make
cd ../../../..
cd cluster-statistics/tools/python-mincut
if [ -d 'build/' ]; then
    rm -r build/
fi
mkdir build
cd build
cmake .. && make
cd ../..