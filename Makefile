#! /usr/bin/env python

output.yaml: ParseSentences.py
	python3 ParseSentences.py
    
.PHONY: clean
   
clean:
	rm output.yaml
