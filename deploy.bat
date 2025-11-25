@echo off
echo Syncing DEV -> PROD...

robocopy dev prod /E /NFL /NDL /NJH /NJS /NP /XD __pycache__

echo Files synced.
echo Committing changes...

git add .
git commit -m "Sync dev to prod"
git push

echo Deployment complete!
pause