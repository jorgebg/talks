# TEX_PATH := /usr/local/texlive/2019/bin/x86_64-darwin/

PyConES2019submission.pdf: PyConES2019submission.tex egbib.bib
	bibtex ./PyConES2019submission
	pdflatex PyConES2019submission.tex
	pdflatex PyConES2019submission.tex
