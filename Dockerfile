#https://dragonprogrammer.com/dockerized-django-api-angular-tutorial/
#https://dev.to/domysee/setting-up-a-reverse-proxy-with-nginx-and-docker-compose-29jg
FROM python:3.7


# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ponto_backend.settings
ENV WWW_ROOT "/www_root"
# Set work directory.
RUN mkdir ${WWW_ROOT}

WORKDIR ${WWW_ROOT}

# Copying container initialization script
COPY init-container.bash ${WWW_ROOT}/
RUN chmod +x init-container.bash

# Installing GDAL Packages
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin supervisor

# Copy the requirements first
# Copying the project code after dependencies are installed means that Docker will cache
# the image to include the installed dependencies. This means that when you change your 
# project’s source code, Docker will rebuild the image from the point where we copy the 
# project’s code onto the image, without reinstalling dependencies.
COPY requirements.txt ${WWW_ROOT}/

# Install dependencies.
RUN pip install --upgrade pip
RUN pip install -r ${WWW_ROOT}/requirements.txt


# Copy project code.
COPY . ${WWW_ROOT}/
# Running Permissions
RUN chown -R www-data:www-data ./logs
RUN chmod -R 775 ./logs
RUN chown -R www-data:www-data ./files
RUN chmod -R 775 ./files
RUN chown -R www-data:www-data ./static
RUN chmod -R 775 ./static


STOPSIGNAL SIGTERM
EXPOSE 8000
ENTRYPOINT ["sh", "init-container.bash"]
CMD ["ponto_backend.wsgi", "--timeout 45", "--threads 256", "--workers 2", "0:8000"]
