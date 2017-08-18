run:
	docker run -it --rm -p 8888:8888 --volume-driver=nfs -v /Users/andy/development/data-science/course/notebooks:/home/jovyan/work jupyter/datascience-notebook

shell:
	docker run -it --rm --volume-driver=nfs -v /Users/andy/development/data-science/course/notebooks:/home/jovyan/work jupyter/datascience-notebook bash