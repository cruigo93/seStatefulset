FROM python:3.7

RUN mkdir backend
COPY . ./backend
WORKDIR backend

RUN pip install -r req.txt
EXPOSE 9000
ENTRYPOINT ["bash", "run_service.sh"]