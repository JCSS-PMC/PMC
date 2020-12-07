all:	clean html

html:
	jupyter-book build .

pdf:
	jupyter-book build . --builder latex

clean:
	rm -rfv _build

#end

