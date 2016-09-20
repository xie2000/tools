mkdir -p ./out/oc
protoc --plugin=/usr/local/bin/protoc-gen-objc *.proto --objc_out=./out/oc
