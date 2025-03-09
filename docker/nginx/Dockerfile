FROM nginx:1.25-alpine

RUN apk add --no-cache bash openssl

RUN rm /etc/nginx/conf.d/default.conf

# dir SSL certificates
RUN mkdir -p /etc/nginx/ssl

# Generate a self-signed SSL certificate for development
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"

# admin Nginx user
RUN chown -R nginx:nginx /etc/nginx/ssl

# Copy 
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/ /etc/nginx/conf.d/

# Create logs dir
RUN mkdir -p /var/log/nginx
RUN touch /var/log/nginx/access.log /var/log/nginx/error.log
RUN chown -R nginx:nginx /var/log/nginx

# Forward request and error logs to Docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 81 443

CMD ["nginx", "-g", "daemon off;"]