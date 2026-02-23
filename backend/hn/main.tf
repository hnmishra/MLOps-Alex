provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket_versioning" "hn_versioning" {
  bucket = aws_s3_bucket.hn_bucket123.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket" "hn_bucket123" {
  bucket = "my-tf-test-bucket-hnm-123"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

