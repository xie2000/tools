md .\out\java
protoc.exe -I=. --java_out=./out/java/ *.proto
pause