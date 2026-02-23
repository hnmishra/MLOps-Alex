output "hn_s3_bucket_print" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.hn_bucket123.bucket
}

output "hn_s3_bucket_arn_print" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.hn_bucket123.arn
}

output "hn_s3_bucket_versioning_print" {
  description = "Versioning status of the S3 bucket"
  value       = aws_s3_bucket_versioning.hn_versioning.versioning_configuration[0].status
}
