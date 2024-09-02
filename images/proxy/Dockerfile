FROM nginx:alpine

# Install the stream module
RUN apk add --no-cache nginx-mod-stream

# Copy configuration file
COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]