DOCUMENTATION_CHECKOUT ?= ../documentation

src/anko/proto: $(DOCUMENTATION_CHECKOUT)/proto/gateway.proto
	mkdir -p $@
	python -m grpc_tools.protoc -I $(dir $<) --python_out=$@ --grpc_python_out=$@ $<
