git fetch origin
git reset --hard origin/main
(cd ~/3D-xmaslights-v2/server && yarn)
(cd ~/3D-xmaslights-v2/server && yarn tsc)
pm2 reload index
