FROM public.ecr.aws/lambda/python:3.9
ENV TZ="America/Argentina/San_Juan"
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src/* ./

CMD [ "rss.handler" ]