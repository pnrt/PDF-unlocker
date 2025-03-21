# Use lightweight Nginx image
FROM nginx:alpine

# Remove default Nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Copy our custom Nginx config
COPY nginx.conf /etc/nginx/conf.d/

# Copy website files to Nginx serving directory
COPY index.html /usr/share/nginx/html/

# Expose HTTP port
EXPOSE 80
