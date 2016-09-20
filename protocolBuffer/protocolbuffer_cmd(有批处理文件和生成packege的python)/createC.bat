md .\out\cpp
protoc.exe -I=. --cpp_out=./out/cpp/ *.proto
pause