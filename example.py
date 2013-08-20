#!/usr/bin/env python
import ostack.endpoints
import ostack.tokens
import ostack.images

print ostack.endpoints.get('image')
print ostack.endpoints.volume()
print ostack.keypairs.list()
print ostack.tokens.get()
print ostack.images.list()
