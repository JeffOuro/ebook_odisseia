# Stage 1: Build frontend assets with Node.js
FROM node:20-alpine AS frontend
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production PHP + Nginx environment
FROM php:8.3-fpm-alpine

# Install php-extension-installer for fast pre-compiled extension installation
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/

# Install system utilities and PHP extensions via pre-compiled binaries
RUN apk add --no-cache \
    nginx \
    supervisor \
    curl \
    zip \
    unzip \
    sqlite \
    sqlite-dev \
    && install-php-extensions pdo pdo_sqlite mbstring gd bcmath intl opcache

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

# Copy application code
COPY . .
COPY --from=frontend /app/public/build ./public/build

# Install PHP production dependencies
RUN composer install --no-dev --optimize-autoloader --no-interaction

# Production permissions & storage directory setup
RUN mkdir -p storage/framework/views storage/framework/sessions storage/framework/cache storage/logs bootstrap/cache \
    && chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache \
    && chmod -R 775 /var/www/html/storage /var/www/html/bootstrap/cache

# Copy Nginx & Supervisor configuration
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose HTTP port
EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
