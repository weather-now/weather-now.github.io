. set-webapp-path.sh
rm -rf $WEBAPP_PATH/dist
npm run build --prefix $WEBAPP_PATH
cp -R ~/WebstormProjects/aws-on-leaflet/dist/* .