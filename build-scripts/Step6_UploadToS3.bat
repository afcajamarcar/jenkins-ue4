set "str=%~1"
aws s3 cp .\C:\BUILDS_FOLDER\GAME_NAME\GAME_%str%.zip s3://BUCKET_NAME/GAME_NAME/GAME_%str%