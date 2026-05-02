terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region                      = var.aws_region
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
}

# Security Group
resource "aws_security_group" "flask_sg" {
  name        = "flask-app-sg"
  description = "Security group for Flask app EC2 instance"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Flask App"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = { Name = "flask-app-sg" }
}

# S3 Bucket
resource "aws_s3_bucket" "app_bucket" {
  bucket = var.s3_bucket_name
  tags   = { Name = "flask-app-bucket", Environment = "dev" }
}

resource "aws_s3_bucket_versioning" "app_bucket_versioning" {
  bucket = aws_s3_bucket.app_bucket.id
  versioning_configuration { status = "Enabled" }
}

# EC2 Instance
resource "aws_instance" "flask_ec2" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.flask_sg.id]
  key_name               = var.key_name

  user_data = <<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y python3-pip docker.io
    systemctl start docker
    pip3 install flask
    echo "Flask App Running" > /var/www/index.html
  EOF

  tags = { Name = "flask-ec2-instance", Practical = "DevOps-9" }
}

# Attach S3 bucket to EC2 (via IAM role reference)
output "ec2_public_ip"  { value = aws_instance.flask_ec2.public_ip }
output "s3_bucket_name" { value = aws_s3_bucket.app_bucket.bucket }
output "security_group" { value = aws_security_group.flask_sg.name }
