FROM python:3.11-slim

WORKDIR /app

COPY . .

# Install Flask only
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

CMD ["bash", "start.sh"]
